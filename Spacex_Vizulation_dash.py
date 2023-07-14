# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Sample data
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 1, 5, 3]
})
spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Initialize the app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Scatter Plot"),
    dcc.Graph(id='scatter-plot'),
    html.Div(id='output')
])

# Define the callback function
@app.callback(
    Output('output', 'children'),
    [Input('scatter-plot', 'hoverData')])
def update_output(hoverData):
    return f"You hovered over point {hoverData['points'][0]['x']}"

# Define the callback function
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('scatter-plot', 'hoverData')])
def update_figure(hoverData):
    fig = px.scatter(df, x='x', y='y')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
