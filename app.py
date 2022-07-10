from typing import Dict
import dash
from dash import dcc
import dash_bootstrap_components as dbc
import numpy as np
from PIL import Image
import json

import os

# import glob, os
from dash import html
from matplotlib.pyplot import pie
from numpy import empty, unicode_
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
from views.sunburst import sunburst_departments, sunburst_executive
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State
from dash import Dash, dash_table
from views.tsne import *
from views.heap_isiavann import create_heap
import re
import ast
import plotly.graph_objects as go
#dictionary used in coloring the network visualizations on page 4.
dic = {'Mat Bramar': 'black', 'Anda Ribera': 'black', 'Rachel Pantanal': 'black', 'Linda Lagos': 'orange', 'Carla Forluniau': 'black', 'Cornelia Lais': 'black',
    'Marin Onda': 'red', 'Isande Borrasca': 'red', 'Axel Calzas': 'red', 'Kare Orilla': 'red', 'Elsa Orilla': 'red', 'Brand Tempestad': 'red', 'Lars Azada': 'red', 'Felix Balas': 'red',
    'Lidelse Dedos': 'red', 'Birgitta Frente': 'red', 'Adra Nubarron': 'red', 'Gustav Cazar': 'red', 'Vira Frente': 'red', 'Willem Vasco-Pais': 'green', 'Ingrid Barranco': 'green',
    'Ada Campo-Corrente': 'green', 'Orhan Strum': 'green', 'Bertrand Ovan': 'purple', 'Emile Arpa': 'purple', 'Varro Awelon': 'purple', 'Dante Coginian': 'purple', 'Albina Hafon': 'purple',
    'Benito Hawelon': 'purple', 'Claudio Hawelon': 'purple', 'Valeria Morlun': 'purple', 'Adan Morlun': 'purple', 'Cecilia Morluniau': 'purple', 'Irene Nant': 'purple', 'Linnea Bergen': 'blue',
    'Lucas Alcazar': 'blue', 'Isak Baza': 'blue', 'Nils Calixto': 'blue', 'Sven Flecha': 'blue', 'Kanon Herrero': 'orange', 'Varja Lagos': 'orange', 'Stenig Fusil': 'orange', 'Hennie Osvaldo': 'orange',
    'Isia Vann': 'orange', 'Edvard Vann': 'orange', 'Felix Resumir': 'orange', 'Loreto Bodrogi': 'orange', 'Hideki Cocinaro': 'orange', 'Inga Ferro': 'orange', 'Ruscella Mies': 'black',
    'Sten Sanjorge Jr': 'green', 'Sten Sanjorge Jr (tethys)': 'black', 'Henk Mies': 'purple', 'Dylan Scozzese': 'purple', 'Minke Mies': 'orange'}


# #create default article to print
article1 = [open("data/articles/{}".format("0.txt")).read()]

#create the sunburst used in multiple pages of the DASH.
sunburst_executive_start = sunburst_executive('', True)
sunburst_departments_start = sunburst_departments('', True)

#load isia vann network data for page 2
df_isia_vann = pd.read_csv("data/networks_isiavann.csv").drop("Unnamed: 0", axis=1).set_index('time')
list_times = df_isia_vann.index
elements0 = create_heap(df_isia_vann, list_times[0])

def sorted_alphanumeric(path):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(path, key=alphanum_key)

path_articles = 'data/articles/'
path_resumes = 'data/resumes/txt versions/'
path_docs = 'data/HistoricalDocuments/txt versions/'

articles = []
for i in sorted_alphanumeric(os.listdir(path_articles)):
    articles.append(open(path_articles + i).read())
documents2 = tok_prepro_docs(articles)

historicalDocs = {i :  tok_prepro_docs([open(path_docs + i, encoding='utf-8').read()]) for i in sorted_alphanumeric(os.listdir(path_docs))}
resumes = {i :  tok_prepro_docs([open(path_resumes + i).read()]) for i in sorted_alphanumeric(os.listdir(path_resumes))}

#load names used for checking whether appearing in a document
dfnames = pd.read_excel('data/EmployeeRecords.xlsx')
names = []
for name in dfnames.LastName:
    names.append(name.lower())

#load tsne plots
df_tsne  = function_tsne([path_articles, path_resumes, path_docs], 'Cosine distance')
df, fig_tsne = plot_tsne(df_tsne, [path_articles, path_resumes, path_docs])

