import dash
from dash import dcc
import dash_bootstrap_components as dbc
import numpy as np
from PIL import Image

# import glob, os
from dash import html
from matplotlib.pyplot import pie
from numpy import unicode_
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
from views.sunburst import sunburst_departments, sunburst_executive
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State
from views.network_heap import prepare_data_heap
from views.subjects import get_subjects_heap
from views.pok_table import search_on_names
from views.communities import communities_plot
from views.heatmap_creater import create_heap
from dash import Dash, dash_table
from views.page1 import create_visualizations_page1, print_text_of_words
from views.page2_pca import create_pca, plot_pca_kmeans

#dictionary used in coloring the network visualizations on page 4.
dic = {'Mat Bramar': 'black', 'Anda Ribera': 'black', 'Rachel Pantanal': 'black', 'Linda Lagos': 'orange', 'Carla Forluniau': 'black', 'Cornelia Lais': 'black',
    'Marin Onda': 'red', 'Isande Borrasca': 'red', 'Axel Calzas': 'red', 'Kare Orilla': 'red', 'Elsa Orilla': 'red', 'Brand Tempestad': 'red', 'Lars Azada': 'red', 'Felix Balas': 'red',
    'Lidelse Dedos': 'red', 'Birgitta Frente': 'red', 'Adra Nubarron': 'red', 'Gustav Cazar': 'red', 'Vira Frente': 'red', 'Willem Vasco-Pais': 'green', 'Ingrid Barranco': 'green',
    'Ada Campo-Corrente': 'green', 'Orhan Strum': 'green', 'Bertrand Ovan': 'purple', 'Emile Arpa': 'purple', 'Varro Awelon': 'purple', 'Dante Coginian': 'purple', 'Albina Hafon': 'purple',
    'Benito Hawelon': 'purple', 'Claudio Hawelon': 'purple', 'Valeria Morlun': 'purple', 'Adan Morlun': 'purple', 'Cecilia Morluniau': 'purple', 'Irene Nant': 'purple', 'Linnea Bergen': 'blue',
    'Lucas Alcazar': 'blue', 'Isak Baza': 'blue', 'Nils Calixto': 'blue', 'Sven Flecha': 'blue', 'Kanon Herrero': 'orange', 'Varja Lagos': 'orange', 'Stenig Fusil': 'orange', 'Hennie Osvaldo': 'orange',
    'Isia Vann': 'orange', 'Edvard Vann': 'orange', 'Felix Resumir': 'orange', 'Loreto Bodrogi': 'orange', 'Hideki Cocinaro': 'orange', 'Inga Ferro': 'orange', 'Ruscella Mies': 'black',
    'Sten Sanjorge Jr': 'green', 'Sten Sanjorge Jr (tethys)': 'black', 'Henk Mies': 'purple', 'Dylan Scozzese': 'purple', 'Minke Mies': 'orange'}

#describe goals epr page:
goal_page1 = "The goal of this page is to obtain insights into the sentiment analysis of the articles. "
goal_page2 = "The goal of this page consists of finding articles that are similar based on a PCA analysis."
goal_page5 = "The goal of this page consists of obtaining insights into possible subgroups within the email communication network. The columns of the table consist of the found subgroups, with the dropdown menu you can change color details."

#create teh visualizations used in page 1
pie_all = create_visualizations_page1('pie', 'All articles')
bar_all = create_visualizations_page1('bar', 'All articles')
my_list = print_text_of_words('criminals')

wc_all = px.imshow(np.array(Image.open(f"data/wordclouds/all.png")))
wc_all.update_layout(coloraxis_showscale=False)
wc_all.update_xaxes(showticklabels=False)
wc_all.update_yaxes(showticklabels=False)

wc_pok = px.imshow(np.array(Image.open(f"data/wordclouds/pok.png")))
wc_pok.update_layout(coloraxis_showscale=False)
wc_pok.update_xaxes(showticklabels=False)
wc_pok.update_yaxes(showticklabels=False)

#create default article to print
article1 = [open("data/articles/{}".format("0.txt")).read()]

