"""Plotly Dash entry point for Ghana Health Systems Spatial Analysis dashboard."""
import dash
from dash import html

app = dash.Dash(__name__, title="Ghana Health Systems Spatial Dashboard")
server = app.server

app.layout = html.Div([
    html.H1("Ghana Health Systems Spatial Analysis — 261 Districts"),
    html.P("Open dashboard/Ghana_HealthSystems_Spatial_Dashboard.html for the interactive static dashboard."),
    html.P("This Dash app is a stub entry point for the computational pipeline."),
])

if __name__ == "__main__":
    app.run(debug=True)
