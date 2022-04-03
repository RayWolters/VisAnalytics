from click import password_option
import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
from sunburst import sunburst_departments, sunburst_executive
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
from network_plot import create_elements, create_elements_individual, prepare_data, prepare_data_department
import dash_cytoscape as cyto
from pprint import pprint
from dash.dependencies import Input, Output, State
import json
from histogram import create_histogram, create_histogram_department
from subjects import get_subjects
from lineplot import lineplot

elements = prepare_data('2014-01-06', "08", '2014-01-17', '22')

#function who maps indexes from slidebar to days
def get_day(num):
    dic = {'Mon 6':'2014-01-06', 'Tue 7':'2014-01-07', 'Wed 8': '2014-01-08', 'Thu 9':'2014-01-09','Fri 10':'2014-01-10',
     'Mon 13':'2014-01-13', 'Tue 14': '2014-01-14', 'Wed 15': '2014-01-15', 'Thu 16':'2014-01-16', 'Fri 17':'2014-01-17'}
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
                    html.H5("Settings network 1", className="text-center bg-danger text-white p-0 m-0"),
                    dcc.Dropdown(
                                id='dropdown-update-layout',
                                value='circle',
                                clearable=False,
                                options=[
                                    {'label': name.capitalize(), 'value': name}
                                    for name in ['grid', 'random', 'circle', 'cose', 'concentric']
                                ], className = "m-4",
                                ),
                    html.H5('Choose Start and End date:', className="text-center"),
                    dbc.Row(
                            [
                                dbc.Col(
                                        dcc.Dropdown(
                                            id='dropdown-start-day',
                                            value='Mon 6',
                                            clearable=False,
                                            options=[
                                                {'label': name.capitalize(), 'value': name}
                                                for name in ['Mon 6', 'Tue 7', 'Wed 8', 'Thu 9', 'Fri 10',
                                                         'Mon 13', 'Tue 14', 'Wed 15', 'Thu 16', 'Fri 17']
                                            ], className = "m-4",
                                            ),),
                                dbc.Col(
                                        dcc.Dropdown(
                                            id='dropdown-start-hour',
                                            value='08:00',
                                            clearable=False,
                                            options=[
                                                {'label': name.capitalize(), 'value': name}
                                                for name in ['08:00', '09:00', '10:00', '11:00', '12:00','13:00','14:00','15:00','16:00',
                                                         '17:00','18:00','19:00', '20:00', '21:00', '22:00', '23:00']
                                            ], className = "m-4",
                                            ),
                                            ),
                                
                                         
                            ],
                        ),
                    dbc.Row(
                            [
                                dbc.Col(
                                        dcc.Dropdown(
                                            id='dropdown-end-day',
                                            value='Mon 6',
                                            clearable=False,
                                            options=[
                                                {'label': name.capitalize(), 'value': name}
                                                for name in ['Mon 6', 'Tue 7', 'Wed 8', 'Thu 9', 'Fri 10',
                                                         'Mon 13', 'Tue 14', 'Wed 15', 'Thu 16', 'Fri 17']
                                            ], className = "m-4",
                                            ),),
                                dbc.Col(
                                        dcc.Dropdown(
                                            id='dropdown-end-hour',
                                            value='23:00',
                                            clearable=False,
                                            options=[
                                                {'label': name.capitalize(), 'value': name}
                                                for name in ['08:00', '09:00', '10:00', '11:00', '12:00','13:00','14:00','15:00','16:00',
                                                         '17:00','18:00','19:00', '20:00', '21:00', '22:00', '23:00']
                                            ], className = "m-4",
                                            ),),
                            ]
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
                                                for name in ['source', 'target', 'both', 'inner']
                                            ], className = "m-4",
                                            ),),
                            ], className = "g-0 justify-content-center",
                        ),






                    html.H5("Settings network 2", className="text-center bg-danger text-white p-0 m-0"),
                    # dcc.Input(style={"margin-left": "15px"}),

                    dcc.Dropdown(
                                id='dropdown-update-layout-2',
                                value='circle',
                                clearable=False,
                                options=[
                                    {'label': name.capitalize(), 'value': name}
                                    for name in ['grid', 'random', 'circle', 'cose', 'concentric']
                                ], className = "m-4",
                                ),
                    html.H5('Choose Start and End date:', className="text-center"),
                    dbc.Row(
                            [
                                dbc.Col(
                                        dcc.Dropdown(
                                            id='dropdown-start-day-2',
                                            value='Tue 7',
                                            clearable=False,
                                            options=[
                                                {'label': name.capitalize(), 'value': name}
                                                for name in ['Mon 6', 'Tue 7', 'Wed 8', 'Thu 9', 'Fri 10',
                                                         'Mon 13', 'Tue 14', 'Wed 15', 'Thu 16', 'Fri 17']
                                            ], className = "m-4",
                                            ),),
                                dbc.Col(
                                        dcc.Dropdown(
                                            id='dropdown-start-hour-2',
                                            value='08:00',
                                            clearable=False,
                                            options=[
                                                {'label': name.capitalize(), 'value': name}
                                                for name in ['08:00', '09:00', '10:00', '11:00', '12:00','13:00','14:00','15:00','16:00',
                                                         '17:00','18:00','19:00', '20:00', '21:00', '22:00', '23:00']
                                            ], className = "m-4",
                                            ),
                                            ),            
                            ],
                        ),
                    dbc.Row(
                            [
                                dbc.Col(
                                        dcc.Dropdown(
                                            id='dropdown-end-day-2',
                                            value='Tue 7',
                                            clearable=False,
                                            options=[
                                                {'label': name.capitalize(), 'value': name}
                                                for name in ['Mon 6', 'Tue 7', 'Wed 8', 'Thu 9', 'Fri 10',
                                                         'Mon 13', 'Tue 14', 'Wed 15', 'Thu 16', 'Fri 17']
                                            ], className = "m-4",
                                            ),),
                                dbc.Col(
                                        dcc.Dropdown(
                                            id='dropdown-end-hour-2',
                                            value='23:00',
                                            clearable=False,
                                            options=[
                                                {'label': name.capitalize(), 'value': name}
                                                for name in ['08:00', '09:00', '10:00', '11:00', '12:00','13:00','14:00','15:00','16:00',
                                                         '17:00','18:00','19:00', '20:00', '21:00', '22:00', '23:00']
                                            ], className = "m-4",
                                            ),),
                            ]
                        ),
                    html.H5('Categorize per department', className="text-center"),
                            dbc.Row(
                            [
                                dbc.Col(
                                        dcc.Dropdown(
                                            id='dropdown-update-departments-2',
                                            value='GAStech',
                                            clearable=False,
                                            options=[
                                                {'label': name.capitalize(), 'value': name}
                                                for name in ['GAStech', 'Administration', 'Engineering', 'Executive', 'Facilities', 'Information Technology', 'Security']
                                            ], className = "m-4",
                                            ),),
                                dbc.Col(
                                        dcc.Dropdown(
                                            id='dropdown-update-dept_directions-2',
                                            value='both',
                                            clearable=False,
                                            options=[
                                                {'label': name.capitalize(), 'value': name}
                                                for name in ['source', 'target', 'both', 'inner']
                                            ], className = "m-4",
                                            ),),
                            ], className = "g-0 justify-content-center",
                        ),
                html.P(id='cytoscape-tapEdgeData-output'),


                    
                ], width = {'size': 2}, className="border bl border-top-0 border-bottom-0"),
                dbc.Col(
                    [
                        html.H4("GASTech Email Network", className = "text-center bg-danger text-white p-0 m-0"),

                        dbc.Row(
                            [
                                dbc.Col(
                                    [ html.H5("Network 1", className = "text-center bg-danger text-white p-0 m-0"),

                                        html.Div([
                                    cyto.Cytoscape(
                                    id='cytoscape-update-layout',
                                    layout={'name': 'grid'},
                                    style={'width': '100%', 'height': '400px'},
                                    elements=elements
                                    #deze hier onder uit commenten als we niet met kleurtjes willen
                                    ,stylesheet=[
                                                {'selector': 'node','style': {'content': 'data(label)'}},
                                                {'selector': '.black','style': {'background-color': 'black','line-color': 'black'}},
                                                {'selector': '.red','style': {'background-color': 'red','line-color': 'red'}},
                                                {'selector': '.blue','style': {'background-color': 'blue','line-color': 'blue'}},
                                                {'selector': '.orange','style': {'background-color': 'orange','line-color': 'orange'}},
                                                {'selector': '.purple','style': {'background-color': 'purple','line-color': 'purple'}},
                                                {'selector': '.green','style': {'background-color': 'green','line-color': 'green'}}
                                            ]
                                    #^^ tot en met hier
                                 )]),
                                    ], 
                                ),
                                dbc.Col(
                                    [html.H5("Network 2", className = "text-center bg-danger text-white p-0 m-0"),

                                        html.Div([
                                    cyto.Cytoscape(
                                    id='cytoscape-update-layout-2',
                                    layout={'name': 'grid'},
                                    style={'width': '100%', 'height': '400px'},
                                    elements=elements
                                    #deze hier onder uit commenten als we niet met kleurtjes willen
                                    ,stylesheet=[
                                                {'selector': 'node','style': {'content': 'data(label)'}},
                                                {'selector': '.black','style': {'background-color': 'black','line-color': 'black'}},
                                                {'selector': '.red','style': {'background-color': 'red','line-color': 'red'}},
                                                {'selector': '.blue','style': {'background-color': 'blue','line-color': 'blue'}},
                                                {'selector': '.orange','style': {'background-color': 'orange','line-color': 'orange'}},
                                                {'selector': '.purple','style': {'background-color': 'purple','line-color': 'purple'}},
                                                {'selector': '.green','style': {'background-color': 'green','line-color': 'green'}}
                                            ]
                                    #^^ tot en met hier
                                 )]),
                                    ], 
                                ),
                            ], className = "g-0  justify-content-center",
                        ),

                        dbc.Row(
                            [
                                dbc.Col(
                                    [html.Div(id='cytoscape-tapNodeData-output', className = "h-75"),
                                    ], 
                                ),
                                dbc.Col(
                                    [html.Div(id='cytoscape-tapNodeData-output-2', className = "h-75"),
                                    ], 
                                ),
                            ], className = "g-0  justify-content-center",
                        ),
                        
                    # html.Div(id='cytoscape-tapNodeData-output', className = "h-75"),
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
                                        dcc.Graph(figure=lineplot(), className = "h-75"),
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

@app.callback(Output('cytoscape-update-layout-2', 'layout'),
              Input('dropdown-update-layout-2', 'value'))
def update_layout(layout):
    return {
        'name': layout,
        'animate': True
    }

@app.callback(Output('cytoscape-update-layout', 'elements'),
              Input('dropdown-start-day', 'value'),
              Input('dropdown-start-hour', 'value'),
              Input('dropdown-end-day', 'value'),
              Input('dropdown-end-hour', 'value'),
              Input('dropdown-update-departments', 'value'),
              Input('dropdown-update-dept_directions', 'value')
              )
def update_layout(sday,shour,eday,ehour, depts, direction):
    start_day  = get_day(sday)
    start_hour = shour[:2]
    end_day    = get_day(eday)
    end_hour   = ehour[:2]

    if depts == 'GAStech':
        return prepare_data(start_day, start_hour, end_day, end_hour)
    else:
        return prepare_data_department(start_day, start_hour, end_day, end_hour, depts, direction)

@app.callback(Output('cytoscape-update-layout-2', 'elements'),
              Input('dropdown-start-day-2', 'value'),
              Input('dropdown-start-hour-2', 'value'),
              Input('dropdown-end-day-2', 'value'),
              Input('dropdown-end-hour-2', 'value'),
              Input('dropdown-update-departments-2', 'value'),
              Input('dropdown-update-dept_directions-2', 'value')
              )
def update_layout(sday,shour,eday,ehour, depts, direction):
    start_day  = get_day(sday)
    start_hour = shour[:2]
    end_day    = get_day(eday)
    end_hour   = ehour[:2]

    if depts == 'GAStech':
        return prepare_data(start_day, start_hour, end_day, end_hour)
    else:
        return prepare_data_department(start_day, start_hour, end_day, end_hour, depts, direction)

@app.callback(Output('cytoscape-tapNodeData-output', 'children'),
              Input('dropdown-start-day', 'value'),
              Input('dropdown-start-hour', 'value'),
              Input('dropdown-end-day', 'value'),
              Input('dropdown-end-hour', 'value'),
              Input('dropdown-update-departments', 'value'),
              Input('dropdown-update-dept_directions', 'value'),
              Input('cytoscape-update-layout', 'tapNodeData'))
def update_layout(sday,shour,eday,ehour, depts, direction, data):
    start_day  = get_day(sday)
    start_hour = shour[:2]
    end_day    = get_day(eday)
    end_hour   = ehour[:2]

    if data:
        name = data['label']
        if depts == 'GAStech':
            return create_histogram(start_day, start_hour, end_day, end_hour, name)
        else:
            return create_histogram_department(start_day, start_hour, end_day, end_hour, depts, direction, name)

@app.callback(Output('cytoscape-tapNodeData-output-2', 'children'),
              Input('dropdown-start-day-2', 'value'),
              Input('dropdown-start-hour-2', 'value'),
              Input('dropdown-end-day-2', 'value'),
              Input('dropdown-end-hour-2', 'value'),
              Input('dropdown-update-departments-2', 'value'),
              Input('dropdown-update-dept_directions-2', 'value'),
              Input('cytoscape-update-layout-2', 'tapNodeData'))
def update_layout(sday,shour,eday,ehour, depts, direction, data):
    start_day  = get_day(sday)
    start_hour = shour[:2]
    end_day    = get_day(eday)
    end_hour   = ehour[:2]

    if data:
        name = data['label']
        if depts == 'GAStech':
            return create_histogram(start_day, start_hour, end_day, end_hour, name)
        else:
            return create_histogram_department(start_day, start_hour, end_day, end_hour, depts, direction, name)
        

@app.callback(Output('cytoscape-tapEdgeData-output','children' ),
            Input('cytoscape-update-layout', 'tapEdgeData'),
            Input('dropdown-start-day', 'value'),
            Input('dropdown-start-hour', 'value'),
            Input('dropdown-end-day', 'value'),
            Input('dropdown-end-hour', 'value'))
            
def update_layout2(data, sday,shour,eday,ehour):
    start_day  = get_day(sday)
    start_hour = shour[:2]
    end_day    = get_day(eday)
    end_hour   = ehour[:2]


    if data:
        return get_subjects(start_day, start_hour, end_day, end_hour, data['source'], data['target'])


# @app.callback(Output('cytoscape-tapEdgeData-output','children' ),
#             Input('cytoscape-update-layout', 'tapEdgeData'),
#             Input('dropdown-start-day', 'value'),
#             Input('dropdown-start-hour', 'value'),
#             Input('dropdown-end-day', 'value'),
#             Input('dropdown-end-hour', 'value'),
#             Input('submit-button', 'n_clicks'),
#             State('username', 'value'))
            
# def update_layout2(data, sday,shour,eday,ehour):
#     start_day  = get_day(sday)
#     start_hour = shour[:2]
#     end_day    = get_day(eday)
#     end_hour   = ehour[:2]


#     if data:
#         return get_subjects(start_day, start_hour, end_day, end_hour, data['source'], data['target'])




if __name__ == "__main__":
    app.run_server(debug=True)