# -*- coding: utf-8 -*-
"""
First Dash-app
LAM-data to describe changes in traffic due to the covid-19-pandemic.
Several LAM-data points available. 
Country: Finland
Author: Satu Korhonen
June 2020
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output

df = pd.read_csv('lam_data.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

markdown_text = '''
LAM-data from various points in Finland measuring the amount of traffic.
Please choose a LAM-point from the dropdown menu to see the amount of
traffic from January to May in 2020.
'''
markdown_analysis = '''
Generally speaking, traffic decreased in March as Finland adopted social distancing
and everyone was asked to travel as little as possible. In April, traffic slowly
increased, but has not returned to the level before March.
'''
analysis_points = '''
Points of interest are f.ex.:
    LAM-point 225 - Parainen, where the profile is very different. There is very little 
    sign of decrease in traffic due to Covid-19 restrictions and instead the season
    for going to ones cabin can be clearly seen.
'''
analysis_point1 = '''    
    LAM-point 248 - Salo Muurla, where one can clearly see the change due to the restriction of
    going to or from Uusimaa.
    '''
analysis_point2 = '''    
    LAM-points 1431 - Tornio and 1434 - Kolari, where traffic almost ceased altogether
    as people were discouraged from going to Sweden through there. There is some increase
    as it was discovered that Finns are allowed to travel out of Finland and back again
    even with the restrictions.
    '''
analysis_point3 = '''    
    Total refers to the total of all points listed here, not total of Finnish LAM-points. 
'''

app.layout = html.Div(children=[
    html.H1('Changes in traffic due to the Covid-19 pandemic',
            style ={'textAlign': 'center'}),
    html.H5(markdown_text, style={'textAlign': 'center'}),        
    html.Label('Choose LAM-point'),
        dcc.Dropdown(
            id = 'dropdown_select',    
            options=[{'label': 'Total', 'value':'Sum'},
                     {'label': '9 - Vantaa Ilola', 'value':'9'},
                     {'label': '117 - Munkkiniemi', 'value':'117'},
                     {'label': '149 - Malmi', 'value':'149'},
                     {'label': '198 - Porvoo', 'value':'198'},
                     {'label': '205 - Raisio', 'value':'205'},
                     {'label': '225 - Parainen', 'value':'225'},
                     {'label': '235 - Kupittaa', 'value':'235'},
                     {'label': '248 - Salo Muurla', 'value':'248'},
                     {'label': '438 - Tampere Paasikiventie', 'value':'438'},
                     {'label': '453 - Tampere Mustalahti', 'value':'453'},
                     {'label': '573 - Hamina Summa', 'value':'573'},
                     {'label': '633 - Mikkeli', 'value':'633'},
                     {'label': '733 - Joensuu', 'value':'733'},
                     {'label': '937 - Viitasaari Taimoniemi', 'value':'937'},
                     {'label': '1030 - Vaasa Mt', 'value':'1030'},
                     {'label': '1256 - Oulu Kaukovainio', 'value':'1256'},
                     {'label': '1301 - Kajaani Mineraali', 'value':'1301'},
                     {'label': '1431 - Tornio', 'value':'1431'},
                     {'label': '1434 - Kolari', 'value':'1434'},
                     {'label': '1441 - Tornio Torppi', 'value':'1441'}
                     ],
            value='Sum'),
        dcc.Graph(
            id='graph_with_select'),
        html.Div(markdown_analysis, style={'textAlign': 'left'}), 
        html.Div(analysis_points, style={'textAlign': 'left'}), 
        html.Div(analysis_point1, style={'textAlign': 'left'}),
        html.Div(analysis_point2, style={'textAlign': 'left'}),
        html.Div(analysis_point3, style={'textAlign': 'left'}) 
        ]) 
    

@app.callback( 
    Output('graph_with_select', 'figure'),
    [Input('dropdown_select', 'value')])
def update_time_series(value):
    return {
            'data': [dict(
                x=df['Aika'],
                y=df[value],
                mode='lines'
                )],
            'layout': dict(
                    xaxis={
                            'title': 'Timeline from 1st of January to 31st of May 2020'
                            },
                    yaxis={
                            'title': 'Amount of cars at this LAM-point'
                            }
            )}

if __name__ == '__main__':
    app.run_server()