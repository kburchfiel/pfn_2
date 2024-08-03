# This code derives from 
# and https://dash.plotly.com/urls .

import dash
from dash import html

dash.register_page(__name__, path = '/page_3')

layout = html.Div([
    html.H1('Page 3'),
    html.Div('This is page 3 of our app.'),
])