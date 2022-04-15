import email
from click import password_option
import dash
from dash import dcc
import dash_bootstrap_components as dbc

from dash import html
from numpy import unicode_
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
from sunburst import sunburst_departments, sunburst_executive
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
from network_plot import prepare_data
from network_heap import prepare_data_heap

import dash_cytoscape as cyto
from pprint import pprint
from dash.dependencies import Input, Output, State
import json
from histogram import create_histogram, create_histogram_department
from subjects import get_subjects, get_subjects_heap
from lineplot import lineplot
from pok_table import search_on_names
from heatmap import heatmap
from dash import Dash, dash_table
from collections import OrderedDict

#function who maps indexes from slidebar to days
def get_day(num):
    dic = {'Mon 6':'2014-01-06', 'Tue 7':'2014-01-07', 'Wed 8': '2014-01-08', 'Thu 9':'2014-01-09','Fri 10':'2014-01-10',
     'Mon 13':'2014-01-13', 'Tue 14': '2014-01-14', 'Wed 15': '2014-01-15', 'Thu 16':'2014-01-16', 'Fri 17':'2014-01-17'}
    return dic[num]


dic = {'Mat Bramar': 'black', 'Anda Ribera': 'black', 'Rachel Pantanal': 'black', 'Linda Lagos': 'orange', 'Carla Forluniau': 'black', 'Cornelia Lais': 'black',
    'Marin Onda': 'red', 'Isande Borrasca': 'red', 'Axel Calzas': 'red', 'Kare Orilla': 'red', 'Elsa Orilla': 'red', 'Brand Tempestad': 'red', 'Lars Azada': 'red', 'Felix Balas': 'red',
    'Lidelse Dedos': 'red', 'Birgitta Frente': 'red', 'Adra Nubarron': 'red', 'Gustav Cazar': 'red', 'Vira Frente': 'red', 'Willem Vasco-Pais': 'green', 'Ingrid Barranco': 'green',
    'Ada Campo-Corrente': 'green', 'Orhan Strum': 'green', 'Bertrand Ovan': 'purple', 'Emile Arpa': 'purple', 'Varro Awelon': 'purple', 'Dante Coginian': 'purple', 'Albina Hafon': 'purple',
    'Benito Hawelon': 'purple', 'Claudio Hawelon': 'purple', 'Valeria Morlun': 'purple', 'Adan Morlun': 'purple', 'Cecilia Morluniau': 'purple', 'Irene Nant': 'purple', 'Linnea Bergen': 'blue',
    'Lucas Alcazar': 'blue', 'Isak Baza': 'blue', 'Nils Calixto': 'blue', 'Sven Flecha': 'blue', 'Kanon Herrero': 'orange', 'Varja Lagos': 'orange', 'Stenig Fusil': 'orange', 'Hennie Osvaldo': 'orange',
    'Isia Vann': 'orange', 'Edvard Vann': 'orange', 'Felix Resumir': 'orange', 'Loreto Bodrogi': 'orange', 'Hideki Cocinaro': 'orange', 'Inga Ferro': 'orange', 'Ruscella Mies': 'black',
    'Sten Sanjorge Jr': 'green', 'Sten Sanjorge Jr (tethys)': 'black', 'Henk Mies': 'purple', 'Dylan Scozzese': 'purple', 'Minke Mies': 'orange'}


employee_names = list(dic.keys())

employee_names.append('GASTech')


email_df = pd.read_csv('data/email headers.csv', encoding='cp1252')

unique_subjects = list(set(list(email_df['Subject'])))

elements = prepare_data_heap('2014-01-06 09:00', 60)

df_info_associated_employees = search_on_names()

heatm = heatmap(60)

# TODO: Fix styling 
app.layout = html.Div(
    children = [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(dbc.Col(html.H2("VA group 30", className="bg-dark text-white text-center")), className="g-0"),
                        dbc.Row(dbc.Col(id="side-div", className="h-100 m-2"), className="g-0 customHeight"),         
                    ], width={"size": 2}, className="h-75 bg-light p-0 border bl border-bottom-0 border-top-0"),
                dbc.Col(
                    [
                        dbc.Row(dbc.Col(html.H2("Disappearance at GAStech", className="m-0 bg-dark text-white text-center")), className="g-0"),
                        dbc.Row(dbc.Col(id="page-contents", className="h-75 m-2"), className="g-0 customHeight4 mb-4"),
                        dbc.Row(dbc.Col(dbc.Pagination(id="pagination", className="justify-content-center m-0", max_value=3, previous_next=True)), className="g-0"),
                    ], width={"size": 7}, className = 'h-75 bg-light p-0',
                ),
            ], className="vh-100 align-items-center justify-content-center",
        ),
    ],
)

