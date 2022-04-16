import plotly.express as px
import pandas as pd
def heatmap(interval):
    df = pd.read_csv('data/networkplot_data/heatmap/smaller_network/similarities_{}m.csv'.format(str(interval))).set_index('date')

    fig = px.imshow(df)
    return fig