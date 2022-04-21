import nltk
import glob, os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


def create_heatmap(similarity, cmap = "YlGnBu"):
  df = pd.DataFrame(similarity)
  fig, ax = plt.subplots(figsize=(50,50))
  sns.heatmap(df, cmap=cmap)


def create_pca():
    documents = [open("data/articles/{}".format(f)).read() for f in os.listdir("data/articles")]

    tfidf = TfidfVectorizer().fit_transform(documents)
    pca = PCA(n_components=2)
    df = pca.fit_transform(tfidf.todense())
    return df

def plot_tsne_kmeans(k, df):
    #Initialize the class object
    kmeans = KMeans(n_clusters= k)

    #predict the labels of clusters.
    label = kmeans.fit_predict(df)

    dff = pd.DataFrame(df, columns=['pca1', 'pca2'])
    dff['label'] = [str(i) for i in label]
    dff['label2']= label
    dff['article'] = [i for i in range(845)]
    df = dff.sort_values(by='label2')
    df = df[['pca1', 'pca2', 'label', 'article']]
    return px.scatter(df, x='pca1', y='pca2', color="label", hover_data=['article'])
    