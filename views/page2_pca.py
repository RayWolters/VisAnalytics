import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


#this file provides the informatin for the second page.

def create_heatmap(similarity, cmap = "YlGnBu"):
  df = pd.DataFrame(similarity)
  fig, ax = plt.subplots(figsize=(50,50))
  sns.heatmap(df, cmap=cmap)


def create_pca():
    """
    This function will performs the PCA dimensionality reduction on the articles.
    """
    documents = [open("data/articles/{}".format(f)).read() for f in os.listdir("data/articles")]

    tfidf = TfidfVectorizer().fit_transform(documents)
    pca = PCA(n_components=2)
    df = pca.fit_transform(tfidf.todense())
    return df

def plot_pca_kmeans(k, df):
    """
    This function will take the pca's as input and convert it to a k-means plot
    k  -> number of means (clusters)
    df -> dataframe containing pca values 
    """
    kmeans = KMeans(n_clusters= k)
    label = kmeans.fit_predict(df)
    dff = pd.DataFrame(df, columns=['pca1', 'pca2'])
    dff['label'] = [str(i) for i in label]
    dff['label2']= label
    dff['article'] = [i for i in range(845)]
    df = dff.sort_values(by='label2')
    df = df[['pca1', 'pca2', 'label', 'article']]
    return px.scatter(df, x='pca1', y='pca2', color="label", hover_data=['article'])
    