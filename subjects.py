import pandas as pd
from ast import literal_eval

#this file returns the correct subjects when a user clicks on an edge.

def get_subjects_heap(inter, s, t, date):  
    """
    This function gets the corresponding subjects of a email network edge and returns it 
    inter -> interval chosen by user
    s -> source node
    t -> target node
    date -> date (indirectly specified by user after clicking on the heatmap)
    """    
    if len(date) ==16:
            date = date + ':00'

    df = pd.read_csv('data/networkplot_data/network_data_{}_subjects.csv'.format(inter)).set_index('Day')

    lis = literal_eval(df.loc[date]['Network'])


    df = pd.DataFrame(lis, columns=['Source', 'Target', 'Subject'])
    print(len(df))
    dfs = df[df['Source'] == s]
    dft = dfs[dfs['Target'] == t]
    return(list(dft['Subject']))