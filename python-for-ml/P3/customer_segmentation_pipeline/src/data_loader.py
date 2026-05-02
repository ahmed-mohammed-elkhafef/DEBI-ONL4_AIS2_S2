"""
Data loading module for customer segmentation pipeline.
"""

import pandas as pd
import numpy as np
from typing import Tuple
import os


class DataLoader:
    """
    Handles loading and initial validation of customer data.
    """
    
    def __init__(self, raw_data_path: str, drop_columns: list = None):
        """
        Initialize DataLoader.
        
        Args:
            raw_data_path: Path to raw CSV file
            drop_columns: Columns to drop (e.g., ['Region', 'Channel'])
        """
        self.raw_data_path = raw_data_path
        self.drop_columns = drop_columns or []
        self.data = None
        
    def load(self) -> pd.DataFrame:
        """
        Load data from CSV file.
        
        Returns:
            DataFrame with data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            Exception: If data loading fails
        """
        if not os.path.exists(self.raw_data_path):
            raise FileNotFoundError(f"Data file not found: {self.raw_data_path}")
        
        try:
            self.data = pd.read_csv(self.raw_data_path, encoding='utf-8')
            print(f"✓ Data loaded: {self.data.shape[0]} samples, {self.data.shape[1]} features")
            return self.data
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def preprocess_columns(self) -> pd.DataFrame:
        """
        Drop specified columns and validate.
        
        Returns:
            DataFrame with dropped columns
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load() first.")
        
        # Drop specified columns
        if self.drop_columns:
            self.data = self.data.drop(columns=self.drop_columns, errors='ignore')
            print(f"✓ Dropped columns: {self.drop_columns}")
        
        # Check for NaN values
        if self.data.isnull().sum().sum() > 0:
            print("⚠ Warning: NaN values found")
            self.data = self.data.dropna()
        
        print(f"✓ Final shape: {self.data.shape[0]} samples, {self.data.shape[1]} features")
        return self.data
    
    def get_data(self) -> pd.DataFrame:
        """
        Get the loaded data.
        
        Returns:
            DataFrame
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load() first.")
        return self.data
    
    def get_feature_names(self) -> list:
        """
        Get feature column names.
        
        Returns:
            List of column names
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call load() first.")
        return self.data.columns.tolist()
