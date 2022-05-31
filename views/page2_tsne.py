import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans

path_articles = 'data/articles/'
path_historical_docs = 'data/HistoricalDocuments/txt versions/'

def create_heatmap(similarity, cmap = "YlGnBu"):
  df = pd.DataFrame(similarity)
  fig, ax = plt.subplots(figsize=(50,50))
  sns.heatmap(df, cmap=cmap)

def sorted_alphanumeric(path):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(path, key=alphanum_key)

def create_tsne():
    """
    This function will performs the TSNE dimensionality reduction on the articles, historical documents, resumes.
    """
    ordered_dir_articles = sorted_alphanumeric(os.listdir(path_articles))
    documents = [open(path_articles + f).read() for f in ordered_dir_articles]
    tfidf = TfidfVectorizer().fit_transform(documents)
    tsne = TSNE(n_components=2)
    df = tsne.fit_transform(tfidf.todense())
    return df


def plot_tsne_kmeans(k, df):
    """
    This function will take the tsne's as input and convert it to a k-means plot
    k  -> number of means (clusters)
    df -> dataframe containing tsne values 
    """
    kmeans = KMeans(n_clusters= k)
    label = kmeans.fit_predict(df)
    dff = pd.DataFrame(df, columns=['tsne1', 'tsne2'])
    dff['label'] = [str(i) for i in label]
    dff['label2']= label
    dff['article'] = [i for i in range(845)]
    df = dff.sort_values(by='label2')
    df = df[['tsne1', 'tsne2', 'label', 'article']]
    return px.scatter(df, x='tsne1', y='tsne2', color="label", hover_data=['article'])
    