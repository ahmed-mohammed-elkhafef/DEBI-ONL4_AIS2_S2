# 🚴 Ford GoBike Data Analysis Project

## 📋 Project Overview
This project presents a comprehensive data analysis of the Ford GoBike bike-sharing system in the San Francisco Bay Area. The project includes exploratory data analysis (EDA), data cleaning, feature engineering, and an interactive dashboard built with Plotly Dash to visualize key insights and trends.

---

## 👥 Project Team
- **Group:** Group 2
- **Supervisor:** George Samuel
- **Date:** March 2026

---

## 📊 Project Components

### 1. **Data Analysis & Preprocessing**
- **Notebook:** `notebooks/Data_Analysis.ipynb`
- **Raw Data:** `data/raw/fordgobike-trip_v2.csv`
- **Cleaned Data:** `data/processed/bike_data_cleaned.csv`

**Key Steps:**
- Data cleaning and handling missing values
- Feature engineering (age groups, duration in minutes, day of week extraction)
- Statistical analysis and outlier detection
- Data transformation and encoding

### 2. **Interactive Dashboard**
- **Technology:** Plotly Dash with Bootstrap Components
- **Files:**
  - `main.py` - Application entry point
  - `dashboard/layout.py` - UI components and layout
  - `dashboard/callbacks.py` - Interactive logic and data filtering

**Dashboard Features:**
- Real-time data filtering (Date Range, User Type, Gender, Age Group)
- 4 main sections with multiple visualizations
- Responsive, modern UI design
- Production-ready modular architecture

---

## 🎯 Key Insights & Visualizations

### Section 1: Overview KPIs
- **Total Trips:** Dynamic count of all bike trips
- **Average Duration:** Mean trip duration in minutes
- **Total Users:** Unique users/bikes count

### Section 2: Time Analysis
- **Trips by Weekday:** Bar chart showing trip distribution across days
- Identifies peak usage days

### Section 3: User Analysis
- **User Type Distribution:** Pie chart (Subscriber vs Customer)
- **Trip Duration Distribution:** Histogram showing trip length patterns
- Insights into user behavior and trip characteristics

### Section 4: Station Analysis
- **Top 10 Start Stations:** Most popular pickup locations
- **Top 10 End Stations:** Most popular drop-off locations
- Horizontal bar charts for easy comparison

---

## 🛠️ Technology Stack

### Data Processing & Analysis
- **Python 3.12+**
- **Pandas 2.2.0** - Data manipulation and analysis
- **NumPy 1.26.4** - Numerical computations
- **Jupyter Notebook** - Interactive analysis

### Dashboard & Visualization
- **Dash 4.0.0** - Web application framework
- **Dash Bootstrap Components 2.0.4** - UI components
- **Plotly 6.5.2** - Interactive visualizations
- **Flask 3.1.2** - Backend web server

---

## 📁 Project Structure

```
Data_Analysi_Prolect/
│
├── data/
│   ├── raw/
│   │   └── fordgobike-trip_v2.csv          # Original dataset
│   └── processed/
│       └── bike_data_cleaned.csv           # Cleaned & processed data
│
├── notebooks/
│   └── Data_Analysis.ipynb                 # EDA & preprocessing notebook
│
├── dashboard/
│   ├── __init__.py                         # Package initializer
│   ├── layout.py                           # Dashboard UI components
│   ├── callbacks.py                        # Interactive logic & callbacks
│   └── __pycache__/                        # Python cache files
│       ├── __init__.cpython-312.pyc
│       ├── callbacks.cpython-312.pyc
│       └── layout.cpython-312.pyc
│
├── main.py                                 # Application entry point
├── requirements.txt                        # Python dependencies
└── README.md                               # Project documentation
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.12 or higher
- pip package manager
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd Data_Analysi_Prolect
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv env
env\Scripts\activate

# Linux/Mac
python3 -m venv env
source env/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Dashboard
```bash
python main.py
```

### Step 5: Access the Dashboard
Open your web browser and navigate to:
```
http://127.0.0.1:8050/
```

---

## 📈 Dataset Information

### Source
Ford GoBike System Data - San Francisco Bay Area bike-sharing trips

### Size
- **Total Records:** 164,785 trips
- **Time Period:** February-March 2019
- **Format:** CSV

### Key Columns
- `start_time`, `end_time` - Trip timestamps
- `duration_sec`, `duration_min` - Trip duration
- `start_station_name`, `end_station_name` - Station information
- `user_type` - Subscriber or Customer
- `member_gender` - Male, Female, Other
- `member_age` - Calculated from birth year
- `age_group` - Youth, Adults, Senior
- `day_of_week` - Monday to Sunday

---

## 🎨 Dashboard Features

### Interactive Filters
1. **Date Range Picker** - Select custom time periods
2. **User Type Dropdown** - Filter by Subscriber/Customer/All
3. **Gender Dropdown** - Filter by Male/Female/Other/All
4. **Age Group Dropdown** - Filter by Youth/Adults/Senior/All

### Dynamic Updates
- All visualizations update in real-time based on filter selections
- KPIs recalculate automatically
- Charts maintain professional styling and formatting

### Responsive Design
- Bootstrap grid system ensures mobile compatibility
- Cards and charts adapt to different screen sizes
- Professional color schemes and icons

---

## 💡 Key Findings

1. **Peak Usage Days:** [Analysis from weekday chart]
2. **User Demographics:** Subscriber vs Customer distribution patterns
3. **Trip Patterns:** Average duration and distribution insights
4. **Station Popularity:** Identification of high-traffic stations
5. **Temporal Trends:** Weekly and daily usage patterns

---

## 🔧 Technical Highlights

### Modular Architecture
- **Separation of Concerns:** Layout, logic, and execution are separated
- **Single Data Load:** Efficient data handling with single CSV read
- **Reusable Components:** Modular design for easy maintenance

### Best Practices
- Clean, well-documented code
- PEP 8 style guidelines
- Production-ready error handling
- Efficient data filtering and processing

### Performance Optimization
- Data loaded once at module initialization
- Efficient pandas operations
- Optimized callback structure

---

## 📝 Future Enhancements

- [ ] Add map visualization for station locations
- [ ] Implement predictive analytics for demand forecasting
- [ ] Add export functionality (PDF/CSV reports)
- [ ] Include weather data correlation analysis
- [ ] Deploy to cloud platform (Heroku/AWS)
- [ ] Add user authentication and personalized dashboards

---

## 📞 Contact & Support

For questions, suggestions, or contributions, please contact:
- **Group 2 Team**
- **Supervisor:** George Samuel

---

## 📄 License

This project is developed for educational purposes as part of the Data Analysis curriculum.

---

## 🙏 Acknowledgments

- Ford GoBike for providing the dataset
- George Samuel for supervision and guidance
- Plotly & Dash communities for excellent documentation
- Bootstrap team for responsive UI components

---

**Built with ❤️ by Group 2 | © 2026 Ford GoBike Data Analysis Project**