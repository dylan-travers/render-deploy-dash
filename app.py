from dash import Dash, html, dcc
import plotly.express as px

app = Dash(__name__)

server = app.server

df = px.data.iris()

fig = px.scatter(df, x="sepal_width", y="petal_length", color="species")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(id='graph', figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)

