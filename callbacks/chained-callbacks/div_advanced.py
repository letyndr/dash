import dash_core_components as dcc
import dash_html_components as html
from dash import Dash
from dash.dependencies import Input, Output, State


app = Dash(suppress_callback_exceptions=True)

app.layout=html.Div(
    id='output',
    children=[
        html.Div("Default thing"),
        html.Button("Load more",id='load-new-content',n_clicks=0),
    ],
)

@app.callback(
    Output('output','children'),
    [Input('load-new-content','n_clicks')],
    [State('output','children')])
def more_output(n_clicks,old_output):
    # if n_clicks:
    return old_output + [
        html.Div(id=f"div-{n_clicks}", children=['Thing {}'.format(n_clicks)]),
        html.Button(f"button-{n_clicks}", id=f"button-{n_clicks}")
    ]

@app.callback(
    Output("div-1", "children"),
    [Input("button-1", "n_clicks")],
    [State("div-1", "children")]
)
def add_content(n_clicks, current_layout):
    if n_clicks:
        return current_layout + [html.Div("WOW!!!!!")]
    else:
        return current_layout


if __name__ == "__main__":
    app.run_server(debug=True)
