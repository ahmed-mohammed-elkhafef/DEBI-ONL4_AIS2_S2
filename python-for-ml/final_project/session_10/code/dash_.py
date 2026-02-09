from dash import Dash, html, dcc, Input
from dash.dependencies import Input, Output
app = Dash(__name__)
app.layout =html.Div([
    html.Button('submit', id ='number'),
    dcc.Input(placeholder = "Enter a valid number",
               id = 'data', type='number'),
    html.H1(id = 'result')])
@app.callback(Output('result', 'children'),
               Input('number', 'n_clicks'))
def play_data(n,data):
    if n:
        return f"your enter:{data}"
app.run(debug=True)