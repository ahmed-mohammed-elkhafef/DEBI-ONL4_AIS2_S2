"""
Outlier detection and removal module using Tukey's method.
"""

import pandas as pd
import numpy as np


class OutlierDetector:
    """
    Detects and removes outliers using Tukey's method (IQR).
    """
    
    def __init__(self, iqr_multiplier: float = 1.5):
        """
        Initialize OutlierDetector.
        
        Args:
            iqr_multiplier: IQR multiplier for Tukey method (default 1.5)
        """
        self.iqr_multiplier = iqr_multiplier
        self.outlier_indices = []
        self.feature_bounds = {}
        
    def fit(self, data: pd.DataFrame) -> dict:
        """
        Identify outliers in data using Tukey's method.
        
        Args:
            data: Input DataFrame
            
        Returns:
            Dictionary with outlier information per feature
        """
        outlier_info = {}
        all_outlier_indices = set()
        
        for feature in data.columns:
            Q1 = np.percentile(data[feature], 25)
            Q3 = np.percentile(data[feature], 75)
            IQR = Q3 - Q1
            step = self.iqr_multiplier * IQR
            
            lower_bound = Q1 - step
            upper_bound = Q3 + step
            
            self.feature_bounds[feature] = {
                'Q1': Q1,
                'Q3': Q3,
                'IQR': IQR,
                'step': step,
                'lower_bound': lower_bound,
                'upper_bound': upper_bound
            }
            
            # Find outliers for this feature
            outlier_mask = (data[feature] < lower_bound) | (data[feature] > upper_bound)
            feature_outliers = data[outlier_mask].index.tolist()
            
            outlier_info[feature] = {
                'count': len(feature_outliers),
                'indices': feature_outliers,
                'bounds': (lower_bound, upper_bound)
            }
            
            all_outlier_indices.update(feature_outliers)
        
        self.outlier_indices = list(all_outlier_indices)
        
        # Print summary
        print(f"✓ Tukey's method applied (IQR multiplier: {self.iqr_multiplier})")
        for feature, info in outlier_info.items():
            if info['count'] > 0:
                print(f"  {feature}: {info['count']} outliers found")
        
        return outlier_info
    
    def remove_outliers(self, data: pd.DataFrame, indices: list = None) -> pd.DataFrame:
        """
        Remove specified outlier indices from data.
        
        Args:
            data: Input DataFrame
            indices: List of indices to remove. If None, uses detected outliers
            
        Returns:
            DataFrame with outliers removed
        """
        if indices is None:
            indices = self.outlier_indices
        
        cleaned_data = data.drop(data.index[indices]).reset_index(drop=True)
        
        removed_count = len(indices)
        print(f"✓ Removed {removed_count} outlier(s)")
        print(f"  Remaining samples: {cleaned_data.shape[0]}")
        
        return cleaned_data
    
    def get_outlier_indices(self) -> list:
        """
        Get detected outlier indices.
        
        Returns:
            List of outlier indices
        """
        return self.outlier_indices
    
    def get_feature_bounds(self, feature: str) -> dict:
        """
        Get bounds for a specific feature.
        
        Args:
            feature: Feature name
            
        Returns:
            Dictionary with bounds information
        """
        if feature not in self.feature_bounds:
            raise ValueError(f"Feature '{feature}' not in fitted data")
        return self.feature_bounds[feature]
