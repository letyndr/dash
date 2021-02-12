import time
import dash_core_components as dcc
import dash_html_components as html
from dash import Dash
from dash.dependencies import Output, Input, State


app = Dash()
app.layout = html.Div([
    "hello, this is Dash!!!",
    dcc.Input("input"),
    html.Button("Press", id="btn"),
    html.Div(id="result"),
])


@app.callback(
    Output("result", "children"),
    Input("btn", "n_clicks"),
    State("input", "value")
)
def update_div(n_clicks, input_value):
    print(f"n_clicks: {n_clicks}, input value: {input_value}")
    time.sleep(3)
    return input_value


app.run_server()
