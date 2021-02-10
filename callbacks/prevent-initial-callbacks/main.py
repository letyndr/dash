import dash_core_components as dcc
import dash_html_components as html
from dash import Dash
from dash.dependencies import Output, Input
from time import sleep


app = Dash()

app.layout = html.Div(
    [
        html.Div(id="result", children=["hello!!!"]),
        html.Button("Press", id="submit"),
    ]
)


@app.callback(
    Output("result", "children"),
    Input("submit", "n_clicks"),
    prevent_initial_call=True,
)
def update_div(n_clicks):
    return "new content"


if __name__ == "__main__":
    app.run_server(debug=True, port=8051)
