
import pandas as pd
from ast import literal_eval
import plotly.graph_objects as go

def weighted_jaccard2(df1, df2):
    # join source and target into one cell
    df1['Edge'] = df1[['source', 'target']].agg(', '.join, axis=1)
    df2['Edge'] = df2[['source', 'target']].agg(', '.join, axis=1)
    
    # only get relevant columns
    df1_rel = df1[['Edge', 'weight']]
    df2_rel = df2[['Edge', 'weight']]
    
    # transpose the dataframes and rename row name weight to graph_x_weight
    df1_renamed = df1_rel.T.rename(index={'weight' : 'graph_one_weight'})
    df2_renamed = df2_rel.T.rename(index={'weight' : 'graph_two_weight'})
    
    # Move row edge as columns and only keep relevant rows
    df1_final = df1_renamed.rename(columns=df1_renamed.iloc[0]).iloc[1:]
    df2_final = df2_renamed.rename(columns=df2_renamed.iloc[0]).iloc[1:]
    
    # Concat the two dataframes and replace NaN by 0's meaning that the edge is not present at all in a graph
    df_combined = pd.concat([df1_final, df2_final]).fillna(0)
    
    # Calculate weighted jaccard similarity by taking row-wise min and summing each row to get the numerator
    # and for the denominator taking the max instead of min. Dividing this gives the jaccard similarity.
    weighted_jaccard_sim = (df_combined.min().sum()) / (df_combined.max().sum())
    return weighted_jaccard_sim

def lineplot():
    df = pd.read_csv('data/networkplot_data/alldays.csv', )
    nw_sim = pd.DataFrame()
    emjac = []
    emiter = []

    for i in range(len(df) -1): 
        df1 = pd.DataFrame(literal_eval(df.iloc[i]['Network']), columns = ['source', 'target', 'weight'])
        df2 = pd.DataFrame(literal_eval(df.iloc[i +1]['Network']), columns = ['source', 'target', 'weight'])
        if df1.empty == False and df2.empty == False: 
            emjac.append(weighted_jaccard2(df1, df2))
            emiter.append(df.iloc[i][0])
    nw_sim['sim'] = emjac
    nw_sim['time'] = emiter

    return go.Figure(data=go.Scatter(x=nw_sim['time'], y=nw_sim['sim'], mode='markers+lines'))