#create the sunburst used in multiple pages of the DASH.
sunburst_executive_start = sunburst_executive('', True)
sunburst_departments_start = sunburst_departments('', True)

#set default network elements 
elements1 = prepare_data_heap("2014-01-06 09:00", 60, True)
elements2 = prepare_data_heap("2014-01-06 10:00", 60, True)

#create default heatmap used in page 4 of DASH.
heatm = create_heap(60, 10)

#create dataframes used as input for tables within the DASH.
df_info_associated_employees = search_on_names()
df_communities, communities_plot_style = communities_plot('Department')

#create legends corresponding to one of the tables.
legend_millitary = pd.DataFrame(['ArmedForcesOf-Kronos','TethanDefense-ForceArmy','TethanDefense-ForceAir','TethanDefense-ForceNavy'], columns=['Military class'])
legend_department = pd.DataFrame(['Board', 'Facilities','Engineering','IT','Security'], columns=['Departments'])
legend_pok = pd.DataFrame(['not involved with POK', 'involved with POK'], columns=['POK'])



#create default PCA plot.
path_articles = 'data/articles/'
path_resumes = 'data/resumes/txt versions/'
path_docs = 'data/HistoricalDocuments/txt versions/'

df_pca  = create_pca([path_articles, path_resumes, path_docs])
pca_fig = plot_pca_kmeans(8, df_pca, [path_articles, path_resumes, path_docs])


#create the layout used throughout the entire DASH, including multiple pages.
app.layout = html.Div(
    children = [
        dbc.Row(
            [    dbc.Col(
                    [   dbc.Row(dbc.Col(html.H2("VA", className="bg-dark text-white text-center")), className="g-0"),
                        dbc.Row(dbc.Col(id="side-div", className="h-100 m-2"), className="g-0 customHeight"),         
                    ], width={"size": 2}, className="h-75 bg-light p-0 border bl border-bottom-0 border-top-0"),
                dbc.Col(
                    [
                        dbc.Row(dbc.Col(html.H2("Disappearance at GAStech", className="m-0 bg-dark text-white text-center")), className="g-0"),
                        dbc.Row(dbc.Col(id="page-contents", className="h-100 m-2"), className="g-0 customHeight4 mb-4"),
                        dbc.Row(dbc.Col(dbc.Pagination(id="pagination", className="justify-content-center m-0", max_value=5, previous_next=True)), className="g-0"),
                    ], width={"size": 7}, className = 'h-75 bg-light p-0',
                
                ),
                dbc.Col(
                    [
                        dbc.Row(dbc.Col(html.H2("Group 30", className="bg-dark text-white text-center")), className="g-0"),
                        dbc.Row(dbc.Col(id="side-div2", className="h-100 mt-0 m-2"), className="g-0 customHeight"),         
                    ], width={"size": 2}, className="h-75 bg-light p-0 border bl border-bottom-0 border-top-0"),
            ], className="vh-100 align-items-center justify-content-center",
        ),
    ],
)

