###########################################
import dash
import pandas as pd
import dash_cytoscape as cyto
from dash import html
from dash import dcc
from pprint import pprint
from dash.dependencies import Input, Output
import json
###########################################

def create_elements(df):
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

    return nodes, edges