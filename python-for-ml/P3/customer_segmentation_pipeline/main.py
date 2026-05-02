"""
Main entry point for customer segmentation pipeline.
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.pipeline import SegmentationPipeline
from src.utils import load_config


def main():
    """
    Execute the full segmentation pipeline.
    """
    
    # Load configuration
    config = load_config("config/config.yaml")
    
    # Initialize pipeline
    pipeline = SegmentationPipeline(config)
    
    # Execute pipeline with manual outlier indices (from notebook: [154, 97, 126])
    results = pipeline.fit(manual_outlier_indices=[154, 97, 126])
    
    # Get segment profiles
    print("\n" + "="*60)
    print("SEGMENT PROFILES (Original Scale)")
    print("="*60)
    profiles = pipeline.get_segment_profiles()
    print(profiles)
    
    # Save model
    pipeline.save_model()
    
    print("\n✓ Pipeline execution complete!")
    
    return pipeline, results


if __name__ == "__main__":
    pipeline, results = main()
