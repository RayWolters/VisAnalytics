from venv import create
import dash
import pandas as pd
import dash_cytoscape as cyto
from dash import html
from dash import dcc
from pprint import pprint
from dash.dependencies import Input, Output
import json


from ast import literal_eval


#TODO overall todo: implement as many filter/classification functions to the plot. Think of: -visualize per day, -per departement, -per subject,  -let user type in a name and show network of this name
#TODO add more functionalities of cytoscape: -highlight networks of users when clicked on -show other networks when clicked

#Cytoscape Callbacks
#https://dash.plotly.com/cytoscape/callbacks

#Cytoscape User Interactions
#https://dash.plotly.com/cytoscape/events




def prepare_data(start_day, start_hour, end_day, end_hour):
    begin_date = "{} {}:00:00".format(start_day, start_hour)
    end_date = "{} {}:00:00".format(end_day, end_hour)

    df = pd.read_csv('data/networkplot_data/alldays.csv')
    df = df.set_index('Day')
    lis = list(df.loc[begin_date: end_date]['Network'])

    l = []
    for row in lis:
        for row2 in literal_eval(row):
            l.append(row2)
    return create_elements(l)

def prepare_data_department(start_day, start_hour, end_day, end_hour, departments, direction):
    begin_date = "{} {}:00:00".format(start_day, start_hour)
    end_date = "{} {}:00:00".format(end_day, end_hour)

    df = pd.read_csv('data/networkplot_data/per_department.csv')
    df = df.set_index(['Department', 'Direction', 'Date'])
    lis = list(df.loc[departments].loc[direction].loc[begin_date: end_date]['Network'])

    l = []
    for row in lis:
        for row2 in literal_eval(row):
            l.append(row2)
    return create_elements(l)

def create_elements(l):
    dic = {'Mat Bramar': 'black', 'Anda Ribera': 'black', 'Rachel Pantanal': 'black', 'Linda Lagos': 'orange', 'Carla Forluniau': 'black', 'Cornelia Lais': 'black',
    'Marin Onda': 'red', 'Isande Borrasca': 'red', 'Axel Calzas': 'red', 'Kare Orilla': 'red', 'Elsa Orilla': 'red', 'Brand Tempestad': 'red', 'Lars Azada': 'red', 'Felix Balas': 'red',
    'Lidelse Dedos': 'red', 'Birgitta Frente': 'red', 'Adra Nubarron': 'red', 'Gustav Cazar': 'red', 'Vira Frente': 'red', 'Willem Vasco-Pais': 'green', 'Ingrid Barranco': 'green',
    'Ada Campo-Corrente': 'green', 'Orhan Strum': 'green', 'Bertrand Ovan': 'purple', 'Emile Arpa': 'purple', 'Varro Awelon': 'purple', 'Dante Coginian': 'purple', 'Albina Hafon': 'purple',
    'Benito Hawelon': 'purple', 'Claudio Hawelon': 'purple', 'Valeria Morlun': 'purple', 'Adan Morlun': 'purple', 'Cecilia Morluniau': 'purple', 'Irene Nant': 'purple', 'Linnea Bergen': 'blue',
    'Lucas Alcazar': 'blue', 'Isak Baza': 'blue', 'Nils Calixto': 'blue', 'Sven Flecha': 'blue', 'Kanon Herrero': 'orange', 'Varja Lagos': 'orange', 'Stenig Fusil': 'orange', 'Hennie Osvaldo': 'orange',
    'Isia Vann': 'orange', 'Edvard Vann': 'orange', 'Felix Resumir': 'orange', 'Loreto Bodrogi': 'orange', 'Hideki Cocinaro': 'orange', 'Inga Ferro': 'orange', 'Ruscella Mies': 'black',
    'Sten Sanjorge Jr': 'green', 'Sten Sanjorge Jr (tethys)': 'black', 'Henk Mies': 'purple', 'Dylan Scozzese': 'purple', 'Minke Mies': 'orange'}

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
        l2.append((row, row, dic[row]))
    nodes_tuple = tuple(l2)

    nodes = [
        {'data': {'id': short, 'label': label},'classes' : color} for short, label, color in nodes_tuple]

    edges = [{'data': {'source': source, 'target': target}} for source, target in edges_tuples]

    elements =  nodes + edges
    return elements





def create_elements_individual(filename, input_name):
    df = pd.read_csv(filename)
    df = df.rename(columns={'source': 'Source', 'target': 'Target', 'weight': 'Weight'})

    df = df[df['Source'] == input_name]

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

    elements =  nodes + edges
    return elements