#callback that facilitates the switches between pages.
@app.callback(
    [Output("page-contents", "children"),
    Output("side-div", "children")],
    Output("side-div2", "children"),
    [Input("pagination", "active_page")],
)
def switch_page(page):
    if page == 2:#add pca plot
        return [dcc.Graph(id='pca-fig',figure=pca_fig, className = "h-100") ],[
                            html.H5(goal_page2, className="border bg-white mb-0"),
                            html.H5("Change the analysis:", className="bg-dark text-white text-center"),
                            html.H5('Choose a different K to obtain different K-means clusters:'),
                            dbc.Row(dcc.Dropdown(
                            id='choose-k',
                            value=8,
                            clearable=False,
                            options=[
                                {'label': name, 'value': name}
                                for name in [1,2,3,4,5,6,7,8,9,10]
                            ], className = "")),
                            html.H5('Choose which kind of data you want to include in the PCA'),
                            dbc.Row(dcc.Dropdown(id = 'input_plot', options=[
                                    {'label': 'Articles', 'value': path_articles},
                                    {'label': 'Resumes', 'value': path_resumes},
                                    {'label': 'Historical Documents', 'value': path_docs},
                                ],
                                value= [path_articles, path_resumes, path_docs],
                                multi=True)),
                            ],[
                # add a container where articles can be printed.
                dbc.Container([
                    html.Ul(children = [html.Li(x) for x in article1], id='print_article',),
                    ],style={"display": "flex", "overflow":"hidden", "overflow-x":"scroll","overflow-y":"scroll",}, className="h-100 border",
                    ),   
                            ]
    if page == 3:
        return [
            dbc.Row(
            [
                dbc.Row([
                    dbc.Col([
                        html.H5('The goal on this page is, given the historical records and articles* that contain the words POK, pok, or Protectors of Kronos, to find employees that are possibly associated with the POK or even are part of the POK.', className="border bg-white mb-0"),
                        html.H6('* No employee names (either fully, or partially) appear in the articles.', className=""),
                    ], width={"size": 11}),
                ], className="justify-content-center align-items-center customHeight6"),
                dbc.Row([
                    dbc.Col([
                        dbc.Label("The table below contains employee records of employees whose lastname or fullname appears in the historical records. The first column is manually added, as a pre-analysis, to show which employees are (possibly) associated with the POK by considering their full name or lastname."),
                        #add a table containing information about employees found in analysis
                        dash_table.DataTable(
                            id='dash-table',
                            data=df_info_associated_employees.to_dict('records'),
                            columns=[{'id': c, 'name': c} for c in df_info_associated_employees.columns],
                            style_table={'overflowX': 'auto'},
                            style_data_conditional=[
                                {'if': {'row_index':0,},'backgroundColor': 'grey','color': 'black'},
                                {'if': {'row_index':1,},'backgroundColor': 'green','color': 'white'},
                                {'if': {'row_index':2,},'backgroundColor': 'purple','color': 'white'},
                                {'if': {'row_index':3,},'backgroundColor': 'orange','color': 'black'},
                                {'if': {'row_index':4,},'backgroundColor': 'orange','color': 'black'},
                                {'if': {'row_index':5,},'backgroundColor': 'grey','color': 'black'},
                                {'if': {'row_index':6,},'backgroundColor': 'orange','color': 'black'},
                                {'if': {'row_index':7,},'backgroundColor': 'orange','color': 'black'}],
                        ),                      
                    ], width={"size": 10}),
                ], className="justify-content-center align-items-center customHeight7"),
            ], className="h-100",
        ),
        ], [
            #add sunburst plots
            dbc.Row(
                dbc.Col(
                    dcc.Graph(id='sunburst_network_page2',figure=sunburst_departments_start, className = "h-100")), className="customHeight3 g-0"), 
            dbc.Row(
                dbc.Col(
                    dcc.Graph(id='sunburst_exc_page2', figure=sunburst_executive_start, className = "h-100")), className="customHeight3 g-0")
        ],[]

    if page==4:
        return [
        dbc.Row(
            [   
            #add node/edge visualization of netwerk 1
            dbc.Col([
                    html.H5(id='title-plot-1', className="bg-dark text-white text-center"),
                    cyto.Cytoscape(
                    id='cytoscape-update-layout-heat',
                    layout={'name': 'grid'},
                    style={'width': '100%', 'height': '230px'},
                    elements=elements1
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
                html.H5(id='cytoscape-mouseoverEdgeData-output-1')
            ], className="h-100"),
            #add node/edge visualization of netwerk 2
            dbc.Col([
                    html.H5(id='title-plot-2', className="bg-dark text-white text-center"),
                    cyto.Cytoscape(
                    id='cytoscape-update-layout-heat-2',
                    layout={'name': 'grid'},
                    style={'width': '100%', 'height': '230px'},
                    elements=elements2
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
                html.H5(id='cytoscape-mouseoverEdgeData-output-2')
            ], className="h-100"),], className="h-50"),
        dbc.Row(
            [
                dbc.Col(
                    [#add heatmap 
                    html.H5("Network similarity heatmap", className="bg-dark text-white text-center"),
                    dbc.Row(
                        dbc.Col([
                            dcc.Graph(id='heatmap', figure=heatm, className = "h-100"),
                        ]), className="h-100")
                    ], className="h-100",
                ),
                dbc.Col(
                    [
                     html.H5("Heatmap settings", className="bg-dark text-white text-center"),
                    #add a couple of dropdowns that give user opportunity to select/change their analysis
                    html.H5('Choose the communication interval on which you want to find similar networks between POK members', className="border bg-white mb-0"),
                    dbc.Row(dcc.Dropdown(
                            id='dropdown-interval',
                            value='1 hourly interval',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['2 hourly interval', '1 hourly interval', '30 minutes interval', '15 minutes interval']
                            ], className = "")),  
                    html.H5("Choose an upper bound on the number of total to's. E.g. to leave out all emails send to the whole company", className="border bg-white mb-0"),
                    dbc.Row(dcc.Dropdown(
                            id='treshold-interval',
                            value='30 employees',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['30 employees', '25 employees', '20 employees', '15 employees', '10 employees', '8 employees', '5 employees', '3 employees', '2 employees', '1 employee']
                            ], className = "")),
                    html.H5("Choose whether to include the whole network within the interval in plots or only POK member contributions", className="border bg-white mb-0"),
                    dbc.Row(dcc.Dropdown(
                            id='employee-participants',
                            value='only POK',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['all', 'only POK']
                            ], className = "")),
                    ], className="h-100"
                ),
            ], className="customHeight10",
        )], [#add sunbursts
        dbc.Row(
                dbc.Col(
                    dcc.Graph(id='sunburst_network_page3',figure=sunburst_departments_start, className = "h-100")), className="customHeight3 g-0"), 
        dbc.Row(
                dbc.Col(
                    dcc.Graph(id='sunburst_exc_page3', figure=sunburst_executive_start, className = "h-100")), className="customHeight3 g-0"),
        dbc.Row(dcc.Dropdown(
                    id='dropdown-update-layout-heat',
                    value='cose',
                    clearable=False,
                    options=[
                        {'label': name.capitalize(), 'value': name}
                        for name in ['grid', 'random', 'circle', 'cose',]
                    ], className = "mt-4")),     
            ],[#add sunbursts
        dbc.Row(
                dbc.Col(
                    dcc.Graph(id='sunburst_network_page3-2',figure=sunburst_departments_start, className = "h-100")), className="customHeight3 g-0"), 
        dbc.Row(
                dbc.Col(
                    dcc.Graph(id='sunburst_exc_page3-2', figure=sunburst_executive_start, className = "h-100")), className="customHeight3 g-0"),
        dbc.Row(dcc.Dropdown(
                            id='dropdown-update-layout-heat-2',
                            value='cose',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['grid', 'random', 'circle', 'cose']
                            ], className = "mt-4")),  ]
    if page == 5:
        return [
            html.H5(goal_page5, className="border bg-white mb-0"),
            dbc.Row(
            [
                dbc.Row(
                    dbc.Col([ #add a dropdown so user can obtain different insights.
                        dcc.Dropdown(
                            id='Departments',
                            value='Departments',
                            clearable=False,
                            options=[
                                {'label': name.capitalize(), 'value': name}
                                for name in ['Departments', 'POK', 'Military']
                            ], className = "")
                    ], width={"size": 6}), className="justify-content-center align-items-center",
                    ),
                dbc.Row([ #add table
                    dbc.Col([
                        dbc.Label(""),
                        dash_table.DataTable(
                            id='dash-table4',
                            data=df_communities.to_dict('records'),
                            style_table={'overflowY': 'auto'},
                            style_data_conditional=communities_plot_style
                        ),                        
                    ], width={"size": 10}),
                ], className="justify-content-center align-items-center customHeight7"),
            ], className="h-100",
        ),
        ], [
            dbc.Row(
                dbc.Col( #add sunbursts
                    dcc.Graph(id='sunburst_network_page4',figure=sunburst_departments_start, className = "h-100")), className="customHeight3 g-0"), 
            dbc.Row(
                dbc.Col(
                    dcc.Graph(id='sunburst_exc_page4', figure=sunburst_executive_start, className = "h-100")), className="customHeight3 g-0")
        ],[#add table containing the useful information.
                        dash_table.DataTable(
                            id='dash-table-legends',
                            data=legend_millitary.to_dict('records'),
                            columns=[{'id': c, 'name': c} for c in legend_millitary.columns],
                            style_table={'overflowX': 'auto'},
                            style_data_conditional=[
                                {'if': {'row_index':0,},'backgroundColor': 'blue','color': 'white'},
                                {'if': {'row_index':1,},'backgroundColor': 'red','color': 'white'},
                                {'if': {'row_index':2,},'backgroundColor': 'orange','color': 'white'},
                                {'if': {'row_index':3,},'backgroundColor': 'purple','color': 'white'},],
                        ),

        ]
    #if page == 1    
    return [html.H5("Barchart of most frequent words", className="bg-dark text-white text-center"),
            dbc.Row(dcc.Graph(id='bar-chart',figure=bar_all, className = "h-100", style={'height': '500px'}), className="customHeight8"),
            html.H5("Search on words in articles:", className="bg-dark text-white text-center"),
           dbc.Row( 
                dbc.Container([
                    html.Ul(children = [html.Li(x) for x in my_list], id='id1',   ),
                    ],style={"display": "flex", "overflow":"hidden", "overflow-y":"scroll"}, className="h-100 border",
                    ), className = "customHeight9 g-0"), 
            ], [html.H5(goal_page1, className="border bg-white mb-0"),               
                html.H5("Distribution of articles sentiments", className="bg-dark text-white text-center"),
                dbc.Row(                  
                    dbc.Col(
                        dcc.Graph(id='pie-all',figure=pie_all, className = "h-100")), className="customHeight3 g-0"),     
                html.H5("Change the analysis:", className="bg-dark text-white text-center"),
                html.H5('Choose between all articles analysis, or filtered on articles containing POK'),#, className="border bg-white mb-0"),
                dbc.Row(dcc.Dropdown(
                    id='dropdown-update-page1',
                    value='All articles',
                    clearable=False,
                    options=[
                        {'label': name.capitalize(), 'value': name}
                        for name in ['All articles', 'Filter on POK']
                    ], className = "")),  
            ],[
                dbc.Row([
                        html.H5("Wordclouds", className="bg-dark text-white text-center"),
                        html.H5('Click on one of these buttons to view the information from the bar charts in a wordcloud format'),#, className="border bg-white mb-0"),
                ], className="g-0"),
                dbc.Row([
                    dbc.Col(html.Button('Wordcloud all articles', id='btn-nclicks-all', n_clicks=0),),
                    dbc.Col(html.Button('Wordcloud POK articles', id='btn-nclicks-pok', n_clicks=0),),],
            
            ),
            #add modals that shows word clouds to user
               dbc.Modal(
                    [   dbc.ModalHeader(dbc.ModalTitle("All articles")),
                        dcc.Graph(figure=wc_all),
                    ],
                    id="modal_all",
                    size="xl",
                    is_open=False,
                ),
                dbc.Modal(
                    [   dbc.ModalHeader(dbc.ModalTitle("POK related articles")),
                        dcc.Graph(figure=wc_pok),
                    ],
                    id="modal_pok",
                    size="xl",
                    is_open=False,
                ),]



