"""
Preprocessing module for feature scaling and transformation.
"""

import pandas as pd
import numpy as np


class Preprocessor:
    """
    Handles feature scaling and log transformations.
    """
    
    def __init__(self, method: str = "log"):
        """
        Initialize Preprocessor.
        
        Args:
            method: Scaling method ("log" for natural logarithm)
        """
        self.method = method
        self.scaled_data = None
        
    def fit_transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Apply scaling transformation and fit.
        
        Args:
            data: Input DataFrame
            
        Returns:
            Scaled DataFrame
        """
        if self.method == "log":
            self.scaled_data = np.log(data)
            print(f"✓ Applied log transformation to {data.shape[1]} features")
            return self.scaled_data
        else:
            raise ValueError(f"Unknown scaling method: {self.method}")
    
    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Apply scaling transformation to new data.
        
        Args:
            data: Input DataFrame
            
        Returns:
            Scaled DataFrame
        """
        if self.method == "log":
            return np.log(data)
        else:
            raise ValueError(f"Unknown scaling method: {self.method}")
    
    def inverse_transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Reverse the scaling transformation.
        
        Args:
            data: Scaled DataFrame
            
        Returns:
            Original scale DataFrame
        """
        if self.method == "log":
            return np.exp(data)
        else:
            raise ValueError(f"Unknown scaling method: {self.method}")
    
    def get_scaled_data(self) -> pd.DataFrame:
        """
        Get the scaled data.
        
        Returns:
            Scaled DataFrame
        """
        if self.scaled_data is None:
            raise ValueError("Data not scaled. Call fit_transform() first.")
        return self.scaled_data
