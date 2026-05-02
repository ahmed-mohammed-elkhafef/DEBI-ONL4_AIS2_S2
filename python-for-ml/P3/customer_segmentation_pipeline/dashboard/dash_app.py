"""
Dash-based interactive dashboard for customer segmentation.
"""

import sys
import os
from pathlib import Path
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

# Change to parent directory so relative paths work
os.chdir(Path(__file__).parent.parent)

from src.pipeline import SegmentationPipeline
from src.utils import load_config


# Load pipeline
config = load_config("config/config.yaml")
try:
    pipeline = SegmentationPipeline.load_model(config['model']['pipeline_path'])
    print("✓ Loaded trained pipeline")
except FileNotFoundError:
    print("⚠ Pipeline not found. Run main.py first to train.")
    sys.exit(1)

# Load data
raw_data = pd.read_csv(config['data']['raw_path'])
raw_data = raw_data.drop(columns=config['data']['drop_columns'], errors='ignore')

# Get predictions and data
reduced_data = pipeline.reduced_data
labels = pipeline.labels

# Create DataFrame with cluster assignments
data_with_clusters = raw_data.copy()
data_with_clusters = data_with_clusters.drop(data_with_clusters.index[pipeline.outlier_indices], errors='ignore').reset_index(drop=True)
data_with_clusters['Cluster'] = labels
data_with_clusters['Cluster_Name'] = 'Segment ' + labels.astype(str)

# Get segment profiles
segment_profiles = pipeline.get_segment_profiles()

# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define color scheme
colors = px.colors.qualitative.Set1[:config['clustering']['n_clusters']]

# ============================================================================
# LAYOUT
# ============================================================================

app.layout = dbc.Container([
    
    # Header
    dbc.Row([
        dbc.Col([
            html.H1("Customer Segmentation Dashboard", className="mb-2 mt-4")
        ], width=12)
    ]),
    
    # KPI Cards
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Total Customers", className="card-title"),
                    html.H2(len(data_with_clusters), className="text-primary")
                ])
            ])
        ], width=3),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Number of Segments", className="card-title"),
                    html.H2(config['clustering']['n_clusters'], className="text-success")
                ])
            ])
        ], width=3),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Silhouette Score", className="card-title"),
                    html.H2(f"{pipeline.clustering_model.get_silhouette_score():.3f}", className="text-info")
                ])
            ])
        ], width=3),
        
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Total Features", className="card-title"),
                    html.H2(len(config['data']['features']), className="text-warning")
                ])
            ])
        ], width=3),
    ], className="mb-4"),
    
    # Filters & Controls
    dbc.Row([
        dbc.Col([
            html.H5("Filters:", className="mt-3"),
            dcc.Dropdown(
                id='segment-dropdown',
                options=[
                    {'label': 'All Segments', 'value': 'all'},
                    *[{'label': f'Segment {i}', 'value': i} for i in range(config['clustering']['n_clusters'])]
                ],
                value='all',
                clearable=False
            )
        ], width=6, lg=3),
        
        dbc.Col([
            html.H5("Select Feature:", className="mt-3"),
            dcc.Dropdown(
                id='feature-dropdown',
                options=[{'label': f, 'value': f} for f in config['data']['features']],
                value=config['data']['features'][0],
                clearable=False
            )
        ], width=6, lg=3),
    ], className="mb-4"),
    
    # Main Charts
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='pca-scatter')
        ], width=12, lg=6),
        
        dbc.Col([
            dcc.Graph(id='cluster-distribution')
        ], width=12, lg=6),
    ]),
    
    # Feature distributions
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='feature-box-plot')
        ], width=12, lg=6),
        
        dbc.Col([
            dcc.Graph(id='feature-histogram')
        ], width=12, lg=6),
    ]),
    
    # Segment Profiles
    dbc.Row([
        dbc.Col([
            html.H3("Segment Profiles (Average Spending)", className="mt-4 mb-3"),
            html.Div(id='segment-profiles-table')
        ], width=12)
    ]),
    
], fluid=True, className="bg-light")


# ============================================================================
# CALLBACKS
# ============================================================================