#update sunburst based on cells of dataframe at page 2
@app.callback(Output('print_article', 'children'),
             Input('pca-fig', 'clickData'))
def update_call(data):
    if data:
        article_num = str(data['points'][0]['customdata'][0]).split(' ')[1]
        strline = 'ARTICLE {}:'.format(article_num)
        lst = [strline, [open("data/articles/{}.txt".format(article_num)).read()]]
        return [html.Li(x) for x in lst]

#update K-means clustering
@app.callback(
    Output("pca-fig", "figure"),
    Input('choose-k', 'value'),
    Input('input_plot', 'value'))

def update_layout(value, lst):
    # print(lst)
    df_pca = create_pca(lst)
    return(plot_pca_kmeans(value, df_pca, lst))

#show modal
@app.callback(
    Output("modal_all", "is_open"),
    Input('btn-nclicks-all', 'n_clicks'),
    [State("modal_all", "is_open")],)

def update_layout(data, is_open):
    if data:
        return(not is_open)
    else:
        return (is_open)

#show modal
@app.callback(
    Output("modal_pok", "is_open"),
    Input('btn-nclicks-pok', 'n_clicks'),
    [State("modal_pok", "is_open")],)

def update_layout(data, is_open):
    if data:
        return(not is_open)
    else:
        return (is_open)
    
