from dash import Dash, dcc, html, Input, Output, callback, register_page
import plotly.express as px

register_page(__name__, name='Cartographie des élections')

df = px.data.election() 
geojson = px.data.election_geojson()

layout = html.Div([

    html.H4('Political candidate voting pool analysis'),

    html.P("Select a candidate:"),

    dcc.RadioItems(
        id='candidate', 
        options=["Joly", "Coderre", "Bergeron"],
        value="Coderre",
        inline=True
    ),

    dcc.Graph(id="graph")

])

@callback(
    Output("graph", "figure"), 
    Input("candidate", "value"))
def display_choropleth(candidate):

    fig = px.choropleth(
        df, geojson=geojson, color=candidate,
        locations="district", featureidkey="properties.district",
        projection="mercator", range_color=[0, 6500])
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig

if __name__ == '__main__':
    app.run(debug=True)