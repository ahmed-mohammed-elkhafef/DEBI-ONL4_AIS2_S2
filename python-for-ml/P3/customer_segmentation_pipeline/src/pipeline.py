"""
End-to-end segmentation pipeline orchestrator.
"""

import pandas as pd
import numpy as np
import joblib
import os
from typing import Dict, Tuple, Any

from src.data_loader import DataLoader
from src.preprocessing import Preprocessor
from src.outliers import OutlierDetector
from src.features import FeatureTransformer
from src.modeling import ClusteringModel
from src.utils import ensure_directory


class SegmentationPipeline:
    """
    Complete customer segmentation pipeline.
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize pipeline with configuration.
        
        Args:
            config: Configuration dictionary from config.yaml
        """
        self.config = config
        self.data_loader = None
        self.preprocessor = None
        self.outlier_detector = None
        self.feature_transformer = None
        self.clustering_model = None
        
        self.raw_data = None
        self.scaled_data = None
        self.cleaned_data = None
        self.reduced_data = None
        self.labels = None
        self.centers = None
        
        self.feature_names = None
        self.outlier_indices = None
        
        ensure_directory(config['model']['pipeline_path'].rsplit('/', 1)[0])
        ensure_directory(config['data']['processed_path'])
    
    def load_data(self) -> pd.DataFrame:
        """
        Load raw data.
        
        Returns:
            Raw data DataFrame
        """
        print("\n" + "="*60)
        print("STAGE 1: DATA LOADING")
        print("="*60)
        
        self.data_loader = DataLoader(
            raw_data_path=self.config['data']['raw_path'],
            drop_columns=self.config['data']['drop_columns']
        )
        self.raw_data = self.data_loader.load()
        self.raw_data = self.data_loader.preprocess_columns()
        self.feature_names = self.data_loader.get_feature_names()
        
        return self.raw_data
    
    def preprocess_features(self) -> pd.DataFrame:
        """
        Apply feature scaling.
        
        Returns:
            Scaled data DataFrame
        """
        print("\n" + "="*60)
        print("STAGE 2: FEATURE SCALING")
        print("="*60)
        
        self.preprocessor = Preprocessor(
            method=self.config['scaling']['method']
        )
        self.scaled_data = self.preprocessor.fit_transform(self.raw_data)
        
        return self.scaled_data
    
    def detect_and_remove_outliers(self, manual_indices: list = None) -> pd.DataFrame:
        """
        Detect and remove outliers.
        
        Args:
            manual_indices: Manual list of indices to remove
            
        Returns:
            Cleaned data DataFrame
        """
        print("\n" + "="*60)
        print("STAGE 3: OUTLIER DETECTION & REMOVAL")
        print("="*60)
        
        self.outlier_detector = OutlierDetector(
            iqr_multiplier=self.config['outliers']['iqr_multiplier']
        )
        
        # Fit and identify outliers
        outlier_info = self.outlier_detector.fit(self.scaled_data)
        
        # Use manual indices if provided, else use detected
        indices_to_remove = manual_indices if manual_indices else self.outlier_detector.get_outlier_indices()
        self.outlier_indices = indices_to_remove
        
        # Remove outliers
        self.cleaned_data = self.outlier_detector.remove_outliers(
            self.scaled_data, 
            indices=indices_to_remove
        )
        
        return self.cleaned_data
    
    def reduce_dimensions(self, n_components: int = None) -> np.ndarray:
        """
        Apply PCA for dimensionality reduction.
        
        Args:
            n_components: Number of components (default from config)
            
        Returns:
            Reduced data array
        """
        print("\n" + "="*60)
        print("STAGE 4: DIMENSIONALITY REDUCTION (PCA)")
        print("="*60)
        
        if n_components is None:
            n_components = self.config['pca']['n_components_reduced']
        
        self.feature_transformer = FeatureTransformer(n_components=n_components)
        self.reduced_data = self.feature_transformer.fit_transform(self.cleaned_data)
        
        # Convert to DataFrame for easier handling
        if isinstance(self.reduced_data, np.ndarray):
            dimension_names = [f"Dimension {i+1}" for i in range(self.reduced_data.shape[1])]
            self.reduced_data = pd.DataFrame(self.reduced_data, columns=dimension_names)
        
        return self.reduced_data
    
    def cluster(self, algorithm: str = None, n_clusters: int = None) -> np.ndarray:
        """
        Apply clustering algorithm.
        
        Args:
            algorithm: "kmeans" or "gmm" (default from config)
            n_clusters: Number of clusters (default from config)
            
        Returns:
            Cluster labels array
        """
        print("\n" + "="*60)
        print("STAGE 5: CLUSTERING")
        print("="*60)
        
        if algorithm is None:
            algorithm = self.config['clustering']['algorithm']
        if n_clusters is None:
            n_clusters = self.config['clustering']['n_clusters']
        
        self.clustering_model = ClusteringModel(
            algorithm=algorithm,
            n_clusters=n_clusters,
            random_state=self.config['clustering']['random_state']
        )
        
        self.clustering_model.fit(self.reduced_data.values)
        self.labels = self.clustering_model.get_labels()
        self.centers = self.clustering_model.get_centers()
        
        return self.labels
    
    def fit(self, manual_outlier_indices: list = None) -> Dict[str, Any]:
        """
        Execute full pipeline.
        
        Args:
            manual_outlier_indices: Optional manual outlier indices to remove
            
        Returns:
            Dictionary with pipeline results
        """
        print("\n" + "█" * 60)
        print("█  CUSTOMER SEGMENTATION PIPELINE - FULL FIT")
        print("█" * 60)
        
        # Execute pipeline stages
        self.load_data()
        self.preprocess_features()
        self.detect_and_remove_outliers(manual_outlier_indices)
        self.reduce_dimensions()
        self.cluster()
        
        results = {
            'n_samples': self.raw_data.shape[0],
            'n_features': self.raw_data.shape[1],
            'n_clusters': self.config['clustering']['n_clusters'],
            'silhouette_score': self.clustering_model.get_silhouette_score(),
            'cluster_distribution': self.clustering_model.get_cluster_distribution(),
            'outliers_removed': len(self.outlier_indices) if self.outlier_indices else 0
        }
        
        print("\n" + "█" * 60)
        print("█  PIPELINE COMPLETE")
        print("█" * 60)
        print(f"Samples: {results['n_samples']} | Features: {results['n_features']}")
        print(f"Clusters: {results['n_clusters']} | Silhouette: {results['silhouette_score']:.4f}")
        print(f"Outliers removed: {results['outliers_removed']}")
        
        return results
    
    def predict(self, new_data: pd.DataFrame) -> np.ndarray:
        """
        Predict cluster for new samples.
        
        Args:
            new_data: New data in original scale and features
            
        Returns:
            Predicted cluster labels
        """
        # Scale
        scaled = self.preprocessor.transform(new_data)
        
        # Reduce dimensions
        reduced = self.feature_transformer.transform(scaled)
        
        # Predict cluster
        labels = self.clustering_model.predict(reduced)
        
        return labels
    
    def get_segment_profiles(self) -> pd.DataFrame:
        """
        Get representative profile for each cluster (in original scale).
        
        Returns:
            DataFrame with segment profiles
        """
        # Get centers in reduced space
        centers_reduced = self.centers
        
        # Inverse PCA
        centers_scaled = self.feature_transformer.inverse_transform(centers_reduced)
        
        # Inverse log scaling
        centers_original = self.preprocessor.inverse_transform(centers_scaled)
        
        # Create DataFrame
        segment_names = [f"Segment {i}" for i in range(self.config['clustering']['n_clusters'])]
        profiles = pd.DataFrame(
            np.round(centers_original),
            columns=self.feature_names,
            index=segment_names
        )
        
        return profiles
    
    def save_model(self) -> None:
        """
        Save trained pipeline to disk.
        """
        model_config = self.config['model']
        
        joblib.dump(self.preprocessor, model_config['scaler_path'])
        joblib.dump(self.feature_transformer, model_config['pca_path'])
        joblib.dump(self.clustering_model, model_config['clusterer_path'])
        joblib.dump(self, model_config['pipeline_path'])
        
        print(f"\n✓ Pipeline saved to {model_config['pipeline_path']}")
    
    @staticmethod
    def load_model(pipeline_path: str) -> 'SegmentationPipeline':
        """
        Load trained pipeline from disk.
        
        Args:
            pipeline_path: Path to saved pipeline
            
        Returns:
            Loaded pipeline
        """
        pipeline = joblib.load(pipeline_path)
        print(f"✓ Pipeline loaded from {pipeline_path}")
        return pipeline
