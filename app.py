import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
from sunburst import sunburst_departments, sunburst_executive
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
from network_plot import create_elements, create_elements_individual
import dash_cytoscape as cyto
from pprint import pprint
from dash.dependencies import Input, Output, State
import json
from heatmap import heatmap
from histogram import create_histogram

filename = "data/NetworkVis/{}/{}.csv".format('2014-01-06','2014-01-06')
elements = create_elements(filename)

#function who maps indexes from slidebar to days
def get_day(num):
    dic = {1:'2014-01-06', 2:'2014-01-07', 3: '2014-01-08', 4:'2014-01-09',5:'2014-01-10',
     6:'2014-01-13', 7: '2014-01-14', 8: '2014-01-15', 9:'2014-01-16', 10:'2014-01-17'}
    return dic[num]

# TODO: Fix styling 
app.layout = html.Div(
    children = [
        # Navbar with title of dashboard
        dbc.Navbar([
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col([
                                    html.H1("Visual Analytics Group 30"),
                                ],
                            ),
                        ],
                    ),
                ],
            # Put title in the middle
            className = "justify-content-center g-0",
            ), 
        ], className = "bg-dark text-white"),
            dbc.Row([
                dbc.Col([
                    html.H4("Settings", className="text-center bg-danger text-white p-0 m-0"),
                    dcc.Dropdown(
                                id='dropdown-update-layout',
                                value='grid',
                                clearable=False,
                                options=[
                                    {'label': name.capitalize(), 'value': name}
                                    for name in ['grid', 'random', 'circle', 'cose', 'concentric']
                                ], className = "m-4",
                                ),
                    html.H5('Slide from 06-01 to 17-01', className="text-center"),
                    dcc.Slider(1, 10, value=1,
                                id='slider-update-day',
                                marks={
                                    1: {'label' : '06'},# 'style': {'color': '#77b0b1'}},
                                    2: {'label':  '07'},
                                    3: {'label':  '08'},
                                    4: {'label':  '09'},
                                    5: {'label':  '10'},
                                    6: {'label':  '13'},
                                    7: {'label':  '14'},
                                    8: {'label':  '15'},
                                    9: {'label':  '16'},
                                    10: {'label': '17'}},
                                ),
                            html.H5('Categorize per department', className="text-center"),
                            dbc.Row(
                            [
                                dbc.Col(
                                        dcc.Dropdown(
                                            id='dropdown-update-departments',
                                            value='GAStech',
                                            clearable=False,
                                            options=[
                                                {'label': name.capitalize(), 'value': name}
                                                for name in ['GAStech', 'Administration', 'Engineering', 'Executive', 'Facilities', 'Information Technology', 'Security']
                                            ], className = "m-4",
                                            ),),
                                dbc.Col(
                                        dcc.Dropdown(
                                            id='dropdown-update-dept_directions',
                                            value='both',
                                            clearable=False,
                                            options=[
                                                {'label': name.capitalize(), 'value': name}
                                                for name in ['source', 'target', 'both', 'whitin']
                                            ], className = "m-4",
                                            ),),
                            ], className = "g-0 customheight justify-content-center",
                        ),
                dcc.Input(id='username', value='Initial Value', type='text'),
                html.Button(id='submit-button', type='submit', children='Submit'),

                    
                ], width = {'size': 2}, className="border bl border-top-0 border-bottom-0"),
                dbc.Col(
                    [
                        html.H4("GASTech Email Network", className = "text-center bg-danger text-white p-0 m-0"),
                        html.Div([
                                    cyto.Cytoscape(
                                    id='cytoscape-update-layout',
                                    layout={'name': 'grid'},
                                    style={'width': '100%', 'height': '400px'},
                                    elements=elements
                                )
                                ]),
                        html.Div(id='cytoscape-tapNodeData-output', className = "h-75"),
                    ], width = {'size': 6}, className="border bl border-top-0 border-bottom-0",
                    ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.H4("GAStech Organisation ", className = "text-center bg-danger text-white p-0 m-0"),
                                        dcc.Graph(figure=sunburst_executive(), className = "h-75 mt-3"),
                                    ], width = {'size': 6},
                                ),
                                dbc.Col(
                                    [
                                        html.H4("GAStech Board", className = "text-center bg-danger text-white p-0 m-0"),
                                        dcc.Graph(figure=sunburst_departments(), className = "h-75 mt-3"),
                                    ], width = {'size': 6},
                                ),
                            ], className = "g-0 customheight justify-content-center",
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.H4("Plot", className = "text-center bg-danger text-white p-0 m-0"),
                                        dcc.Graph(figure=heatmap(), className = "h-75"),
                                    ], 
                                ),
                            ], className = "g-0 customheight2",
                        ),
                    ], width = {'size': 4}, className = "h-100"
                ),
            ], className = "vh-100 g-0",
        ),
    ],
)

@app.callback(Output('cytoscape-update-layout', 'layout'),
              Input('dropdown-update-layout', 'value'))
def update_layout(layout):
    return {
        'name': layout,
        'animate': True
    }

@app.callback(Output('cytoscape-update-layout', 'elements'),
              Output('cytoscape-tapNodeData-output', 'children'),
              Input('slider-update-day', 'value'),
              Input('dropdown-update-departments', 'value'),
              Input('dropdown-update-dept_directions', 'value'),
            Input('submit-button', 'n_clicks'),
            Input('cytoscape-update-layout', 'tapNodeData'),
            State('username', 'value'))
            
def update_layout(day,dept,direction, click, data, input_val):
    d = round(day)
    if dept == 'GAStech':
        file = "data/NetworkVis/{}/{}.csv".format(get_day(d),get_day(d))
    else:
        if direction == 'whitin':
            file = "data/NetworkVis/{}/{}_{}_{}.csv".format(get_day(d),get_day(d), dept, 'inner')
        else:
            file = "data/NetworkVis/{}/{}_{}_{}.csv".format(get_day(d),get_day(d), dept, direction)

    if click is not None:
        elements = create_elements_individual(file, input_val)
    else:
        elements = create_elements(file)
    
    if data:
        name = data['label']
        hist = create_histogram(file, name)      
    return (      
        elements, hist
    )

# @app.callback(Output('cytoscape-tapNodeData-output', 'children'),
#               Input('cytoscape-update-layout', 'tapNodeData')),
# def displayTapNodeData(data):
#     if data:
#         name = data['label']
        





if __name__ == "__main__":
    app.run_server(debug=True)