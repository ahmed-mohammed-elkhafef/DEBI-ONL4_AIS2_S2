# 🏠 Boston Housing Price Prediction Project

A Machine Learning project that predicts Boston housing prices using Decision Tree Regression with an interactive Dash web application.

---

## 📋 Project Overview

This project implements a comprehensive machine learning solution for predicting median home values in Boston neighborhoods based on key housing features. The system includes data analysis, model training, and an interactive dashboard for real-time predictions.

### Key Features:
- **Predictive Model**: Decision Tree Regressor optimized with GridSearchCV
- **Interactive Dashboard**: User-friendly Dash web application
- **Data Analysis**: Comprehensive exploratory data analysis and visualization
- **Model Optimization**: Hyperparameter tuning for optimal performance

---

## 👥 Project Team

- **Developer**: Ahmed Elkhafef
- **Supervisor**: Gourge Samuel
- **Date**: March 2026

---

## 📊 Dataset

The project uses the Boston Housing dataset with the following features:

| Feature | Description | Range |
|---------|-------------|-------|
| **RM** | Average number of rooms per dwelling | 3 - 9 rooms |
| **LSTAT** | Percentage of lower status population | 1% - 40% |
| **PTRATIO** | Pupil-teacher ratio by town | 10 - 25 |
| **MEDV** | Median value of homes (Target) | $266,700 - $919,800 |

**Total Data Points**: 489 neighborhoods

---

## 🗂️ Project Structure

```
bosten_housing_Project/
│
├── data/
│   └── housing.csv              # Dataset with 489 housing records
│
├── model/
│   ├── __init__.py
│   └── housing_model.pkl        # Trained Decision Tree model
│
├── notebook/
│   ├── __init__.py
│   └── boston_housing.ipynb     # EDA, training, and analysis
│
├── src/
│   ├── __init__.py
│   ├── visuals.py               # Visualization utilities
│   └── __pycache__/
│
├── dashboard.py                 # Dash web application
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone or Download the Project
```bash
cd bosten_housing_Project
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Verify Model File
Ensure `housing_model.pkl` exists in the `model/` directory.

---

## 💻 Usage

### Running the Dashboard

1. **Start the Application**:
   ```bash
   python dashboard.py
   ```

2. **Access the Dashboard**:
   - Open your browser and navigate to: `http://127.0.0.1:8050`

3. **Make Predictions**:
   - Adjust the input sliders:
     - **Number of Rooms (RM)**: 3-9
     - **Poverty Level (LSTAT)**: 1%-40%
     - **Student-Teacher Ratio (PTRATIO)**: 10-25
   - Click **"Predict Price"** button
   - View the predicted median home value

### Running the Jupyter Notebook

```bash
jupyter notebook notebook/boston_housing.ipynb
```

The notebook includes:
- Data loading and exploration
- Statistical analysis
- Feature correlation studies
- Model training and optimization
- Model evaluation and testing
- Model persistence (saving)

---

## 🤖 Model Details

### Algorithm
**Decision Tree Regressor** with optimized hyperparameters

### Training Process
1. **Data Preprocessing**: 
   - Feature selection (RM, LSTAT, PTRATIO)
   - Train-test split (80/20)

2. **Hyperparameter Tuning**:
   - Method: GridSearchCV
   - Parameter: `max_depth` (1-10)
   - Cross-validation: 10-fold ShuffleSplit
   - Scoring: R² metric

3. **Optimal Model**:
   - Best max_depth: Determined via grid search
   - Trained on 80% of data
   - Validated on 20% test set

### Model Performance
- **Scoring Metric**: R² (Coefficient of Determination)
- **Cross-Validation**: 10-fold with 20% test size
- **Optimization**: Grid search over max_depth parameter

---

## 📈 Dashboard Features

### Input Controls
- **Interactive Sliders**: Real-time feature adjustment
- **Tooltips**: Always-visible current values
- **Range Indicators**: Min/max markers on sliders

### Prediction Display
- **Large Price Display**: Clear, formatted currency output
- **Input Summary**: Review of selected parameters
- **Visual Feedback**: Icons and color-coded alerts

### Visualization
- **Feature Chart**: Bar chart showing current input values
- **Color-Coded Features**: Easy visual distinction
- **Responsive Design**: Works on various screen sizes

### Model Information
- Algorithm details
- Feature descriptions
- Model status indicator

---

## 🎨 Technology Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.x** | Core programming language |
| **scikit-learn** | Machine learning algorithms |
| **pandas** | Data manipulation and analysis |
| **numpy** | Numerical computations |
| **Dash** | Web application framework |
| **Plotly** | Interactive visualizations |
| **Dash Bootstrap** | UI components and styling |
| **Jupyter** | Interactive development |
| **joblib/pickle** | Model serialization |

---

## 📝 Example Predictions

| Rooms (RM) | Poverty (LSTAT) | PT Ratio | Predicted Price |
|------------|-----------------|----------|-----------------|
| 6 | 12% | 18 | ~$480,000 |
| 8 | 7% | 12 | ~$685,000 |
| 4 | 32% | 22 | ~$310,000 |
| 5 | 17% | 15 | ~$420,000 |

*Note: Actual predictions may vary based on the trained model.*

---

## 🔧 Configuration

### Dashboard Settings
- **Host**: `127.0.0.1` (localhost)
- **Port**: `8050`
- **Debug Mode**: Enabled (for development)

### Model Path
The dashboard automatically loads the model from:
```python
MODEL_PATH = Path(__file__).parent / "model" / "housing_model.pkl"
```

---

## 🐛 Troubleshooting

### Model Not Loading
- **Issue**: "Model could not be loaded successfully"
- **Solution**: 
  - Verify `housing_model.pkl` exists in `model/` directory
  - Re-run the Jupyter notebook to regenerate the model
  - Check file permissions

### Import Errors
- **Issue**: ModuleNotFoundError
- **Solution**: 
  ```bash
  pip install -r requirements.txt
  ```

### Port Already in Use
- **Issue**: Port 8050 is occupied
- **Solution**: Change port in `dashboard.py`:
  ```python
  app.run(debug=True, host='127.0.0.1', port=8051)  # Use different port
  ```

---

## 📚 Learning Objectives

This project demonstrates:
1. **Data Science Workflow**: From EDA to deployment
2. **Machine Learning**: Supervised learning with regression
3. **Model Optimization**: Hyperparameter tuning with GridSearchCV
4. **Web Development**: Interactive dashboards with Dash
5. **Best Practices**: Code organization, documentation, and deployment

---

## 🔮 Future Enhancements

- [ ] Add more features (crime rate, property tax, etc.)
- [ ] Implement additional algorithms (Random Forest, XGBoost)
- [ ] Add model comparison dashboard
- [ ] Include prediction confidence intervals
- [ ] Deploy to cloud platform (Heroku, AWS, etc.)
- [ ] Add historical price trend analysis
- [ ] Implement user authentication
- [ ] Add data upload feature for custom predictions

---

## 📄 License

This project is developed for educational purposes as part of a Machine Learning course.

---

## 📧 Contact

**Developer**: Ahmed Elkhafef  
**Supervisor**: Gourge Samuel  

For questions or feedback about this project, please contact the development team.

---

## 🙏 Acknowledgments

- Boston Housing Dataset from the UCI Machine Learning Repository
- scikit-learn community for excellent documentation
- Plotly Dash for the interactive framework
- Course instructors and mentors for guidance

---