@app.callback(
    [Output("page-contents", "children"),
    Output("side-div", "children")],
    [Input("pagination", "active_page")],
)
def switch_page(page):
    if page == 2:
        return [
            dbc.Row(
            [
                dbc.Row([
                    dbc.Col([
                        html.H5('The goal on this page is, given the historical records and articles*, to find employees that are possibly associated with the POK or even are part of the POK.', className="border bg-white mb-0"),
                        html.H6('* No employee names (either fully, or partially) appear in the articles.', className="border bg-white"),
                    ]),
                ], className=""),
                dbc.Row([
                    dbc.Col([
                        dash_table.DataTable(
                            data=df_info_associated_employees.to_dict('records'),
                            columns=[{'id': c, 'name': c} for c in df_info_associated_employees.columns],
                            style_table={'overflowX': 'auto'},
                            style_data_conditional=[
                                {
                                    'if': {
                                            'row_index':0,  # number | 'odd' | 'even'
                                            
                                          },
                                            'backgroundColor': 'black',
                                            'color': 'white'
                                },
                                {
                                    'if': {
                                            'row_index':1,  # number | 'odd' | 'even'
                                          },
                                            'backgroundColor': 'green',
                                            'color': 'black'
                                },
                                {
                                    'if': {
                                            'row_index':2,  # number | 'odd' | 'even'
                                          },
                                            'backgroundColor': 'purple',
                                            'color': 'white'
                                },
                                {
                                    'if': {
                                            'row_index':3,  # number | 'odd' | 'even'
                                          },
                                            'backgroundColor': 'orange',
                                            'color': 'black'
                                },
                                {
                                    'if': {
                                            'row_index':4,  # number | 'odd' | 'even'
                                          },
                                            'backgroundColor': 'orange',
                                            'color': 'black'
                                },
                                {
                                    'if': {
                                            'row_index':5,  # number | 'odd' | 'even'
                                          },
                                            'backgroundColor': 'orange',
                                            'color': 'black'
                                },
                                {
                                    'if': {
                                            'row_index':6,  # number | 'odd' | 'even'
                                          },
                                            'backgroundColor': 'orange',
                                            'color': 'black'
                                },
                                {
                                    'if': {
                                            'row_index':7,  # number | 'odd' | 'even'
                                          },
                                            'backgroundColor': 'orange',
                                            'color': 'black'
                                },
                                ],
                        ),
                    ]),
                ], className=""),
            ], className="",
        ),
        ], [
            dbc.Row(
                dbc.Col(
                    dcc.Graph(figure=sunburst_executive(), className = "h-100")), className="customHeight3 g-0"), 
            dbc.Row(
                dbc.Col(
                    dcc.Graph(figure=sunburst_departments(), className = "h-100")), className="customHeight3 g-0")
        ]
    if page==3:
        return [
        dbc.Row(
            [
       
            dbc.Col([
            html.H3(id='title-plot-1'),
                cyto.Cytoscape(
                id='cytoscape-update-layout-heat',
                layout={'name': 'grid'},
                style={'width': '100%', 'height': '400px'},
                elements=elements
                #deze hier onder uit commenten als we niet met kleurtjes willen
                ,stylesheet=[
                                    {'selector': 'node','style': {'content': 'data(label)'}},
                                    {'selector': 'edge','style': {'curve-style': 'bezier', 'target-arrow-shape': 'triangle'}},
                                    {'selector': '.black','style': {'background-color': 'black','line-color': 'black'}},
                                    {'selector': '.red','style': {'background-color': 'red','line-color': 'red'}},
                                    {'selector': '.blue','style': {'background-color': 'blue','line-color': 'blue'}},
                                    {'selector': '.orange','style': {'background-color': 'orange','line-color': 'orange'}},
                                    {'selector': '.purple','style': {'background-color': 'purple','line-color': 'purple'}},
                                    {'selector': '.green','style': {'background-color': 'green','line-color': 'green'}},
                                    {'selector': '.orange_pok','style': {'background-color': 'orange','line-color': 'orange', 'shape': 'star'}},
                                    {'selector': '.black_pok','style': {'background-color': 'black','line-color': 'black', 'shape': 'star'}},
                                    {'selector': '.green_pok','style': {'background-color': 'green','line-color': 'green', 'shape': 'star'}},
                                ]
                ), 
            html.H5(id='cytoscape-mouseoverEdgeData-output-1')]),
            
            dbc.Col([
                html.H3(id='title-plot-2'),
                cyto.Cytoscape(
                id='cytoscape-update-layout-heat-2',
                layout={'name': 'grid'},
                style={'width': '100%', 'height': '400px'},
                elements=elements
                #deze hier onder uit commenten als we niet met kleurtjes willen
                ,stylesheet=[
                                    {'selector': 'node','style': {'content': 'data(label)'}},
                                    {'selector': 'edge','style': {'curve-style': 'bezier', 'target-arrow-shape': 'triangle'}},
                                    {'selector': '.black','style': {'background-color': 'black','line-color': 'black'}},
                                    {'selector': '.red','style': {'background-color': 'red','line-color': 'red'}},
                                    {'selector': '.blue','style': {'background-color': 'blue','line-color': 'blue'}},
                                    {'selector': '.orange','style': {'background-color': 'orange','line-color': 'orange'}},
                                    {'selector': '.purple','style': {'background-color': 'purple','line-color': 'purple'}},
                                    {'selector': '.green','style': {'background-color': 'green','line-color': 'green'}},
                                    {'selector': '.orange_pok','style': {'background-color': 'orange','line-color': 'orange', 'shape': 'star'}},
                                    {'selector': '.black_pok','style': {'background-color': 'black','line-color': 'black', 'shape': 'star'}},
                                    {'selector': '.green_pok','style': {'background-color': 'green','line-color': 'green', 'shape': 'star'}},
                                ]
                ), 
            html.H5(id='cytoscape-mouseoverEdgeData-output-2')]),

                
              

            ]),
        dbc.Row(
            dcc.Graph(id='heatmap', figure=heatm, className = "h-100")
        )


        ], [
        dbc.Row(
                dbc.Col(
                    dcc.Graph(figure=sunburst_executive(), className = "h-100")), className="customHeight3 g-0"), 
        dbc.Row(
                dbc.Col(
                    dcc.Graph(figure=sunburst_departments(), className = "h-100")), className="customHeight3 g-0"),
        dbc.Row(dcc.Dropdown(
                            id='dropdown-update-layout-heat',
                            value='circle',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['grid', 'random', 'circle', 'cose', 'concentric']
                            ], className = "")),
        dbc.Row(dcc.Dropdown(
                            id='dropdown-update-layout-heat-2',
                            value='circle',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['grid', 'random', 'circle', 'cose', 'concentric']
                            ], className = "")),  
        dbc.Row(dcc.Dropdown(
                            id='dropdown-interval',
                            value='1 hourly interval',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['2 hourly interval', '1 hourly interval', '30 minutes interval']
                            ], className = "")),
                              
                    ]
    return [], []



