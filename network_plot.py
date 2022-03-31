import dash
import pandas as pd
import dash_cytoscape as cyto
from dash import html
from dash import dcc
from pprint import pprint
from dash.dependencies import Input, Output
import json

#TODO overall todo: implement as many filter/classification functions to the plot. Think of: -visualize per day, -per departement, -per subject,  -let user type in a name and show network of this name
#TODO add more functionalities of cytoscape: -highlight networks of users when clicked on -show other networks when clicked

#Cytoscape Callbacks
#https://dash.plotly.com/cytoscape/callbacks

#Cytoscape User Interactions
#https://dash.plotly.com/cytoscape/events

def create_elements(filename):
    df = pd.read_csv(filename)
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

