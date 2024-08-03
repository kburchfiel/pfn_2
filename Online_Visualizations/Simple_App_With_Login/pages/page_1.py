# This code derives from 
# and https://dash.plotly.com/urls .

import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('Home page'),
    html.Div('This is a basic home page.'),
])