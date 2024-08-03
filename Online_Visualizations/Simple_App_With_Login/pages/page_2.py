# This code derives from 
# and https://dash.plotly.com/urls .

import dash
from dash import html

dash.register_page(__name__, path = '/page_2')

layout = html.Div([
    html.H1('Page 2'),
    html.Div('This is page 2 of our app.'),
])