#update sunburst based on cells of dataframe at page 2
@app.callback(Output('id1', 'children'),
             Input('bar-chart', 'clickData'))
def update_call(data):
    if data:
        lst = print_text_of_words(data['points'][0]['y'])
        return [html.Li(x) for x in lst]
    
#update sunburst based on cells of dataframe at page 2
@app.callback(Output('pie-all', 'figure'),
             Output('bar-chart', 'figure'),
             Input('dropdown-update-page1', 'value'))
def update_call(value):
    return (create_visualizations_page1('pie', value), create_visualizations_page1('bar', value))

#update the heatmap with other input values
@app.callback(Output('heatmap', 'figure'),
              Input('dropdown-interval', 'value'),
              Input('treshold-interval', 'value'))
def update_layout(value, treshold):
    if value == '2 hourly interval':
        inter = 120
    elif value == '1 hourly interval':
        inter = 60
    elif value == '30 minutes interval':
        inter = 30
    elif value == '15 minutes interval':
        inter = 15
    elif value == '5 minutes interval':
        inter = 5

    t = int(treshold.split()[0])
    return(create_heap(inter, t))


#update layout of left network
@app.callback(Output('cytoscape-update-layout-heat', 'layout'),
              Input('dropdown-update-layout-heat', 'value'))
