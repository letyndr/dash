import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash import Dash
from dash.dependencies import Output, Input


global_df = pd.DataFrame({"name": ["Ovalle", "Mayor"], "Goals": [5, 10]})

app = Dash()

app.layout = html.Div([
    dcc.Graph(id='graph'),
    html.Table(id='table'),
    dcc.Dropdown(id='dropdown'),

    # Hidden div inside the app that stores the intermediate value
    html.Div(id='intermediate-value', style={'display': 'none'})
])

@app.callback(Output('intermediate-value', 'children'), Input('dropdown', 'value'))
def clean_data(value):
     # some expensive clean data step
     cleaned_df = global_df[global_df["name"] == "Ovalle"]

     # more generally, this line would be
     # json.dumps(cleaned_df)
     return cleaned_df.to_json(date_format='iso', orient='split')

# @app.callback(Output('graph', 'figure'), Input('intermediate-value', 'children'))
# def update_graph(jsonified_cleaned_data):

#     # more generally, this line would be
#     # json.loads(jsonified_cleaned_data)
#     dff = pd.read_json(jsonified_cleaned_data, orient='split')

#     figure = create_figure(dff)
#     return figure

@app.callback(Output('table', 'children'), Input('intermediate-value', 'children'))
def update_table(jsonified_cleaned_data):
    dff = pd.read_json(jsonified_cleaned_data, orient='split')
    # table = create_table(dff)
    print(dff)
    return

app.run_server(debug=True)