@app.callback(
    Output('pca-scatter', 'figure'),
    Input('segment-dropdown', 'value')
)
def update_pca_scatter(selected_segment):
    """Update PCA scatter plot."""
    
    if selected_segment == 'all':
        mask = np.ones(len(data_with_clusters), dtype=bool)
    else:
        mask = data_with_clusters['Cluster'] == selected_segment
    
    filtered_data = data_with_clusters[mask]
    
    fig = px.scatter(
        filtered_data,
        x=reduced_data.iloc[mask, 0],
        y=reduced_data.iloc[mask, 1],
        color='Cluster_Name',
        hover_data=config['data']['features'][:3],
        title="PCA-Reduced Customer Space (2D)",
        labels={"x": "Dimension 1", "y": "Dimension 2"},
        color_discrete_sequence=colors
    )
    
    fig.update_layout(
        height=500,
        hovermode='closest',
        template='plotly_white'
    )
    
    return fig


@app.callback(
    Output('cluster-distribution', 'figure'),
    Input('segment-dropdown', 'value')
)
def update_cluster_dist(selected_segment):
    """Update cluster distribution chart."""
    
    if selected_segment == 'all':
        dist = data_with_clusters['Cluster'].value_counts().sort_index()
        title = "Cluster Distribution"
    else:
        dist = data_with_clusters[data_with_clusters['Cluster'] == selected_segment]['Cluster'].value_counts()
        title = f"Segment {selected_segment} - Sample Count"
    
    fig = go.Figure(data=[
        go.Bar(
            x=[f"Segment {i}" for i in dist.index],
            y=dist.values,
            marker=dict(color=[colors[i % len(colors)] for i in dist.index]),
            text=dist.values,
            textposition='auto'
        )
    ])
    
    fig.update_layout(
        title=title,
        xaxis_title="Segment",
        yaxis_title="Number of Customers",
        height=450,
        template='plotly_white'
    )
    
    return fig


@app.callback(
    Output('feature-box-plot', 'figure'),
    Input('feature-dropdown', 'value'),
    Input('segment-dropdown', 'value')
)
def update_feature_box(selected_feature, selected_segment):
    """Update feature distribution box plot."""
    
    if selected_segment == 'all':
        plot_data = data_with_clusters
    else:
        plot_data = data_with_clusters[data_with_clusters['Cluster'] == selected_segment]
    
    fig = px.box(
        plot_data,
        x='Cluster_Name',
        y=selected_feature,
        color='Cluster_Name',
        title=f"Distribution of {selected_feature} by Segment",
        color_discrete_sequence=colors
    )
    
    fig.update_layout(
        height=450,
        template='plotly_white',
        showlegend=False
    )
    
    return fig


@app.callback(
    Output('feature-histogram', 'figure'),
    Input('feature-dropdown', 'value'),
    Input('segment-dropdown', 'value')
)
def update_feature_hist(selected_feature, selected_segment):
    """Update feature histogram."""
    
    if selected_segment == 'all':
        plot_data = data_with_clusters
        title = f"{selected_feature} Distribution - All Segments"
    else:
        plot_data = data_with_clusters[data_with_clusters['Cluster'] == selected_segment]
        title = f"{selected_feature} Distribution - Segment {selected_segment}"
    
    fig = px.histogram(
        plot_data,
        x=selected_feature,
        color='Cluster_Name',
        nbins=30,
        title=title,
        color_discrete_sequence=colors
    )
    
    fig.update_layout(
        height=450,
        template='plotly_white'
    )
    
    return fig


@app.callback(
    Output('segment-profiles-table', 'children'),
    Input('segment-dropdown', 'value')
)
def update_profiles_table(selected_segment):
    """Update segment profiles table."""
    
    if selected_segment == 'all':
        profiles = segment_profiles
    else:
        profiles = segment_profiles.iloc[[selected_segment]]
    
    table = dbc.Table.from_dataframe(
        profiles.astype(int),
        striped=True,
        bordered=True,
        hover=True,
        responsive=True
    )
    
    return table


# ============================================================================
# RUN APP
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*60)
    print("Dash Dashboard Running...")
    print("="*60)
    print(f"Open browser at: http://{config['dashboard']['host']}:{config['dashboard']['port']}")
    
    app.run(
        host=config['dashboard']['host'],
        port=config['dashboard']['port'],
        debug=config['dashboard']['debug']
    )