def update_layout(layout):
    return {
        'name': layout,
        'animate': True
    }

#update layout of right network
@app.callback(Output('cytoscape-update-layout-heat-2', 'layout'),
              Input('dropdown-update-layout-heat-2', 'value'))
def update_layout(layout):
    return {
        'name': layout,
        'animate': True
    }

#update both networks by new data obtained from heatmap
@app.callback(Output('cytoscape-update-layout-heat', 'elements'),
              Output('cytoscape-update-layout-heat-2', 'elements'),
              Output('title-plot-1', 'children'),
              Output('title-plot-2', 'children'),
              Input('heatmap','clickData'),
              Input('dropdown-interval', 'value'),
              Input('employee-participants', 'value')
              )
def update_table(clickData, value, employees):
    if clickData:
        if value == '2 hourly interval':
            inter = 120
        elif value == '1 hourly interval':
            inter = 60
        elif value == '30 minutes interval':
            inter = 30

    if employees == 'all':
        only_pok = False
    elif employees == 'only POK':
        only_pok = True

    if clickData:
        xnode = clickData['points'][0]['x']
        ynode = clickData['points'][0]['y']
        elements1 = prepare_data_heap(xnode, inter, only_pok)
        elements2 = prepare_data_heap(ynode, inter, only_pok)
        return(elements1, elements2, xnode, ynode)
    else:
        return ( prepare_data_heap("2014-01-06 10:00", 60, True), prepare_data_heap("2014-01-06 12:00", 60, True),"2014-01-06 10:00","2014-01-06 12:00")

#print subjects of mails after clicked on edge of network 1
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

#print subjects of mails after clicked on edge of network 2
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

#update left sunburst corresponding to nodes of left network
@app.callback(Output('sunburst_network_page3', 'figure'),
             Output('sunburst_exc_page3', 'figure'),
              Input('cytoscape-update-layout-heat', 'tapNodeData'))
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

#update sunburst based on cells of dataframe at page 2
@app.callback(Output('sunburst_network_page2', 'figure'),
             Output('sunburst_exc_page2', 'figure'),
             Input('dash-table', 'active_cell'))
