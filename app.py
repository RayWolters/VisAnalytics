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
import dash_cytoscape as cyto
from pprint import pprint
from dash.dependencies import Input, Output, State
import json
from histogram import create_histogram, create_histogram_department
from subjects import get_subjects
from lineplot import lineplot
from pok_table import search_on_names
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

elements = prepare_data('2014-01-06', "08", '2014-01-17', '22', 'Source')

df_table_full, df_table_last, df_table_middle, df_info_associated_employees = search_on_names()

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
        return [], [dcc.Graph(figure=lineplot(), className = "h-75"),]
    if page == 3:
        return [
        dbc.Row(
            [dbc.Col(
                [
                dbc.Row(
                    dbc.Col(
                        html.H5("Settings network 1", className="text-center bg-white border p-0 m-0"),
                    ), 
                    className="g-0",
                ),
                dbc.Row(
                    dbc.Col(
                        html.H6('Choose layout and type of POK member contribution in network:', className="text-center mt-2"),
                    ),
                    className="g-0",
                ),
                dbc.Row([
                    dbc.Col(
                        dcc.Dropdown(
                            id='dropdown-update-layout',
                            value='circle',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['grid', 'random', 'circle', 'cose', 'concentric']
                            ], className = ""), width={"size":5},
                        ),
                    dbc.Col(
                        dcc.Dropdown(
                            id='dropdown-update-employees',
                            value='Source',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['Source', 'Target', 'Both', 'Inner']
                            ], className = "",
                            ),width={"size":5},
                        ),

                    ], className="g-0",),

                dbc.Row(
                    dbc.Col(
                        html.H6('Choose Start and End date:', className="text-center mt-2"),
                    ),
                    className="g-0",
                ),
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
                            ], className = ""), width={"size":3}, className = "ml-1 mr-0",
                        ), 
                    dbc.Col(
                        dcc.Dropdown(
                            id='dropdown-start-hour',
                            value='08:00',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['08:00', '09:00', '10:00', '11:00', '12:00','13:00','14:00','15:00','16:00',
                                            '17:00','18:00','19:00', '20:00', '21:00', '22:00', '23:00']
                            ], className = ""), width={"size":3}, className = "m-0",
                        ), 
                    dbc.Col(
                        dcc.Dropdown(
                            id='dropdown-end-day',
                            value='Mon 6',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['Mon 6', 'Tue 7', 'Wed 8', 'Thu 9', 'Fri 10',
                                            'Mon 13', 'Tue 14', 'Wed 15', 'Thu 16', 'Fri 17']
                            ], className = ""), width={"size":3}, className = "m-0",
                        ),
                    dbc.Col(
                        dcc.Dropdown(
                            id='dropdown-end-hour',
                            value='23:00',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['08:00', '09:00', '10:00', '11:00', '12:00','13:00','14:00','15:00','16:00',
                                            '17:00','18:00','19:00', '20:00', '21:00', '22:00', '23:00']
                            ], className = ""), width={"size":3}, className = "ml-0 mr-1",
                        ),
                    ], className="g-0",
                    ), 
                dbc.Row(
                    dbc.Col(
                        [cyto.Cytoscape(
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
                                                {'selector': '.green','style': {'background-color': 'green','line-color': 'green'}},
                                                {'selector': '.orange_pok','style': {'background-color': 'orange','line-color': 'orange', 'shape': 'triangle'}},
                                                {'selector': '.black_pok','style': {'background-color': 'black','line-color': 'black', 'shape': 'triangle'}},
                                            ]
                                ),
                        dbc.Modal([
                            dbc.ModalHeader(dbc.ModalTitle("Header")),
                            dbc.ModalBody(html.Div(id='cytoscape-tapEdgeData-output', className = "h-75"),),
                            # dbc.ModalFooter(
                            #     dbc.Button(
                            #         "Close", id="close", className="ms-auto", n_clicks=0
                            #     )
                            # ),
                            ],
                            id="modal",
                            is_open=False,
                        ),
                        ],      
                    ),
                    className="g-0",
                ),
                dbc.Row([
                    dbc.Col(
                        [html.Div(id='cytoscape-tapNodeData-output', className = "h-75")], 
                        ),
                    dbc.Col(
                        [html.Div(id='cytoscape-tapNodeData-output-2', className = "h-75")], 
                    ),
                ], className = "g-0  justify-content-center",),
                ], width={"size":6}, className = "",
            ),
            dbc.Col([
                dbc.Row(
                    dbc.Col(
                        html.H5("Settings network 2", className="text-center bg-white border p-0 m-0"),
                    ), 
                    className="g-0",
                ),
                dbc.Row(
                    dbc.Col(
                        html.H6('Choose layout:', className="text-center mt-2"),
                    ),
                    className="g-0",
                ),
                dbc.Row([
                    dbc.Col(
                        dcc.Dropdown(
                            id='dropdown-update-layout-2',
                            value='circle',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['grid', 'random', 'circle', 'cose', 'concentric']
                            ], className = ""), width={"size":5},
                        ),  
                    dbc.Col(
                        dcc.Dropdown(
                            id='dropdown-update-employees-2',
                            value='Source',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['Source', 'Target', 'Both', 'Inner']
                            ], className = "",
                            ), width={"size":5},
                        ),
                ], className="g-0",),

                dbc.Row(
                    dbc.Col(
                        html.H6('Choose Start and End date:', className="text-center mt-2"),
                    ),
                    className="g-0",
                ),
                dbc.Row([
                    dbc.Col(
                        dcc.Dropdown(
                            id='dropdown-start-day-2',
                            value='Tue 7',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['Mon 6', 'Tue 7', 'Wed 8', 'Thu 9', 'Fri 10',
                                            'Mon 13', 'Tue 14', 'Wed 15', 'Thu 16', 'Fri 17']
                            ], className = ""), width={"size":3}, className = "ml-1 mr-0",
                    ),
                    dbc.Col(
                        dcc.Dropdown(
                            id='dropdown-start-hour-2',
                            value='08:00',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['08:00', '09:00', '10:00', '11:00', '12:00','13:00','14:00','15:00','16:00',
                                            '17:00','18:00','19:00', '20:00', '21:00', '22:00', '23:00']
                            ], className = ""), width={"size":3},
                    ),
                    dbc.Col(
                        dcc.Dropdown(
                            id='dropdown-end-day-2',
                            value='Tue 7',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['Mon 6', 'Tue 7', 'Wed 8', 'Thu 9', 'Fri 10',
                                            'Mon 13', 'Tue 14', 'Wed 15', 'Thu 16', 'Fri 17']
                            ], className = "",), width={"size":3},
                    ),
                    dbc.Col(
                        dcc.Dropdown(
                            id='dropdown-end-hour-2',
                            value='23:00',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['08:00', '09:00', '10:00', '11:00', '12:00','13:00','14:00','15:00','16:00',
                                            '17:00','18:00','19:00', '20:00', '21:00', '22:00', '23:00']
                            ], className = "",), width={"size":3},
                    ),
                ], className="g-0"),
                dbc.Row(
                    dbc.Col(
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
                                                {'selector': '.green','style': {'background-color': 'green','line-color': 'green'}},
                                                {'selector': '.orange_pok','style': {'background-color': 'orange','line-color': 'orange', 'shape': 'triangle'}},
                                                {'selector': '.black_pok','style': {'background-color': 'black','line-color': 'black', 'shape': 'triangle'}},
                                            ]
                            ), 
                        ),
                    ),
                dbc.Row([
                    dbc.Col(
                        [html.Div(id='cytoscape-tapNodeData-output-target', className = "h-75")], 
                    ),
                    dbc.Col(
                        [html.Div(id='cytoscape-tapNodeData-output-target-2', className = "h-75")], 
                    ),
                ], className = "g-0  justify-content-center",),
                    ], width={"size":6},
                ),
            ], className=""),  
        ], [
    dbc.Row(
            dbc.Col(
                dcc.Graph(figure=sunburst_executive(), className = "h-100")), className="customHeight3 g-0"), 
    dbc.Row(
            dbc.Col(
                dcc.Graph(figure=sunburst_departments(), className = "h-100")), className="customHeight3 g-0")]
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
                        html.H6('Lastnames of employees that appear in the historical records that contain POK, pok or Protectors.', className="border"),
                        dash_table.DataTable(
                            data=df_table_last.to_dict('records'),
                            columns=[{'id': c, 'name': c} for c in df_table_last.columns],
                            style_table={'overflowX': 'auto'},
                        ),
                        html.H6('Employee Records of employees whose last-, first-, or middlename appears in one of the historical records', className="border bg-white mt-2"),
                    ], width={'size': 6}),
                    dbc.Col([
                        html.H6('Some lastnames of employees consist of two words which is why we also check on these names of employees that appear in the historical \
                        records that contain POK, pok or Protectors. \
                        It appears that there is only one employee whose name is fully contained in one of the historical records.', className="border"),
                        dash_table.DataTable(
                            data=df_table_middle.to_dict('records'),
                            columns=[{'id': c, 'name': c} for c in df_table_middle.columns],
                            style_table={'overflowX': 'auto'},
                        ),
                        dash_table.DataTable(
                            data=df_table_full.to_dict('records'),
                            columns=[{'id': c, 'name': c} for c in df_table_full.columns],
                            style_table={'overflowX': 'auto'},
                        ), 
                    ], width={'size': 6}),
                ]),
                dbc.Row([ 
                    dbc.Col([
                        
                        
                    ], width={"size": 6}),
                ], className=""),
                dbc.Row([
                    dbc.Col([
                        dash_table.DataTable(
                            data=df_info_associated_employees.to_dict('records'),
                            columns=[{'id': c, 'name': c} for c in df_info_associated_employees.columns],
                            style_table={'overflowX': 'auto'},
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
                dcc.Graph(figure=sunburst_departments(), className = "h-100")), className="customHeight3 g-0")]

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
              Input('dropdown-update-employees', 'value'),
              )

def update_layout(sday,shour,eday,ehour, way):
    start_day  = get_day(sday)
    start_hour = shour[:2]
    end_day    = get_day(eday)
    end_hour   = ehour[:2]
    
    return prepare_data(start_day, start_hour, end_day, end_hour, way)


@app.callback(Output('cytoscape-update-layout-2', 'elements'),
              Input('dropdown-start-day-2', 'value'),
              Input('dropdown-start-hour-2', 'value'),
              Input('dropdown-end-day-2', 'value'),
              Input('dropdown-end-hour-2', 'value'),
              Input('dropdown-update-employees-2', 'value'),
              )

def update_layout(sday,shour,eday,ehour, way):
    start_day  = get_day(sday)
    start_hour = shour[:2]
    end_day    = get_day(eday)
    end_hour   = ehour[:2]
    
    return prepare_data(start_day, start_hour, end_day, end_hour, way)



# @app.callback(Output('cytoscape-tapNodeData-output', 'children'),
#               Input('dropdown-start-day', 'value'),
#               Input('dropdown-start-hour', 'value'),
#               Input('dropdown-end-day', 'value'),
#               Input('dropdown-end-hour', 'value'),
#               Input('dropdown-update-departments', 'value'),
#               Input('dropdown-update-dept_directions', 'value'),
#               Input('cytoscape-update-layout', 'tapNodeData'))
# def update_layout(sday,shour,eday,ehour, depts, direction, data):
#     start_day  = get_day(sday)
#     start_hour = shour[:2]
#     end_day    = get_day(eday)
#     end_hour   = ehour[:2]

    

#     if data:
#         name = data['label']
#         if depts == 'GAStech':
#             return create_histogram(start_day, start_hour, end_day, end_hour, name, 'source')
#         else:
#             return create_histogram_department(start_day, start_hour, end_day, end_hour, depts, direction, name, 'source')

# @app.callback(Output('cytoscape-tapNodeData-output-2', 'children'),
#               Input('dropdown-start-day-2', 'value'),
#               Input('dropdown-start-hour-2', 'value'),
#               Input('dropdown-end-day-2', 'value'),
#               Input('dropdown-end-hour-2', 'value'),
#               Input('dropdown-update-departments-2', 'value'),
#               Input('dropdown-update-dept_directions-2', 'value'),
#               Input('cytoscape-update-layout-2', 'tapNodeData'))
# def update_layout(sday,shour,eday,ehour, depts, direction, data):
#     start_day  = get_day(sday)
#     start_hour = shour[:2]
#     end_day    = get_day(eday)
#     end_hour   = ehour[:2]

#     if data:
#         name = data['label']
#         if depts == 'GAStech':
#             return create_histogram(start_day, start_hour, end_day, end_hour, name, 'source')
#         else:
#             return create_histogram_department(start_day, start_hour, end_day, end_hour, depts, direction, name, 'source')


# @app.callback(Output('cytoscape-tapNodeData-output-target', 'children'),
#               Input('dropdown-start-day', 'value'),
#               Input('dropdown-start-hour', 'value'),
#               Input('dropdown-end-day', 'value'),
#               Input('dropdown-end-hour', 'value'),
#               Input('dropdown-update-departments', 'value'),
#               Input('dropdown-update-dept_directions', 'value'),
#               Input('cytoscape-update-layout', 'tapNodeData'))
# def update_layout(sday,shour,eday,ehour, depts, direction, data):
#     start_day  = get_day(sday)
#     start_hour = shour[:2]
#     end_day    = get_day(eday)
#     end_hour   = ehour[:2]

#     if data:
#         name = data['label']
#         if depts == 'GAStech':
#             return create_histogram(start_day, start_hour, end_day, end_hour, name, 'target')
#         else:
#             return create_histogram_department(start_day, start_hour, end_day, end_hour, depts, direction, name, 'target')

# @app.callback(Output('cytoscape-tapNodeData-output-target-2', 'children'),
#               Input('dropdown-start-day-2', 'value'),
#               Input('dropdown-start-hour-2', 'value'),
#               Input('dropdown-end-day-2', 'value'),
#               Input('dropdown-end-hour-2', 'value'),
#               Input('dropdown-update-departments-2', 'value'),
#               Input('dropdown-update-dept_directions-2', 'value'),
#               Input('cytoscape-update-layout-2', 'tapNodeData'))
# def update_layout(sday,shour,eday,ehour, depts, direction, data):
#     start_day  = get_day(sday)
#     start_hour = shour[:2]
#     end_day    = get_day(eday)
#     end_hour   = ehour[:2]

#     if data:
#         name = data['label']
#         if depts == 'GAStech':
#             return create_histogram(start_day, start_hour, end_day, end_hour, name, 'target')
#         else:
#             return create_histogram_department(start_day, start_hour, end_day, end_hour, depts, direction, name, 'target')
        

# @app.callback(Output('cytoscape-tapEdgeData-output','children' ),
#             Input('cytoscape-update-layout', 'tapEdgeData'),
#             Input('dropdown-start-day', 'value'),
#             Input('dropdown-start-hour', 'value'),
#             Input('dropdown-end-day', 'value'),
#             Input('dropdown-end-hour', 'value'))
            
# def update_layout2(data, sday,shour,eday,ehour):
#     start_day  = get_day(sday)
#     start_hour = shour[:2]
#     end_day    = get_day(eday)
#     end_hour   = ehour[:2]


#     if data:
#         return get_subjects(start_day, start_hour, end_day, end_hour, data['source'], data['target'])

# @app.callback(
#     Output("modal", "is_open"),
#     Output('cytoscape-tapEdgeData-output', 'children'),
#     Input('dropdown-start-day', 'value'),
#     Input('dropdown-start-hour', 'value'),
#     Input('dropdown-end-day', 'value'),
#     Input('dropdown-end-hour', 'value'),
#     Input('cytoscape-update-layout', 'tapEdgeData'),
#     [State("modal", "is_open")],)

# def update_layout(sday,shour,eday,ehour, data, is_open):
#     start_day  = get_day(sday)
#     start_hour = shour[:2]
#     end_day    = get_day(eday)
#     end_hour   = ehour[:2]

#     if data:
#         return(not is_open, get_subjects(start_day, start_hour, end_day, end_hour, data['source'], data['target']))
#     else:
#         return (is_open, '')
    


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