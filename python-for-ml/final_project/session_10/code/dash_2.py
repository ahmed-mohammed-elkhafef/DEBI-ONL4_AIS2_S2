import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

df = pd.read_excel(r"D:\01_ENV_AI\DEBI-ONL4\DEBI-ONL4_AIS2_S2\python-for-ml\final_project\session_10\code\Dash.xlsx")
df.head()
app= Dash()
app.title="interactive Dashpord"
num_cols= df.select_dtypes(include='number').columns
app.layout = html.Div([html.H1("interactive dashboard with pie plot"),
                       html.Label("select a value"),
                       dcc.Dropdown(id="column-dropdown",
                       options=[{'label':col,'value':col}for col in num_cols],
                       value= num_cols[0]),
                        dcc.Graph(id='pie-chart') ])
@app.callback(Output('pie-chart','figure'), Input('column-dropdown','value'))
def update_pie(select_col ):
    grouped= df.groupby('Area')[select_col].sum().reset_index()
    fig = px.pie(grouped, names="Area", values=select_col, title= f"distribution of {select_col} by Area", hole = .4,
                 color_discrete_sequence=px.colors.qualitative.Set2)
    return fig
app.run(debug=True)
