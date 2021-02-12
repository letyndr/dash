import plotly.express as px
import dash_core_components as dcc


df = px.data.iris() # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")

graph_object = dcc.Graph(figure=fig)
