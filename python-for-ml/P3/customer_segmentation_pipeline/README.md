# Customer Segmentation 

A complete end-to-end machine learning pipeline for customer segmentation using K-Means clustering with dimensionality reduction and outlier detection.

## 📋 Project Overview

This project implements an automated customer segmentation solution that:
- Loads and preprocesses customer spending data
- Applies log transformation for feature scaling
- Detects and removes outliers using Tukey's method
- Performs dimensionality reduction with PCA
- Clusters customers into segments using K-Means
- Provides interactive visualization via Dash dashboard

## 👥 Team

- **Developer**: Ahmed Elkhafef
- **Supervisor**: George Samuel

## 🏗️ Project Structure

```
customer_segmentation_pipeline/
├── main.py                    # Main entry point - trains the pipeline
├── requirements.txt           # Python dependencies
├── config/
│   └── config.yaml           # Configuration file
├── dashboard/
│   └── dash_app.py           # Interactive Dash dashboard
├── data/
│   ├── raw/
│   │   └── customers.csv     # Raw customer data (440 samples, 8 features)
│   └── processed/            # Processed data output
├── models/
│   ├── segmentation_pipeline.pkl   # Trained pipeline
│   ├── scaler.pkl                  # Feature scaler
│   ├── pca.pkl                     # PCA transformer
│   └── clusterer.pkl               # K-Means model
└── src/
    ├── __init__.py
    ├── pipeline.py           # Main pipeline orchestrator
    ├── data_loader.py        # Data loading utilities
    ├── preprocessing.py      # Feature preprocessing
    ├── outliers.py          # Outlier detection
    ├── features.py          # Feature transformation
    ├── modeling.py          # Clustering model
    └── utils.py             # Utility functions
```

## 📊 Features

### Data Features (6 dimensions after preprocessing)
- **Fresh**: Spending on fresh products
- **Milk**: Spending on milk products
- **Grocery**: Spending on grocery items
- **Frozen**: Spending on frozen products
- **Detergents_Paper**: Spending on detergents & paper
- **Delicatessen**: Spending on delicatessen

### Data Statistics
- **Total Samples**: 440 customers
- **Original Features**: 8 (includes Region and Channel)
- **Processed Features**: 6 (after dropping Region and Channel)
- **Outliers Removed**: 3 samples
- **Final Dataset**: 437 samples

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment with dependencies installed

### Setup & Installation

1. **Navigate to the project directory**:
```bash
cd customer_segmentation_pipeline
```

2. **Install dependencies** (if not already installed):
```bash
pip install -r requirements.txt
```

### Running the Pipeline

#### 1. Train the Model
```bash
python main.py
```

**Expected Output**:
```
████████████████████████████████████████████████████████████
█  CUSTOMER SEGMENTATION PIPELINE - FULL FIT
████████████████████████████████████████████████████████████

============================================================
STAGE 1: DATA LOADING
============================================================
✓ Data loaded: 440 samples, 8 features
✓ Dropped columns: ['Region', 'Channel']
✓ Final shape: 440 samples, 6 features

============================================================
STAGE 2: FEATURE SCALING
============================================================
✓ Applied log transformation to 6 features

============================================================
STAGE 3: OUTLIER DETECTION & REMOVAL
============================================================
✓ Tukey's method applied (IQR multiplier: 1.5)
✓ Removed 3 outlier(s)
  Remaining samples: 437

============================================================
STAGE 4: DIMENSIONALITY REDUCTION (PCA)
============================================================
✓ PCA fitted with 2 components
  PC1: 0.4420 variance (cumulative: 0.4420)
  PC2: 0.2703 variance (cumulative: 0.7123)

============================================================
STAGE 5: CLUSTERING
============================================================
✓ KMEANS fitted with 3 clusters
  Silhouette Score: 0.3981

✓ Pipeline execution complete!
```

#### 2. Launch Interactive Dashboard
```bash
python dashboard/dash_app.py
```

Then open your browser and navigate to: **http://127.0.0.1:8050**

## 📈 Model Performance

| Metric | Value |
|--------|-------|
| Silhouette Score | 0.3981 |
| Number of Clusters | 3 |
| PCA Variance Explained | 71.23% |
| Samples After Cleaning | 437 |

## 🎯 Customer Segments

### Segment 0: Budget Buyers
- Fresh: €899
- Milk: €5,205
- Focus: Milk and basic products

