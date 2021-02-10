import dash_html_components as html
from src.app import app
from dash.dependencies import Input, Output
from src.callbacks import callbacks


app.layout = html.Div(
    children=
    [
        html.Button("Press this button", id="btn"),
        html.Div(id="result"),
    ]
)

# @app.callback(
#     Output("result", "children"),
#     Input("btn", "n_clicks"),
# )
# def update_div(value):
#     return value

app.run_server()
