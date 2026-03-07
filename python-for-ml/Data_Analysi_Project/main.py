"""
Main Application File
=====================
This file initializes the Dash application, sets up the layout,
and registers callbacks for interactivity.
"""

import dash
import dash_bootstrap_components as dbc
from dashboard.layout import create_layout
from dashboard.callbacks import register_callbacks

# Initialize Dash app with Bootstrap theme
app = dash.Dash(
    __name__, 
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

# Set application title
app.title = "Ford GoBike Dashboard - Interactive Data Analysis"

# Create and assign layout
app.layout = create_layout()

# Register all callbacks for interactivity
register_callbacks(app)

# Run the server
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8050)