import os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

path_articles = 'data/articles/'
path_resumes = 'data/resumes/txt versions/'
path_docs = 'data/HistoricalDocuments/txt versions/'

def create_heatmap(similarity, cmap = "YlGnBu"):
  df = pd.DataFrame(similarity)
  fig, ax = plt.subplots(figsize=(50,50))
  sns.heatmap(df, cmap=cmap)

def sorted_alphanumeric(path):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(path, key=alphanum_key)

# def create_pca():
#     """
#     This function will performs the PCA dimensionality reduction on the articles.
#     """
#     ordered_dir_articles = sorted_alphanumeric(os.listdir(path_articles))
#     documents = [open("data/articles/{}".format(f)).read() for f in os.listdir("data/articles")]
#     tfidf = TfidfVectorizer().fit_transform(documents)
#     pca = PCA(n_components=2)
#     df = pca.fit_transform(tfidf.todense())
#     return df

def create_pca(lst_input):
    """
    This function will performs the PCA dimensionality reduction on the articles.
    """    
    documents = []
    
    if path_articles in lst_input:
        for i in sorted_alphanumeric(os.listdir(path_articles)):
            documents.append(open(path_articles + i).read())
    if path_resumes in lst_input:              
        for i in sorted_alphanumeric(os.listdir(path_resumes)):
            documents.append(open(path_resumes + i).read())
    if path_docs in lst_input:
        for i in sorted_alphanumeric(os.listdir(path_docs)):
            documents.append(open(path_docs + i, encoding="utf8").read())

    tfidf = TfidfVectorizer().fit_transform(documents)
    pca = PCA(n_components=2)
    df = pca.fit_transform(tfidf.todense())
    return df


# def plot_pca_kmeans(k, df):
#     """
#     This function will take the PCA's as input and convert it to a k-means plot
#     k  -> number of means (clusters)
#     df -> dataframe containing tsne values 
#     """
#     kmeans = KMeans(n_clusters= k)
#     label = kmeans.fit_predict(df)
#     dff = pd.DataFrame(df, columns=['pca1', 'pca2'])
#     dff['label'] = [str(i) for i in label]
#     dff['label2']= label
#     dff['article'] = [i for i in range(845)]
#     df = dff.sort_values(by='label2')
#     df = df[['pca1', 'pca2', 'label', 'article']]
#     return px.scatter(df, x='pca1', y='pca2', color="label", hover_data=['article'])

def plot_pca_kmeans(k, df, lst_input):
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
    
    article_list, symbol_lst_article = [], []
    resumes_list, symbol_lst_resumes = [], []
    docs_list, symbol_lst_docs       = [], []
    
    if path_articles in lst_input:
        article_list =  ["article " + str(i) for i in range(845)]    
        symbol_lst_article = ['circle' for i in range(845)]
        
    if path_resumes in lst_input:
        resumes_list = sorted_alphanumeric(os.listdir(path_resumes))
        symbol_lst_resumes = ['diamond-cross' for i in range(35)]
        
    if path_docs in lst_input:
        docs_list = sorted_alphanumeric(os.listdir(path_docs))
        symbol_lst_docs = ['triangle-up' for i in range(2)]
        
    
    lst = article_list + resumes_list + docs_list    
    symbol_lst = symbol_lst_article + symbol_lst_resumes + symbol_lst_docs
    dff['name'] = lst
    dff['symbol'] = symbol_lst
    
    df = dff.sort_values(by='label2')
    df = df[['tsne1', 'tsne2', 'label', 'name', 'symbol']]


    return px.scatter(df, x='tsne1', y='tsne2', color="label", hover_data=['name'], symbol='symbol')
    