#load default wc
wc = px.imshow(np.array(Image.open(f"wordclouds/default_wc.png")))
wc.update_layout(coloraxis_showscale=False)
wc.update_xaxes(showticklabels=False)
wc.update_yaxes(showticklabels=False)


styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

#create the layout used throughout the entire DASH, including multiple pages.
app.layout = html.Div(
    children = [
        dbc.Row([
                dbc.Col(
                    [
                        dbc.Row(dbc.Col(html.H2("Disappearance at GAStech", className="m-0 bg-dark text-white text-center")), className="g-0"),
                        dbc.Row(dbc.Col(id="page-contents", className="h-100 m-2"), className="g-0 customHeight4 mb-4"),
                        dbc.Row(dbc.Col(dbc.Pagination(id="pagination", className="justify-content-center m-0", max_value=2, previous_next=True)), className="g-0"),
                    ], width={"size": 5}, className = 'h-100 bg-light p-0',
                
                ),
                dbc.Col(
                    [
                        dbc.Row(dbc.Col(html.H2("Group 30", className="bg-dark text-white text-center")), className="g-0"),
                        dbc.Row(dbc.Col(id="side-div2", className="h-100 mt-0 m-2"), className="g-0 customHeight"),         
                    ], width={"size": 5}, className="h-100 bg-light p-0 border bl border-bottom-0 border-top-0"),
            ], className="vh-100 align-items-center justify-content-center",
        ),
    ],
)

#callback that facilitates the switches between pages.
@app.callback(
    [Output("page-contents", "children")],
    Output("side-div2", "children"),
    [Input("pagination", "active_page")],
)



