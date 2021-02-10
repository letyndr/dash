from src.app import app
from dash.dependencies import Input, Output


@app.callback(
    Output("result", "children"),
    Input("btn", "n_clicks"),
)
def update_div(value):
    return value
