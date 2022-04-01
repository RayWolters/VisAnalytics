import pandas as pd
import plotly.graph_objects as go
from dash import dcc
from ast import literal_eval

def create_histogram(start_day, start_hour, end_day, end_hour, name):

    begin_date = "{} {}:00:00".format(start_day, start_hour)
    end_date = "{} {}:00:00".format(end_day, end_hour)

    df = pd.read_csv('data/networkplot_data/alldays.csv')
    df = df.set_index('Day')
    lis = list(df.loc[begin_date: end_date]['Network'])

    l = []
    for row in lis:
        for row2 in literal_eval(row):
            l.append(row2)
    
    df = pd.DataFrame(l, columns=['Source', 'Target', 'Weight'])

    df = df[df['Source'] == name]

    return dcc.Graph(figure=go.Figure(go.Bar(x=list(df['Target']), y=list(df['Weight']))))

def create_histogram_department(start_day, start_hour, end_day, end_hour, departments, direction, name):
    begin_date = "{} {}:00:00".format(start_day, start_hour)
    end_date = "{} {}:00:00".format(end_day, end_hour)

    df = pd.read_csv('data/networkplot_data/per_department.csv')
    df = df.set_index(['Department', 'Direction', 'Date'])
    lis = list(df.loc[departments].loc[direction].loc[begin_date: end_date]['Network'])

    l = []
    for row in lis:
        for row2 in literal_eval(row):
            l.append(row2)
    df = pd.DataFrame(l, columns=['Source', 'Target', 'Weight'])

    df = df[df['Source'] == name]

    return dcc.Graph(figure=go.Figure(go.Bar(x=list(df['Target']), y=list(df['Weight']))))
