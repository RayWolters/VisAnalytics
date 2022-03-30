import dash
import pandas as pd
import dash_cytoscape as cyto
from dash import html
from dash import dcc
from pprint import pprint
from dash.dependencies import Input, Output

import json

import dash_cytoscape as cyto
# import dash_reusable_components as drc


app = dash.Dash(__name__)

filepath_main = 'C:/Users/20183046/Documents/MASTER DS&AI/YEAR_1/Q3/2AMV10/Github/VisAnalytics/remove-later/email network/Data/data_2014-01-06.csv'
df = pd.read_csv(filepath_main)
df = df.rename(columns={'source': 'Source', 'target': 'Target', 'weight': 'Weight'})

l = df.values.tolist()
lst =[]
all_names = []
for row in l:
    all_names.append(row[0])
    all_names.append(row[1])
    lst.append((row[0], row[1]))
edges_tuples = tuple(lst)

lall_names = list(set(all_names))

l2 = []
for row in lall_names:
    l2.append((row, row))
nodes_tuple = tuple(l2)



nodes = [
    {
        'data': {'id': short, 'label': label}
        # 'position': {'x': 20*lat, 'y': -20*long}
    }
    for short, label in nodes_tuple
]

edges = [
    {'data': {'source': source, 'target': target}}
    for source, target in edges_tuples
]

elements = nodes + edges

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown-update-layout',
        value='grid',
        clearable=False,
        options=[
            {'label': name.capitalize(), 'value': name}
            for name in ['grid', 'random', 'circle', 'cose', 'concentric']
        ]
    ),
    cyto.Cytoscape(
        id='cytoscape-update-layout',
        layout={'name': 'grid'},
        style={'width': '100%', 'height': '450px'},
        elements=elements
    )
])


@app.callback(Output('cytoscape-update-layout', 'layout'),
              Input('dropdown-update-layout', 'value'))
def update_layout(layout):
    return {
        'name': layout,
        'animate': True
    }


if __name__ == '__main__':
    app.run_server(debug=True)

# default_stylesheet = [
#     {
#         "selector": 'node',
#         'style': {
#             "opacity": 0.65,
#         }
#     },
#     {
#         "selector": 'edge',
#         'style': {
#             "curve-style": "bezier",
#             "opacity": 0.65
#         }
#     },
# ]

# styles = {
#     'json-output': {
#         'overflow-y': 'scroll',
#         'height': 'calc(50% - 25px)',
#         'border': 'thin lightgrey solid'
#     },
#     'tab': {
#         'height': 'calc(98vh - 105px)'
#     }
# }

# app.layout = html.Div([
#     html.Div(className='eight columns', children=[
#         cyto.Cytoscape(
#             id='cytoscape',
#             elements=elements,
#             style={
#                 'height': '95vh',
#                 'width': '100%'
#             }
#         )
#     ]),

#     html.Div(className='four columns', children=[
#         dcc.Tabs(id='tabs', children=[
#             dcc.Tab(label='Control Panel', children=[
#                 drc.NamedDropdown(
#                     name='Layout',
#                     id='dropdown-layout',
#                     options=drc.DropdownOptionsList(
#                         'random',
#                         'grid',
#                         'circle',
#                         'concentric',
#                         'breadthfirst',
#                         'cose'
#                     ),
#                     value='grid',
#                     clearable=False
#                 ),

#                 drc.NamedDropdown(
#                     name='Node Shape',
#                     id='dropdown-node-shape',
#                     value='ellipse',
#                     clearable=False,
#                     options=drc.DropdownOptionsList(
#                         'ellipse',
#                         'triangle',
#                         'rectangle',
#                         'diamond',
#                         'pentagon',
#                         'hexagon',
#                         'heptagon',
#                         'octagon',
#                         'star',
#                         'polygon',
#                     )
#                 ),

#                 drc.NamedInput(
#                     name='Followers Color',
#                     id='input-follower-color',
#                     type='text',
#                     value='#0074D9',
#                 ),

#                 drc.NamedInput(
#                     name='Following Color',
#                     id='input-following-color',
#                     type='text',
#                     value='#FF4136',
#                 ),
#             ]),

#             dcc.Tab(label='JSON', children=[
#                 html.Div(style=styles['tab'], children=[
#                     html.P('Node Object JSON:'),
#                     html.Pre(
#                         id='tap-node-json-output',
#                         style=styles['json-output']
#                     ),
#                     html.P('Edge Object JSON:'),
#                     html.Pre(
#                         id='tap-edge-json-output',
#                         style=styles['json-output']
#                     )
#                 ])
#             ])
#         ]),
#     ])
# ])


# @app.callback(Output('tap-node-json-output', 'children'),
#               [Input('cytoscape', 'tapNode')])
# def display_tap_node(data):
#     return json.dumps(data, indent=2)


# @app.callback(Output('tap-edge-json-output', 'children'),
#               [Input('cytoscape', 'tapEdge')])
# def display_tap_edge(data):
#     return json.dumps(data, indent=2)


# @app.callback(Output('cytoscape', 'layout'),
#               [Input('dropdown-layout', 'value')])
# def update_cytoscape_layout(layout):
#     return {'name': layout}


# @app.callback(Output('cytoscape', 'stylesheet'),
#               [Input('cytoscape', 'tapNode'),
#                Input('input-follower-color', 'value'),
#                Input('input-following-color', 'value'),
#                Input('dropdown-node-shape', 'value')])
# def generate_stylesheet(node, follower_color, following_color, node_shape):
#     if not node:
#         return default_stylesheet

#     stylesheet = [{
#         "selector": 'node',
#         'style': {
#             'opacity': 0.3,
#             'shape': node_shape
#         }
#     }, {
#         'selector': 'edge',
#         'style': {
#             'opacity': 0.2,
#             "curve-style": "bezier",
#         }
#     }, {
#         "selector": 'node[id = "{}"]'.format(node['data']['id']),
#         "style": {
#             'background-color': '#B10DC9',
#             "border-color": "purple",
#             "border-width": 2,
#             "border-opacity": 1,
#             "opacity": 1,

#             "label": "data(label)",
#             "color": "#B10DC9",
#             "text-opacity": 1,
#             "font-size": 12,
#             'z-index': 9999
#         }
#     }]

#     for edge in node['edgesData']:
#         if edge['source'] == node['data']['id']:
#             stylesheet.append({
#                 "selector": 'node[id = "{}"]'.format(edge['target']),
#                 "style": {
#                     'background-color': following_color,
#                     'opacity': 0.9
#                 }
#             })
#             stylesheet.append({
#                 "selector": 'edge[id= "{}"]'.format(edge['id']),
#                 "style": {
#                     "mid-target-arrow-color": following_color,
#                     "mid-target-arrow-shape": "vee",
#                     "line-color": following_color,
#                     'opacity': 0.9,
#                     'z-index': 5000
#                 }
#             })

#         if edge['target'] == node['data']['id']:
#             stylesheet.append({
#                 "selector": 'node[id = "{}"]'.format(edge['source']),
#                 "style": {
#                     'background-color': follower_color,
#                     'opacity': 0.9,
#                     'z-index': 9999
#                 }
#             })
#             stylesheet.append({
#                 "selector": 'edge[id= "{}"]'.format(edge['id']),
#                 "style": {
#                     "mid-target-arrow-color": follower_color,
#                     "mid-target-arrow-shape": "vee",
#                     "line-color": follower_color,
#                     'opacity': 1,
#                     'z-index': 5000
#                 }
#             })

#     return stylesheet


# if __name__ == '__main__':
#     app.run_server(debug=True)