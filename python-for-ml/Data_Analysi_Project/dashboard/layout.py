"""
Dashboard Layout Module
========================
This module contains all UI components and layout structure.
The dataset is loaded ONCE at the top and used for filter options.
"""

import pandas as pd
import dash_bootstrap_components as dbc
from dash import dcc, html

# Load dataset ONCE for the entire layout
df = pd.read_csv('data/processed/bike_data_cleaned.csv')

# Convert start_time to datetime
df['start_time'] = pd.to_datetime(df['start_time'])

# Extract unique values for filters
user_types = sorted(df['user_type'].dropna().unique().tolist())
genders = sorted([g for g in df['member_gender_Female'].dropna().unique().tolist() 
                  if pd.notna(g)]) if 'member_gender_Female' in df.columns else []
# Get gender from boolean columns
gender_options = []
if 'member_gender_Male' in df.columns:
    gender_options = ['Male', 'Female', 'Other', 'All']
age_groups = sorted(df['age_group'].dropna().unique().tolist())

# Get date range
min_date = df['start_time'].min().date()
max_date = df['start_time'].max().date()


def create_layout():
    """
    Creates and returns the complete dashboard layout with Bootstrap grid system.
    
    Returns:
        dbc.Container: The complete dashboard layout
    """
    
    layout = dbc.Container([
        
        # Header Section
        dbc.Row([
            dbc.Col([
                html.H1(
                    "🚴 Ford GoBike Data Analysis Dashboard",
                    className="text-center text-primary mb-4 mt-4"
                ),
                html.Hr()
            ])
        ]),
        
        # Filters Section
        dbc.Row([
            dbc.Col([
                html.H4("📊 Filters & Slicers", className="text-info mb-3"),
                
                # Date Range Filter
                html.Label("Select Date Range:", className="fw-bold"),
                dcc.DatePickerRange(
                    id='date-range-filter',
                    min_date_allowed=min_date,
                    max_date_allowed=max_date,
                    start_date=min_date,
                    end_date=max_date,
                    display_format='YYYY-MM-DD',
                    className="mb-3"
                ),
                html.Br(),
                html.Br(),
                
                # User Type Filter
                html.Label("User Type:", className="fw-bold mt-3"),
                dcc.Dropdown(
                    id='user-type-filter',
                    options=[{'label': 'All', 'value': 'All'}] + 
                            [{'label': ut, 'value': ut} for ut in user_types],
                    value='All',
                    clearable=False,
                    className="mb-3"
                ),
                
                # Gender Filter
                html.Label("Member Gender:", className="fw-bold mt-3"),
                dcc.Dropdown(
                    id='gender-filter',
                    options=[{'label': g, 'value': g} for g in gender_options],
                    value='All',
                    clearable=False,
                    className="mb-3"
                ),
                
                # Age Group Filter
                html.Label("Age Group:", className="fw-bold mt-3"),
                dcc.Dropdown(
                    id='age-group-filter',
                    options=[{'label': 'All', 'value': 'All'}] + 
                            [{'label': ag, 'value': ag} for ag in age_groups],
                    value='All',
                    clearable=False,
                    className="mb-3"
                ),
                
            ], width=12, lg=3, className="bg-light p-3 rounded"),
            
            # Main Dashboard Area
            dbc.Col([
                
                # SECTION 1: Overview KPIs
                html.H4("📈 Overview KPIs", className="text-success mb-3"),
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Total Trips", className="card-title text-center"),
                                html.H2(id='kpi-total-trips', className="text-center text-primary")
                            ])
                        ], className="shadow-sm mb-3")
                    ], width=12, md=4),
                    
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Avg Duration (mins)", className="card-title text-center"),
                                html.H2(id='kpi-avg-duration', className="text-center text-success")
                            ])
                        ], className="shadow-sm mb-3")
                    ], width=12, md=4),
                    
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Total Users", className="card-title text-center"),
                                html.H2(id='kpi-total-users', className="text-center text-danger")
                            ])
                        ], className="shadow-sm mb-3")
                    ], width=12, md=4),
                ]),
                
                html.Hr(),
                
                # SECTION 2: Time Analysis
                html.H4("📅 Time Analysis", className="text-info mb-3"),
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Trips by Weekday", className="card-title"),
                                dcc.Graph(id='time-analysis-chart')
                            ])
                        ], className="shadow-sm mb-4")
                    ], width=12)
                ]),
                
                # SECTION 3: User Analysis
                html.H4("👥 User Analysis", className="text-warning mb-3"),
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("User Type Distribution", className="card-title"),
                                dcc.Graph(id='user-type-chart')
                            ])
                        ], className="shadow-sm mb-4")
                    ], width=12, md=6),
                    
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Trip Duration Distribution", className="card-title"),
                                dcc.Graph(id='duration-histogram')
                            ])
                        ], className="shadow-sm mb-4")
                    ], width=12, md=6),
                ]),
                
                # SECTION 4: Station Analysis
                html.H4("🚉 Station Analysis", className="text-danger mb-3"),
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Top 10 Start Stations", className="card-title"),
                                dcc.Graph(id='start-station-chart')
                            ])
                        ], className="shadow-sm mb-4")
                    ], width=12, md=6),
                    
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H5("Top 10 End Stations", className="card-title"),
                                dcc.Graph(id='end-station-chart')
                            ])
                        ], className="shadow-sm mb-4")
                    ], width=12, md=6),
                ]),
                
            ], width=12, lg=9),
            
        ], className="mb-4"),
        
        # Footer
        dbc.Row([
            dbc.Col([
                html.Hr(),
                html.P(
                    "© 2026 Ford GoBike Dashboard | Built with Plotly Dash & Bootstrap",
                    className="text-center text-muted"
                )
            ])
        ])
        
    ], fluid=True, className="p-4")
    
    return layout