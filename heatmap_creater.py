import pandas as pd
import numpy as np
from ast import literal_eval
import matplotlib.pyplot as plt

import networkx as nx
import plotly.express as px

import sys
import warnings

warnings.filterwarnings("ignore")

import seaborn as sns



#this file creates the heatmap visualizing the similarties between different networks.



def jaccard_similarity(g, h):
    if len(g) == 0 and len(h) == 0:
        return 0
    i = set(g).intersection(h)
    return round(len(i) / (len(g) + len(h) - len(i)),3)

def create_data(interval, treshold):
    #interval -> the time interval for networks to be analyzes (e.g. one hour or 30 minutes)
    #treshold -> the maximum number of receivers for one specific mail (e.g. to left out mails send to whole company)
    df = pd.read_csv('data/email headers.csv', encoding='cp1252')
    df.Date = pd.to_datetime(df.Date)
    df.head()

    dffrom = list(df.From)
    dfto = list(df.To)
    dftone = []
    for row in dfto:
        dftone.append(row.split(', '))

    dffrom2 = []
    for row in dffrom:
        if row.split('@')[1] == "gastech.com.tethys":
            dffrom2.append((row.split('@')[0].split('.')[0] + ' ' + row.split('@')[0].split('.')[1]) + ' (tethys)')
        else:
            dffrom2.append((row.split('@')[0].split('.')[0] + ' ' + row.split('@')[0].split('.')[1]))

    ef_to = []
    for row in dftone:
        l = []
        for name in row:
            if name.split('@')[1] == "gastech.com.tethys":
                l.append((name.split('@')[0].split('.')[0] + ' ' + name.split('@')[0].split('.')[1]) + ' (tethys)')
            l.append((name.split('@')[0].split('.')[0] + ' ' + name.split('@')[0].split('.')[1]))
        ef_to.append(l)
    df = pd.DataFrame({ 'from': dffrom2, 'to':ef_to, 'date': df.Date, 'subject':df.Subject})

    df['interval'] = df['date'].dt.round('{}min'.format((str(interval))))  #at this place all networks are rounded to the specific interval.
    df.head()

    data = df.values.tolist()

    dicdat = {}
    for row in data:
        if len(row[1]) < treshold:   #at this place all emails send to more people than treshold are left out of the anlyse to similar networks.
            day = str(row[4])
            if day in dicdat.keys():
                dicdat[day].append(row)
            else:
                dicdat[day] = [row]


    dic = {}

    for key in dicdat.keys():
        lst = dicdat[key]
        lh = []
        for row in lst:
            source = row[0]
            for tat in row[1]:
                lh.append([source, tat, row[3]])
        dic[key] = lh

    l = []

    for k,v in dic.items():
        l.append([k,v])

    return(pd.DataFrame(l, columns=['Day', 'Network']))

def create_heap(interval, treshold):
    df = create_data(interval, treshold).set_index('Day')

    pok_names = ['Loreto Bodrogi', 'Hennie Osvaldo', 'Isia Vann', 'Edvard Vann', 'Minke Mies', 'Ruscella Mies', 'Sten Sanjorge Jr (tethys)', 'Sten Sanjorge Jr']

    dates = df.index

    dic = {}
    for day in dates:
        l = (df.loc[day][0])
        newl = []
        for row in l:
            if row[0] in pok_names or row[1] in pok_names:
                newl.append([row[0], row[1]])

        dic[day] = newl
        
        
    dic_similarities = {}

    for day in dates:
        siml = []
        l1 = dic[day]

        for day2 in dates:
            l2 = dic[day2]

            G = nx.from_edgelist(l1)
            H = nx.from_edgelist(l2)

            siml.append(jaccard_similarity(G.edges(), H.edges()))

        dic_similarities[day] = siml
        
    df = pd.DataFrame(list(dic_similarities.values()),columns=dates)
    df['date'] = dates
    df = df.set_index('date')
    fig = px.imshow(df)
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0, pad = 3), paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',)
    return(fig)
