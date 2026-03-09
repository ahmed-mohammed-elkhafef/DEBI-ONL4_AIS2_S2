"""
Boston Housing Price Prediction Dashboard
Simple and Clean Implementation
"""

import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import joblib
import numpy as np
from pathlib import Path

# ============ Load Model ============
MODEL_PATH = Path(__file__).parent / "model" / "housing_model.pkl"

try:
    model = joblib.load(MODEL_PATH)
    print("✓ Model loaded successfully")
except Exception as e:
    print(f"✗ Error: {e}")
    model = None

# ============ Create App ============
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.title = "Boston Housing Price Predictor"

# ============ Design Layout ============
app.layout = dbc.Container([
    # Main Title
    dbc.Row([
        dbc.Col([
            html.H1("🏠 Boston Housing Price Predictor", 
                   className="text-center mt-4 mb-2",
                   style={'color': '#2C3E50', 'font-weight': 'bold'}),
            html.P("Predict home prices using Machine Learning",
                  className="text-center text-muted mb-4"),
            html.Hr(style={'border-top': '3px solid #4ECDC4'}),
        ])
    ]),
    
    # Inputs and Results
    dbc.Row([
        # Input Column
        dbc.Col([
            html.H4("📊 Input Features", className="mb-3", style={'color': '#2C3E50'}),
            
            # RM Slider
            dbc.Card([
                dbc.CardBody([
                    html.H5("RM - Number of Rooms", style={'color': '#2C3E50'}),
                    html.P("Average number of rooms per dwelling (3-9)", className="text-muted"),
                    dcc.Slider(
                        id='rm-slider',
                        min=3, max=9, step=1, value=6,
                        marks={3: '3', 6: '6', 9: '9'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    ),
                ])
            ], className="mb-3 shadow-sm"),
            
            # LSTAT Slider
            dbc.Card([
                dbc.CardBody([
                    html.H5("LSTAT - Poverty Level", style={'color': '#2C3E50'}),
                    html.P("Percentage of lower status population (1-40%)", className="text-muted"),
                    dcc.Slider(
                        id='lstat-slider',
                        min=1, max=40, step=0.5, value=12,
                        marks={1: '1%', 20: '20%', 40: '40%'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    ),
                ])
            ], className="mb-3 shadow-sm"),
            
            # PTRATIO Slider
            dbc.Card([
                dbc.CardBody([
                    html.H5("PTRATIO - Student-Teacher Ratio", style={'color': '#2C3E50'}),
                    html.P("Pupil-teacher ratio by town (10-25)", className="text-muted"),
                    dcc.Slider(
                        id='ptratio-slider',
                        min=10, max=25, step=1, value=18,
                        marks={10: '10', 18: '18', 25: '25'},
                        tooltip={"placement": "bottom", "always_visible": True}
                    ),
                ])
            ], className="mb-3 shadow-sm"),
            
            # Predict Button
            dbc.Button(
                "🔮 Predict Price",
                id="predict-button",
                color="primary",
                size="lg",
                className="w-100 mt-3",
                style={'font-weight': 'bold'}
            ),
        ], md=12, lg=5),
        
        # Results Column
        dbc.Col([
            html.H4("💰 Predicted Price", className="mb-3", style={'color': '#2C3E50'}),
            dbc.Card([
                dbc.CardBody([
                    html.Div(id="prediction-output", className="text-center",
                            style={'min-height': '250px', 'padding': '20px'})
                ])
            ], className="mb-4 shadow-sm"),
            
            # Chart
            html.H4("📈 Feature Analysis", className="mb-3", style={'color': '#2C3E50'}),
            dcc.Graph(id='feature-chart', config={'displayModeBar': False})
        ], md=12, lg=7),
    ]),
    
    # Model Information
    dbc.Row([
        dbc.Col([
            dbc.Alert([
                html.H5("ℹ️ Model Information", className="alert-heading"),
                html.Hr(),
                html.P([
                    "📌 Algorithm: Decision Tree Regressor", html.Br(),
                    "📌 Optimal Depth: max_depth = 3", html.Br(),
                    "📌 Input Features: RM, LSTAT, PTRATIO", html.Br(),
                    "📌 Output: Home price in USD", html.Br(),
                    f"📌 Model Status: {'✓ Ready' if model else '✗ Not Available'}"
                ])
            ], color="info", className="mt-4")
        ])
    ]),
    
    # Footer
    html.Hr(className="mt-5"),
    html.P("© 2026 Boston Housing Prediction | Powered by Dash & ML",
           className="text-center text-muted mb-3")
    
], fluid=True, style={'background-color': '#F8F9FA'})

# ============ Helper Functions ============

def create_feature_chart(rm_val, lstat_val, ptratio_val):
    """Create a bar chart for input features"""
    features = ['Number of Rooms<br>(RM)', 'Poverty Level<br>(LSTAT)', 'Student-Teacher Ratio<br>(PTRATIO)']
    values = [rm_val, lstat_val, ptratio_val]
    colors = ['#FF6B6B', '#4ECDC4', '#FFD93D']
    
    fig = go.Figure(data=[
        go.Bar(
            x=features,
            y=values,
            text=[f'{v:.1f}' for v in values],
            textposition='auto',
            marker=dict(color=colors, line=dict(color='#2C3E50', width=1.5)),
            hovertemplate='<b>%{x}</b><br>Value: %{y:.2f}<extra></extra>'
        )
    ])
    
    fig.update_layout(
        title='Current Input Values',
        xaxis_title='Features',
        yaxis_title='Value',
        plot_bgcolor='rgba(240, 240, 240, 0.5)',
        paper_bgcolor='white',
        height=350,
        font=dict(size=12)
    )
    
    return fig

# ============ Prediction Callback ============

@app.callback(
    [Output('prediction-output', 'children'),
     Output('feature-chart', 'figure')],
    [Input('predict-button', 'n_clicks')],
    [State('rm-slider', 'value'),
     State('lstat-slider', 'value'),
     State('ptratio-slider', 'value')]
)
def predict_price(n_clicks, rm_val, lstat_val, ptratio_val):
    """Make price prediction"""
    
    # Create chart (always updated)
    chart = create_feature_chart(rm_val, lstat_val, ptratio_val)
    
    # Before button click
    if n_clicks is None or n_clicks == 0:
        initial_msg = html.Div([
            html.I(className="fas fa-info-circle fa-3x mb-3", 
                  style={'color': '#4ECDC4'}),
            html.H4("Ready to Predict", className="mb-3"),
            html.P("Adjust the input sliders and click 'Predict Price'", 
                  className="text-muted")
        ], style={'padding': '60px 20px'})
        return initial_msg, chart
    
    # Check if model is loaded
    if model is None:
        error_msg = html.Div([
            html.I(className="fas fa-exclamation-triangle fa-3x mb-3", 
                  style={'color': '#FF6B6B'}),
            html.H4("Model Error", className="mb-3", 
                   style={'color': '#FF6B6B'}),
            html.P("Model could not be loaded successfully", className="text-muted")
        ], style={'padding': '60px 20px'})
        return error_msg, chart
    
    try:
        # Make prediction
        features = np.array([[rm_val, lstat_val, ptratio_val]])
        prediction = model.predict(features)[0]
        price = prediction  # The model already returns the price in dollars
        
        # Display result
        result = html.Div([
            html.I(className="fas fa-home fa-4x mb-3", 
                  style={'color': '#4ECDC4'}),
            html.H2(
                f"${price:,.2f}",
                style={
                    'color': '#2C3E50',
                    'font-weight': 'bold',
                    'font-size': '3rem',
                    'margin': '20px 0'
                }
            ),
            html.P("Predicted Median Home Value", 
                  className="text-muted", 
                  style={'font-size': '1.1rem'}),
            html.Hr(style={'margin': '30px 40px'}),
            html.Div([
                html.P([
                    html.Strong("Input Parameters:"), html.Br(),
                    f"🛏️ Number of Rooms: {int(rm_val)}", html.Br(),
                    f"📊 Poverty Level: {lstat_val:.1f}%", html.Br(),
                    f"👨‍🏫 Student-Teacher Ratio: {int(ptratio_val)}"
                ], style={'color': '#555'})
            ])
        ], style={'padding': '40px 20px'})
        
        return result, chart
        
    except Exception as e:
        error_msg = html.Div([
            html.I(className="fas fa-exclamation-circle fa-3x mb-3", 
                  style={'color': '#FF6B6B'}),
            html.H4("Prediction Error", className="mb-3", 
                   style={'color': '#FF6B6B'}),
            html.P(f"An error occurred: {str(e)}", className="text-muted")
        ], style={'padding': '60px 20px'})
        return error_msg, chart

# ============ Run Application ============

if __name__ == '__main__':
    print("="*60)
    print("🚀 Boston Housing Price Predictor")
    print("="*60)
    print(f"✓ Model Status: {'Ready' if model else 'Not Available'}")
    print("🌐 Open browser at: http://127.0.0.1:8050")
    print("="*60)
    
    app.run(debug=True, host='127.0.0.1', port=8050)