def switch_page(page):
    if page == 2:
                return [
        dbc.Col(
            [   
            #add node/edge visualization of netwerk 1
            dbc.Row([
                    html.H5(id='title-plot-1', className="bg-dark text-white text-center"),
                    cyto.Cytoscape(
                    id='cytoscape-update-layout-heat',
                    layout={'name': 'circle'},
                    style={'width': '100%', 'height': '600px'},
                    elements=elements0
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
                html.H5(id='cytoscape-mouseoverEdgeData-output-1', className="bg-dark text-white text-center"),

                dcc.Slider(0, len(list_times), 1,
                            value=0,
                            id='my-slider',
                            marks=None,
                            ),
            ], ),]),
            ], [
        dbc.Row(
                dbc.Col(
                    dcc.Graph(id='sunburst_network_page3',figure=sunburst_departments_start, className = "h-100")), className="customHeight3 g-0"), 
        dbc.Row(
                dbc.Col(
                    dcc.Graph(id='sunburst_exc_page3', figure=sunburst_executive_start, className = "h-100")), className="customHeight3 g-0"),  
                    
            ],
    return [html.H5('Select a group of articles with the Lasso Select function to generate wordclouds'),
            dcc.Graph(id='tsne-fig',figure=fig_tsne, className = "customHeight8"),
            dbc.Row(dcc.Graph(id='wc-figs',figure=wc, className = "h-100"), className="customHeight16")
            ], [html.H5('Choose which kind of data you want to include in the TSNE and the similarity distance'),   
            dbc.Row([
                dbc.Col([
                 dbc.Row(dcc.Dropdown(id = 'input_plot', options=[
                                    {'label': 'Articles', 'value': path_articles},
                                    {'label': 'Resumes', 'value': path_resumes},
                                    {'label': 'Historical Documents', 'value': path_docs},
                                ],
                                value= [path_articles, path_resumes, path_docs],
                                multi=True))], width={'size': 8}),
                dbc.Col([
                    dcc.Dropdown(['Cosine distance','Euclidean distance'], 'Cosine distance', id='demo-dropdown'),
                ], width={'size': 4}),
            ]),
            html.H5('Type a word below to get the concordance.'),
            dcc.Input(
                id="word", placeholder="word"
            ),
            dbc.Row( 
                dbc.Container([
                    html.Ul(id='id1',   ),
                    ],style={"display": "flex", "overflow":"hidden", "overflow-y":"scroll"}, className="h-100 border",
                    ), className = "customHeight9 g-0")]
            

@app.callback(
    Output("tsne-fig", "figure"),
    Input('demo-dropdown', 'value'),
    Input('input_plot', 'value'))
def figupdate(value, lst):
    if lst:
        df_tsne  = function_tsne(lst, value)
        df, fig_tsne = plot_tsne(df_tsne, lst)
        return fig_tsne
    else:
        return {}

@app.callback(
    Output("wc-figs", "figure"),
    Input('tsne-fig', 'selectedData'))
def display_selected_data(selectedData):
    d = selectedData
    if d:
        art_nums = []
        for row in d['points']:
            art_nums.append(row['customdata'][0])

        file_name = "wordclouds/wc_{}.png".format(art_nums[0])
        input_docs = []
        

        #add the files to the input_docs file which will be used for making the wordclouds
        for art in art_nums:
            if art == "5 year report clean.txt" or art == "10 year historical document clean.txt":
                for word in historicalDocs[art][0]:
                    input_docs.append(word)
            elif art[:7] == 'article':
                docie = documents2[int(art.split(' ')[1])]
                for word in docie:
                    input_docs.append(word)
            else:
                for word in resumes[art][0]:
                    input_docs.append(word)
        create_wordcloud(input_docs, names, file_name)

        with Image.open(file_name) as im:
            wcfig = px.imshow(np.array(im))
            wcfig.update_layout(margin=dict(l=0, r=0, b=0, t=0, pad=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',)
            wcfig.update_layout(coloraxis_showscale=False)
            wcfig.update_xaxes(showticklabels=False)
            wcfig.update_yaxes(showticklabels=False)
        return wcfig
    else:
        return {}


#update both networks by new data obtained from heatmap
@app.callback(Output('title-plot-1', 'children'),
              Output('cytoscape-update-layout-heat', 'elements'),
              Input('my-slider', 'value')
              )
def update_table(value):
    return str(list_times[value]), create_heap(df_isia_vann, list_times[value])

#print subjects of mails after clicked on edge of network 1
@app.callback(Output('cytoscape-mouseoverEdgeData-output-1', 'children'),
              Input('cytoscape-update-layout-heat', 'tapEdgeData'),
              Input('title-plot-1', 'children'))
def displayTapEdgeData(data, date):
    if data: 
        return(str(df_isia_vann.loc[date].subject))



#update left sunburst corresponding to nodes of left network
@app.callback(Output('sunburst_network_page3', 'figure'),
             Output('sunburst_exc_page3', 'figure'),
              Input('cytoscape-update-layout-heat', 'tapNodeData'))
def update_call(data):
    executives = {'Sten Sanjorge Jr': 'Sangorge JR. (CEO)', 'Sten Sanjorge Jr (tethys)': 'Sangorge JR. (CEO)', 'Willem Vasco-Pais': 'Vasco-Pais (ESA)', 'Ingrid Barranco': 'Barranco (CFO)',
                  'Ada Campo-Corrente': 'Campo-Corrente (CIO)', 'Orhan Strum': 'Strum (COO)', 'Mat Bramar': 'Bramar', 'Anda Ribera': 'Ribera','Linda Lagos': 'L.Lagos', 'Rachel Pantanal':'Pantanal'}
    if data:
        if data['label'] in executives.keys():
            return(sunburst_departments_start, sunburst_executive(data['label'], False))
        else:
            return(sunburst_departments(data['label'], False), sunburst_executive_start)
    else:
        return (sunburst_departments('', True),  sunburst_executive('', True))

#update right sunburst corresponding to nodes of right network
@app.callback(Output('sunburst_network_page3-2', 'figure'),
             Output('sunburst_exc_page3-2', 'figure'),
              Input('cytoscape-update-layout-heat-2', 'tapNodeData'))
def update_call(data):
    executives = {'Sten Sanjorge Jr': 'Sangorge JR. (CEO)', 'Sten Sanjorge Jr (tethys)': 'Sangorge JR. (CEO)', 'Willem Vasco-Pais': 'Vasco-Pais (ESA)', 'Ingrid Barranco': 'Barranco (CFO)',
                  'Ada Campo-Corrente': 'Campo-Corrente (CIO)', 'Orhan Strum': 'Strum (COO)', 'Mat Bramar': 'Bramar', 'Anda Ribera': 'Ribera','Linda Lagos': 'L.Lagos'}
    if data:
        if data['label'] in executives.keys():
            return(sunburst_departments_start, sunburst_executive(data['label'], False))
        else:
            return(sunburst_departments(data['label'], False), sunburst_executive_start)
    else:
        return (sunburst_departments('', True),  sunburst_executive('', True))


@app.callback(Output('id1', 'children'),
            Input('word', 'value'))
def context(word):
    if word:
        return [html.Li(x) for x in print_text_of_words(str(word))]
if __name__ == "__main__":
    app.run_server(debug=True)