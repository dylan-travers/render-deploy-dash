from dash import Dash, html, dcc, callback, Input, Output, register_page
import dash_bootstrap_components as dbc
import plotly.express as px

register_page(__name__, name='Espérence de vie par PIB par tête et population')


# Recuperation du dataset Gapminder
df = px.data.gapminder()

# Recuperation du minimum et du maximum des annees disponibles
min_year, max_year = df.year.min(), df.year.max()

# Creation des markers pour le slider sur les annees
slider_marks = {str(year): str(year) for year in df.year.unique()}

# Recuperation de la liste des continents 
opt_continent = df.continent.unique()

# Creation des options du radio items pour l'activation du logarithme sur l'axe des x
opt_log = [{'label': 'Activée', 'value': True}, {'label': 'Désactivée', 'value': False}]

#-----------------------------------------------------------------------#
# Interface                                                             #
#-----------------------------------------------------------------------#


layout = html.Div([    

    html.Header(html.H1('Gapminder dataset')),

    dbc.Row([

        # Affichage du graphique LifeExp by GDPperCap
        dbc.Col([

            dcc.Graph(id='graph-gdp', figure={})

        ], align="start", width=7),

        # Affichage des composantes de selection
        dbc.Col([

            # Ligne contenant le choix des continents et de la transformation log
            dbc.Row(children=[

                # Choix des continents
                dbc.Col([

                    html.H6("Choix des Continents :"),
                    dcc.Checklist(id='checklist', options=opt_continent, value=opt_continent)

                ], width = 6),

                # Transformation logarithmique
                dbc.Col([

                    html.H6("Transformation Log (PIB par tête) :"),
                    dcc.RadioItems(id='radio', options=opt_log, value=True)

                ], width = 6)

            ]),

            html.Br(),

            # Ligne contenant le choix de l'annee
            dbc.Row([

                html.H6("Sélection de l'année :"),
                dcc.Slider(id='slider', min=min_year , max=max_year , value=max_year, marks=slider_marks, step = None)
            ])

        ], align="center", width=4)

    ])

])

#-----------------------------------------------------------------------#
# Serveur                                                               #
#-----------------------------------------------------------------------#


@callback(
    Output('graph-gdp', 'figure'),
    Input('slider', "value"),
    Input('checklist', "value"),
    Input('radio', 'value')
)
def update_graph(year_value, continent_value, log_boolean):
    df_update = df[(df.year == year_value) & df.continent.isin(continent_value)]
    fig = px.scatter(df_update, 
                     x="gdpPercap",
                     y="lifeExp", 
                     size="pop",
                     color="continent",
                     hover_name="country",
                     log_x=log_boolean,
                     size_max=60,
                     title=f'Life expectancy by GDP per capita and population in {year_value}')
    if log_boolean:
        fig.update_xaxes(type="log", range=[2,5])
    else :
        fig.update_xaxes(range=[-5000,50000])
    fig.update_yaxes(range=[20, 100])

    return fig

