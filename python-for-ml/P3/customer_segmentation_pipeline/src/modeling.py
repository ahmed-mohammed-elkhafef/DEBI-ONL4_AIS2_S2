"""
Clustering module for customer segmentation.
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score


class ClusteringModel:
    """
    Handles clustering using KMeans or GMM.
    """
    
    def __init__(self, algorithm: str = "kmeans", n_clusters: int = 3, random_state: int = 42):
        """
        Initialize ClusteringModel.
        
        Args:
            algorithm: "kmeans" or "gmm"
            n_clusters: Number of clusters
            random_state: Random seed
        """
        self.algorithm = algorithm
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.model = None
        self.labels = None
        self.centers = None
        self.silhouette_score_value = None
        
    def fit(self, data: np.ndarray) -> 'ClusteringModel':
        """
        Fit clustering model to data.
        
        Args:
            data: Input array (n_samples, n_features)
            
        Returns:
            Self for chaining
        """
        if self.algorithm == "kmeans":
            self.model = KMeans(
                n_clusters=self.n_clusters,
                random_state=self.random_state,
                init='k-means++',
                n_init=10
            )
            self.model.fit(data)
            self.centers = self.model.cluster_centers_
            self.labels = self.model.labels_
            
        elif self.algorithm == "gmm":
            self.model = GaussianMixture(
                n_components=self.n_clusters,
                random_state=self.random_state
            )
            self.model.fit(data)
            self.labels = self.model.predict(data)
            self.centers = self.model.means_
            
        else:
            raise ValueError(f"Unknown algorithm: {self.algorithm}")
        
        # Calculate silhouette score
        self.silhouette_score_value = silhouette_score(data, self.labels)
        
        print(f"✓ {self.algorithm.upper()} fitted with {self.n_clusters} clusters")
        print(f"  Silhouette Score: {self.silhouette_score_value:.4f}")
        
        return self
    
    def predict(self, data: np.ndarray) -> np.ndarray:
        """
        Predict cluster labels for new data.
        
        Args:
            data: Input array
            
        Returns:
            Cluster labels
        """
        if self.model is None:
            raise ValueError("Model not fitted. Call fit() first.")
        
        if self.algorithm == "kmeans":
            return self.model.predict(data)
        elif self.algorithm == "gmm":
            return self.model.predict(data)
    
    def predict_proba(self, data: np.ndarray) -> np.ndarray:
        """
        Get probability of belonging to each cluster (GMM only).
        
        Args:
            data: Input array
            
        Returns:
            Probability array
        """
        if self.algorithm != "gmm":
            raise ValueError("predict_proba only available for GMM")
        
        return self.model.predict_proba(data)
    
    def get_labels(self) -> np.ndarray:
        """
        Get cluster labels for fitted data.
        
        Returns:
            Labels array
        """
        if self.labels is None:
            raise ValueError("Model not fitted.")
        return self.labels
    
    def get_centers(self) -> np.ndarray:
        """
        Get cluster centers.
        
        Returns:
            Centers array
        """
        if self.centers is None:
            raise ValueError("Model not fitted.")
        return self.centers
    
    def get_silhouette_score(self) -> float:
        """
        Get silhouette score.
        
        Returns:
            Silhouette score
        """
        if self.silhouette_score_value is None:
            raise ValueError("Model not fitted.")
        return self.silhouette_score_value
    
    def get_cluster_distribution(self) -> dict:
        """
        Get distribution of samples across clusters.
        
        Returns:
            Dictionary with cluster counts
        """
        unique, counts = np.unique(self.labels, return_counts=True)
        return {f"Cluster {i}": int(count) for i, count in zip(unique, counts)}
