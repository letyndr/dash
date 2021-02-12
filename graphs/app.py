from dash import Dash
import dash_html_components as html
# import dash_core_components as dcc
# import plotly.express as px
from graph import graph_object


# df = px.data.iris() # iris is a pandas DataFrame
# fig = px.scatter(df, x="sepal_width", y="sepal_length")

# graph_object = dcc.Graph(figure=fig)

app = Dash()
app.layout = html.Div([
    "hello, this is Dash!!!",
    graph_object,
    ])

app.run_server()

