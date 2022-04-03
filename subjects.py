import pandas as pd
from ast import literal_eval


# def get_subjects2(filename, source, target):
#     df = pd.read_csv(filename)
#     dfs = df[df['Source'] == source]
#     dft = dfs[dfs['Target'] == target]

#     return(list(dft['Subject']))


def get_subjects(start_day, start_hour, end_day, end_hour, source, target):

    begin_date = "{} {}:00:00".format(start_day, start_hour)
    end_date = "{} {}:00:00".format(end_day, end_hour)

    df = pd.read_csv('data/networkplot_data/subjects.csv')
    df = df.set_index('Day')
    lis = list(df.loc[begin_date: end_date]['Network'])

    l = []
    for row in lis:
        for row2 in literal_eval(row):
            l.append(row2)
    
    df = pd.DataFrame(l, columns=['Source', 'Target', 'Subject'])
    dfs = df[df['Source'] == source]
    dft = dfs[dfs['Target'] == target]

    return(list(dft['Subject']))