"""
Dashboard Callbacks Module
===========================
This module contains all callback functions for dashboard interactivity.
The dataset is loaded ONCE at the top and filtered within callbacks.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output

# Load dataset ONCE for all callbacks
df = pd.read_csv('data/processed/bike_data_cleaned.csv')

# Convert start_time to datetime for filtering
df['start_time'] = pd.to_datetime(df['start_time'])


def register_callbacks(app):
    """
    Registers all callback functions for the dashboard.
    
    Args:
        app: The Dash application instance
    """
    
    @app.callback(
        [
            Output('kpi-total-trips', 'children'),
            Output('kpi-avg-duration', 'children'),
            Output('kpi-total-users', 'children'),
            Output('time-analysis-chart', 'figure'),
            Output('user-type-chart', 'figure'),
            Output('duration-histogram', 'figure'),
            Output('start-station-chart', 'figure'),
            Output('end-station-chart', 'figure'),
        ],
        [
            Input('date-range-filter', 'start_date'),
            Input('date-range-filter', 'end_date'),
            Input('user-type-filter', 'value'),
            Input('gender-filter', 'value'),
            Input('age-group-filter', 'value'),
        ]
    )
    def update_dashboard(start_date, end_date, user_type, gender, age_group):
        """
        Main callback function that updates all dashboard components based on filter selections.
        
        Args:
            start_date: Start date from date range picker
            end_date: End date from date range picker
            user_type: Selected user type (Subscriber/Customer/All)
            gender: Selected gender (Male/Female/Other/All)
            age_group: Selected age group (Youth/Adults/Senior/All)
            
        Returns:
            tuple: All updated components (KPIs and charts)
        """
        
        # Create a copy of the dataframe for filtering
        filtered_df = df.copy()
        
        # Apply Date Range Filter
        if start_date and end_date:
            filtered_df = filtered_df[
                (filtered_df['start_time'].dt.date >= pd.to_datetime(start_date).date()) &
                (filtered_df['start_time'].dt.date <= pd.to_datetime(end_date).date())
            ]
        
        # Apply User Type Filter
        if user_type and user_type != 'All':
            filtered_df = filtered_df[filtered_df['user_type'] == user_type]
        
        # Apply Gender Filter
        if gender and gender != 'All':
            if gender == 'Male':
                filtered_df = filtered_df[filtered_df['member_gender_Male'] == True]
            elif gender == 'Female':
                filtered_df = filtered_df[filtered_df['member_gender_Female'] == True]
            elif gender == 'Other':
                filtered_df = filtered_df[filtered_df['member_gender_Other'] == True]
        
        # Apply Age Group Filter
        if age_group and age_group != 'All':
            filtered_df = filtered_df[filtered_df['age_group'] == age_group]
        
        # ==================== SECTION 1: KPIs ====================
        
        # KPI 1: Total Trips
        total_trips = f"{len(filtered_df):,}"
        
        # KPI 2: Average Duration (in minutes)
        avg_duration = f"{filtered_df['duration_min'].mean():.2f}" if len(filtered_df) > 0 else "0.00"
        
        # KPI 3: Total Users (unique bike_id as proxy for users)
        total_users = f"{filtered_df['bike_id'].nunique():,}"
        
        # ==================== SECTION 2: Time Analysis ====================
        
        # Chart: Trips by Weekday
        # Define the correct order for days of the week
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        # Use day_of_week column (assuming it's in the data)
        if 'day_of_week' in filtered_df.columns:
            weekday_counts = filtered_df['day_of_week'].value_counts()
            weekday_df = pd.DataFrame({
                'Day': weekday_counts.index,
                'Trips': weekday_counts.values
            })
        else:
            # Extract day name from start_time
            filtered_df['day_name'] = filtered_df['start_time'].dt.day_name()
            weekday_counts = filtered_df['day_name'].value_counts()
            weekday_df = pd.DataFrame({
                'Day': weekday_counts.index,
                'Trips': weekday_counts.values
            })
        
        # Sort by day order
        weekday_df['Day'] = pd.Categorical(weekday_df['Day'], categories=day_order, ordered=True)
        weekday_df = weekday_df.sort_values('Day')
        
        time_fig = px.bar(
            weekday_df,
            x='Day',
            y='Trips',
            title='Number of Trips by Day of the Week',
            color='Trips',
            color_continuous_scale='Blues',
            labels={'Trips': 'Number of Trips'}
        )
        time_fig.update_layout(
            xaxis_title="Day of the Week",
            yaxis_title="Number of Trips",
            showlegend=False,
            plot_bgcolor='white'
        )
        
        # ==================== SECTION 3: User Analysis ====================
        
        # Chart 1: User Type Distribution (Pie Chart)
        user_type_counts = filtered_df['user_type'].value_counts().reset_index()
        user_type_counts.columns = ['User Type', 'Count']
        
        user_type_fig = px.pie(
            user_type_counts,
            values='Count',
            names='User Type',
            title='Subscriber vs Customer Distribution',
            color_discrete_sequence=px.colors.qualitative.Set3,
            hole=0.3
        )
        user_type_fig.update_traces(textposition='inside', textinfo='percent+label')
        
        # Chart 2: Trip Duration Distribution (Histogram)
        # Filter extreme outliers for better visualization (durations > 120 mins)
        duration_data = filtered_df[filtered_df['duration_min'] <= 120]['duration_min']
        
        duration_fig = px.histogram(
            duration_data,
            nbins=50,
            title='Trip Duration Distribution (0-120 mins)',
            labels={'value': 'Duration (minutes)', 'count': 'Frequency'},
            color_discrete_sequence=['#FFA500']
        )
        duration_fig.update_layout(
            xaxis_title="Duration (minutes)",
            yaxis_title="Frequency",
            showlegend=False,
            plot_bgcolor='white'
        )
        
        # ==================== SECTION 4: Station Analysis ====================
        
        # Chart 1: Top 10 Start Stations
        start_station_counts = filtered_df['start_station_name'].value_counts().head(10).reset_index()
        start_station_counts.columns = ['Station', 'Trips']
        start_station_counts = start_station_counts.sort_values('Trips')  # Sort for horizontal bar
        
        start_station_fig = px.bar(
            start_station_counts,
            x='Trips',
            y='Station',
            orientation='h',
            title='Top 10 Start Stations',
            color='Trips',
            color_continuous_scale='Greens',
            labels={'Trips': 'Number of Trips'}
        )
        start_station_fig.update_layout(
            xaxis_title="Number of Trips",
            yaxis_title="Station Name",
            showlegend=False,
            plot_bgcolor='white',
            height=400
        )
        
        # Chart 2: Top 10 End Stations
        end_station_counts = filtered_df['end_station_name'].value_counts().head(10).reset_index()
        end_station_counts.columns = ['Station', 'Trips']
        end_station_counts = end_station_counts.sort_values('Trips')  # Sort for horizontal bar
        
        end_station_fig = px.bar(
            end_station_counts,
            x='Trips',
            y='Station',
            orientation='h',
            title='Top 10 End Stations',
            color='Trips',
            color_continuous_scale='Reds',
            labels={'Trips': 'Number of Trips'}
        )
        end_station_fig.update_layout(
            xaxis_title="Number of Trips",
            yaxis_title="Station Name",
            showlegend=False,
            plot_bgcolor='white',
            height=400
        )
        
        return (
            total_trips,
            avg_duration,
            total_users,
            time_fig,
            user_type_fig,
            duration_fig,
            start_station_fig,
            end_station_fig
        )