import pandas as pd
import plotly.graph_objects as go
from dash import dcc

def create_histogram(filename, name):
    df = pd.read_csv(filename)
    df = df.rename(columns={'source': 'Source', 'target': 'Target', 'weight': 'Weight'})

    df = df[df['Source'] == name]

    return dcc.Graph(figure=go.Figure(go.Bar(x=list(df['Target']), y=list(df['Weight']))))
