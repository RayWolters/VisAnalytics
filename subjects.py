import pandas as pd


def get_subjects(filename, source, target):
    df = pd.read_csv(filename)
    dfs = df[df['Source'] == source]
    dft = dfs[dfs['Target'] == target]

    return(list(dft['Subject']))