import pandas as pd
from ast import literal_eval


def get_subjects_heap(inter, s, t, date):
    if len(date) ==16:
            date = date + ':00'

    df = pd.read_csv('data/networkplot_data/network_data_{}_subjects.csv'.format(inter)).set_index('Day')

    lis = literal_eval(df.loc[date]['Network'])


    df = pd.DataFrame(lis, columns=['Source', 'Target', 'Subject'])
    dfs = df[df['Source'] == s]
    dft = dfs[dfs['Target'] == t]

    return(list(dft['Subject']))