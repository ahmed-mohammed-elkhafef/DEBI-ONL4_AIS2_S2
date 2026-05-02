"""
Feature transformation module using PCA.
"""

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA


class FeatureTransformer:
    """
    Handles PCA transformation for dimensionality reduction.
    """
    
    def __init__(self, n_components: int = 2):
        """
        Initialize FeatureTransformer.
        
        Args:
            n_components: Number of principal components
        """
        self.n_components = n_components
        self.pca = None
        self.transformed_data = None
        self.feature_names = None
        
    def fit(self, data: pd.DataFrame) -> 'FeatureTransformer':
        """
        Fit PCA to data.
        
        Args:
            data: Input DataFrame
            
        Returns:
            Self for chaining
        """
        self.pca = PCA(n_components=self.n_components)
        self.pca.fit(data)
        self.feature_names = data.columns.tolist()
        
        cumsum_var = np.cumsum(self.pca.explained_variance_ratio_)
        
        print(f"✓ PCA fitted with {self.n_components} components")
        for i, (var, cumvar) in enumerate(zip(self.pca.explained_variance_ratio_, cumsum_var)):
            print(f"  PC{i+1}: {var:.4f} variance (cumulative: {cumvar:.4f})")
        
        return self
    
    def fit_transform(self, data: pd.DataFrame) -> np.ndarray:
        """
        Fit PCA and transform data in one step.
        
        Args:
            data: Input DataFrame
            
        Returns:
            Transformed array
        """
        self.fit(data)
        return self.transform(data)
    
    def transform(self, data: pd.DataFrame) -> np.ndarray:
        """
        Transform data using fitted PCA.
        
        Args:
            data: Input DataFrame
            
        Returns:
            Transformed array (n_samples, n_components)
        """
        if self.pca is None:
            raise ValueError("PCA not fitted. Call fit() first.")
        
        return self.pca.transform(data)
    
    def inverse_transform(self, data: np.ndarray) -> np.ndarray:
        """
        Inverse transform from PCA space to original feature space.
        
        Args:
            data: Transformed data array
            
        Returns:
            Data in original feature space
        """
        if self.pca is None:
            raise ValueError("PCA not fitted. Call fit() first.")
        
        return self.pca.inverse_transform(data)
    
    def get_components(self) -> np.ndarray:
        """
        Get PCA components (loadings).
        
        Returns:
            Components array (n_components, n_features)
        """
        if self.pca is None:
            raise ValueError("PCA not fitted.")
        return self.pca.components_
    
    def get_explained_variance_ratio(self) -> np.ndarray:
        """
        Get explained variance ratio for each component.
        
        Returns:
            Variance ratios array
        """
        if self.pca is None:
            raise ValueError("PCA not fitted.")
        return self.pca.explained_variance_ratio_
    
    def get_cumsum_variance(self) -> np.ndarray:
        """
        Get cumulative explained variance.
        
        Returns:
            Cumulative variance array
        """
        if self.pca is None:
            raise ValueError("PCA not fitted.")
        return np.cumsum(self.pca.explained_variance_ratio_)
    
    def get_pca_object(self) -> PCA:
        """
        Get the underlying PCA object.
        
        Returns:
            sklearn PCA object
        """
        return self.pca
