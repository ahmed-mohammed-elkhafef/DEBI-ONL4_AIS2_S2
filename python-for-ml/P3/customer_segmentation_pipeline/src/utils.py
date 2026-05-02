"""
Utility functions for the customer segmentation pipeline.
"""

import yaml
import os
from typing import Dict, Any


def load_config(config_path: str = "config/config.yaml") -> Dict[str, Any]:
    """
    Load configuration from YAML file.
    
    Args:
        config_path: Path to config.yaml
        
    Returns:
        Configuration dictionary
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    return config


def ensure_directory(path: str) -> None:
    """
    Ensure directory exists, create if not.
    
    Args:
        path: Directory path
    """
    os.makedirs(path, exist_ok=True)
