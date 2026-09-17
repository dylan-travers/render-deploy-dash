from dash import html, register_page

register_page(__name__, path='/', name='Home')

layout = html.Div([

    html.P('Bonjour à tous ! Voici notre travail sur notre initiation à Dash et Git'),

])