def update_call(cell):
    executives = {'Sten Sanjorge Jr.': 'Sangorge JR. (CEO)', 'Sten Sanjorge Jr': 'Sangorge JR. (CEO)', 'Sten Sanjorge Jr (tethys)': 'Sangorge JR. (CEO)', 'Willem Vasco-Pais': 'Vasco-Pais (ESA)', 'Ingrid Barranco': 'Barranco (CFO)',
                  'Ada Campo-Corrente': 'Campo-Corrente (CIO)', 'Orhan Strum': 'Strum (COO)', 'Mat Bramar': 'Bramar', 'Anda Ribera': 'Ribera','Linda Lagos': 'L.Lagos'}
    if cell:
        row = cell['row']
        name = df_info_associated_employees.iloc[row][1]
        if name in executives.keys():
            return(sunburst_departments_start, sunburst_executive(name, False))
        else:
            return(sunburst_departments(name, False), sunburst_executive_start)
    else:
        return (sunburst_departments('', True),  sunburst_executive('', True))

#update sunburst based on cells of dataframe at page 2
@app.callback(Output('sunburst_network_page4', 'figure'),
             Output('sunburst_exc_page4', 'figure'),
             Input('dash-table4', 'active_cell'))
def update_call(cell):
    executives = {'Sten Sanjorge Jr.': 'Sangorge JR. (CEO)', 'Sten Sanjorge Jr': 'Sangorge JR. (CEO)', 'Sten Sanjorge Jr (tethys)': 'Sangorge JR. (CEO)', 'Willem Vasco-Pais': 'Vasco-Pais (ESA)', 'Ingrid Barranco': 'Barranco (CFO)',
                  'Ada Campo-Corrente': 'Campo-Corrente (CIO)', 'Orhan Strum': 'Strum (COO)', 'Mat Bramar': 'Bramar', 'Anda Ribera': 'Ribera','Linda Lagos': 'L.Lagos'}
    if cell:
        row = cell['row']
        col = cell['column']
        name = df_communities.iloc[row][col]
        if name in executives.keys():
            return(sunburst_departments_start, sunburst_executive(name, False))
        else:
            return(sunburst_departments(name, False), sunburst_executive_start)
    else:
        return (sunburst_departments('', True),  sunburst_executive('', True))

#update tables and corresponding legends
@app.callback(Output('dash-table4', 'style_data_conditional'),
              Output('dash-table-legends', 'data'),
              Output('dash-table-legends', 'columns'),
              Output('dash-table-legends', 'style_data_conditional'),
              Input('Departments', 'value'))
def update_layout(value):
    if value == 'Military':
        style =[
                                {'if': {'row_index':0,},'backgroundColor': 'blue','color': 'white'},
                                {'if': {'row_index':1,},'backgroundColor': 'red','color': 'white'},
                                {'if': {'row_index':2,},'backgroundColor': 'orange','color': 'white'},
                                {'if': {'row_index':3,},'backgroundColor': 'purple','color': 'white'},]
        data = legend_millitary.to_dict('records')
        cols =[{'id': c, 'name': c} for c in legend_millitary.columns]

    elif value == 'Departments':
        style =[
                                {'if': {'row_index':0,},'backgroundColor': 'green','color': 'white'},
                                {'if': {'row_index':1,},'backgroundColor': 'purple','color': 'white'},
                                {'if': {'row_index':2,},'backgroundColor': 'red','color': 'white'},
                                {'if': {'row_index':3,},'backgroundColor': 'blue','color': 'white'},
                                {'if': {'row_index':4,},'backgroundColor': 'orange','color': 'black'}]
        data = legend_department.to_dict('records')
        cols =[{'id': c, 'name': c} for c in legend_department.columns]
    else:
        style =[
                                {'if': {'row_index':0,},'backgroundColor': 'white','color': 'black'},
                                {'if': {'row_index':1,},'backgroundColor': 'yellow','color': 'black'}]
        data = legend_pok.to_dict('records')
        cols =[{'id': c, 'name': c} for c in legend_pok.columns]

    return (communities_plot(value)[1], data, cols, style)

if __name__ == "__main__":
    app.run_server(debug=True)