@app.callback(Output('heatmap', 'figure'),
              Input('dropdown-interval', 'value'))
def update_layout(value):
    if value == '2 hourly interval':
        inter = 120
    elif value == '1 hourly interval':
        inter = 60
    elif value == '30 minutes interval':
        inter = 30
    return(heatmap(inter))

@app.callback(Output('cytoscape-update-layout', 'layout'),
              Input('dropdown-update-layout', 'value'))
def update_layout(layout):
    return {
        'name': layout,
        'animate': True
    }

@app.callback(Output('cytoscape-update-layout-2', 'layout'),
              Input('dropdown-update-layout-2', 'value'))
def update_layout(layout):
    return {
        'name': layout,
        'animate': True
    }

@app.callback(Output('cytoscape-update-layout-heat', 'layout'),
              Input('dropdown-update-layout-heat', 'value'))
def update_layout(layout):
    return {
        'name': layout,
        'animate': True
    }

@app.callback(Output('cytoscape-update-layout-heat-2', 'layout'),
              Input('dropdown-update-layout-heat-2', 'value'))
def update_layout(layout):
    return {
        'name': layout,
        'animate': True
    }

@app.callback(Output('cytoscape-update-layout-heat', 'elements'),
              Output('cytoscape-update-layout-heat-2', 'elements'),
              Output('title-plot-1', 'children'),
              Output('title-plot-2', 'children'),
              Input('heatmap','clickData'),
              Input('dropdown-interval', 'value')
              )
def update_table(clickData, value):
    if clickData:
        if value == '2 hourly interval':
            inter = 120
        elif value == '1 hourly interval':
            inter = 60
        elif value == '30 minutes interval':
            inter = 30

        xnode = clickData['points'][0]['x']
        ynode = clickData['points'][0]['y']
        elements1 = prepare_data_heap(xnode, inter)
        elements2 = prepare_data_heap(ynode, inter)

        
        return(elements1, elements2, xnode, ynode)

@app.callback(Output('cytoscape-mouseoverEdgeData-output-1', 'children'),
              Input('cytoscape-update-layout-heat', 'tapEdgeData'),
              Input('title-plot-1', 'children'),
              Input('dropdown-interval', 'value'))
def displayTapEdgeData(data, date, value):
    if data: 
        if value == '2 hourly interval':
            inter = 120
        elif value == '1 hourly interval':
            inter = 60
        elif value == '30 minutes interval':
            inter = 30
        return get_subjects_heap(inter, data['source'], data['target'], date)



@app.callback(Output('cytoscape-mouseoverEdgeData-output-2', 'children'),
              Input('cytoscape-update-layout-heat-2', 'tapEdgeData'), #mouseoverEdgeData
              Input('title-plot-2', 'children'),
              Input('dropdown-interval', 'value'))

def displayTapEdgeData(data, date, value):
    if data: 
        if value == '2 hourly interval':
            inter = 120
        elif value == '1 hourly interval':
            inter = 60
        elif value == '30 minutes interval':
            inter = 30
        return get_subjects_heap(inter, data['source'], data['target'], date)



if __name__ == "__main__":
    app.run_server(debug=True)