### Segment 1: Fresh Enthusiasts
- Fresh: €8,422
- Focused spending on fresh products

### Segment 2: Heavy Buyers
- Fresh: €11,023
- Milk: €7,650
- High spending across categories

## ⚙️ Configuration

Edit `config/config.yaml` to customize:

```yaml
# Data paths
data:
  raw_path: "data/raw/customers.csv"
  processed_path: "data/processed/"

# PCA configuration
pca:
  n_components_full: 6
  n_components_reduced: 2

# Clustering configuration
clustering:
  algorithm: "kmeans"
  n_clusters: 3
  random_state: 42

# Dashboard settings
dashboard:
  host: "127.0.0.1"
  port: 8050
  debug: false
```

## 📦 Dependencies

- **pandas** (≥2.0.0): Data manipulation
- **numpy** (≥1.24.0): Numerical computing
- **scikit-learn** (≥1.3.0): ML algorithms
- **pyyaml** (≥6.0): Configuration parsing
- **joblib** (≥1.3.0): Model serialization
- **plotly** (≥5.14.0): Interactive visualizations
- **dash** (≥2.14.0): Web dashboard framework
- **dash-bootstrap-components** (≥1.4.0): Bootstrap styling
- **scipy** (≥1.11.0): Scientific computing

## 🔄 Pipeline Stages

1. **Data Loading**: Read CSV and validate data
2. **Feature Scaling**: Apply log transformation for normalization
3. **Outlier Detection**: Use Tukey's IQR method to identify outliers
4. **Feature Transformation**: Apply PCA for dimensionality reduction
5. **Clustering**: Apply K-Means to segment customers
6. **Profiling**: Generate segment profiles in original scale
7. **Model Persistence**: Save trained models for inference

## 💾 Model Artifacts

All trained models are saved in the `models/` directory:
- `segmentation_pipeline.pkl` - Complete pipeline object
- `scaler.pkl` - Feature scaler (log transformation)
- `pca.pkl` - PCA transformer (2 components)
- `clusterer.pkl` - K-Means clustering model

These can be loaded for inference on new data.

## 📊 Dashboard Features

The interactive Dash dashboard provides:
- **Segment Overview**: Distribution and metrics
- **Cluster Visualization**: 2D PCA-reduced space
- **Segment Profiles**: Spending patterns by segment
- **New Customer Classification**: Classify individual customers

## 🔍 Usage Examples

### Training and Evaluation
```bash
# Train the pipeline
python main.py
```

### Interactive Dashboard
```bash
# Launch the dashboard
python dashboard/dash_app.py
# Open http://127.0.0.1:8050 in browser
```

### Using the Trained Pipeline (Programmatically)
```python
from src.pipeline import SegmentationPipeline
from src.utils import load_config

# Load config and pipeline
config = load_config("config/config.yaml")
pipeline = SegmentationPipeline.load_model(config['model']['pipeline_path'])

# Make predictions on new data
import pandas as pd
new_customers = pd.DataFrame({
    'Fresh': [10000, 5000, 2000],
    'Milk': [4000, 8000, 15000],
    'Grocery': [6000, 12000, 20000],
    'Frozen': [2000, 3000, 4000],
    'Detergents_Paper': [2000, 8000, 10000],
    'Delicatessen': [1500, 2500, 500]
})

predictions = pipeline.predict(new_customers)
print(predictions)  # [0, 1, 2]
```

## 🛠️ Troubleshooting

### Pipeline Not Running
- Ensure you're in the correct directory: `cd customer_segmentation_pipeline`
- Check that Python dependencies are installed: `pip install -r requirements.txt`

### Dashboard Not Loading
- Make sure the pipeline was trained first: `python main.py`
- Check that port 8050 is not in use
- Verify the working directory is correct

### Missing Config File
- Ensure `config/config.yaml` exists in the pipeline root directory
- Check file paths in the configuration are correct

## 📝 Log Output Example

```
============================================================
SEGMENT PROFILES (Original Scale)
============================================================
             Fresh    Milk  Grocery  Frozen  Detergents_Paper  Delicatessen
Segment 0    899.0  5205.0   7421.0  1256.0            3637.0         331.0
Segment 1   8422.0  1708.0   3193.0   918.0             240.0         614.0
Segment 2  11023.0  7650.0   8901.0  3240.0            3078.0        1859.0

✓ Pipeline saved to models/segmentation_pipeline.pkl
```



**Last Updated**: May 2, 2026
**Status**: ✅ Production Ready
