'''
Visualizing results on a dashboard.
'''

# Imports
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('data/most-commonly-rented-movies.csv')

app.layout = html.Div(children=[
    html.H1(children='DvD Rentals'),

    html.Div(children='''Most Commonly Rented Movies'''),

    dcc.Graph(
        id='most-commonly-rented-movies',
        figure={
            'data': [
                dict(
                    x=df['frequency'],
                    y=df['title'],
                    type='bar',
                    orientation='h',
                )
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'width': 1200,
                'height': 1200
            }
        },
        style={'textAlign': 'center'}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
