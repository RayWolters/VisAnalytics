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
import string


from matplotlib import markers
import nltk
import glob, os
import re
import numpy as np
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
from nltk.text import Text
import plotly.graph_objects as go
import plotly.express as px

tokenizer = RegexpTokenizer(r'\w+')
sia = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))

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


def make_flat(docs):
    doclist = tok_prepro_docs(docs)
    flat_list = [item for sublist in doclist for item in sublist]
    return flat_list

def make_bar(docs, size=20, flatten=True):
    #make bar chart
    if flatten:
        freq = nltk.FreqDist(make_flat(docs))
    else:
        freq = nltk.FreqDist(docs)
    testcloud = freq.most_common(size)
    freqdf = pd.DataFrame(testcloud, columns=['Word', 'Frequency'])
    freqdf['category'] = ['negative' if i in ['died', 'death'] else 'neutral' for i in freqdf.Word]
    return px.bar(freqdf, x="Frequency", y="Word", color='category', orientation='h')

def tok_prepro_docs(docs):
    newd = []
    newd_sw = []
    for i in docs:
        i = i.lower()
        i = remove_whitespace(i)
        date = re.findall(r'(\d+/\d+/\d+)', i)
        date2 = re.findall(r'(\d+\s(?:jan|feb|mar|apr|may|jun|jul|aug|oct|sep|nov|dec|january|february|march|april|may|june|july|august|september|october|november|december|January|February|March|April|May|June|July|August|September|October|November|December)\s\d+)',
                           i)
        dates = (date + date2)
        for x in dates:
            i = i.replace(x, '')
        i = i.translate(str.maketrans('', '', string.punctuation))  
        i = tokenizer.tokenize(i)
        newd_sw.append(i)
        newi = [w for w in i if not w.lower() in stop_words]
        newd.append(newi)
    return newd

#preprocessing without tokenizer
def no_tok_prepro_docs(docs):
    texts = []
    newd_sw = []
    for i in docs:
        i = i.lower()
        i = remove_whitespace(i)
        date = re.findall(r'(\d+/\d+/\d+)', i)
        date2 = re.findall(r'(\d+\s(?:jan|feb|mar|apr|may|jun|jul|aug|oct|sep|nov|dec|january|february|march|april|may|june|july|august|september|october|november|december|January|February|March|April|May|June|July|August|September|October|November|December)\s\d+)',
                           i)
        dates = (date + date2)
        for x in dates:
            i = i.replace(x, '')
        texts.append(i)
    return texts

def remove_whitespace(text):
    return  " ".join(text.split())


from wordcloud import WordCloud
def make_wc(docs, size=20, flatten=True):
    if flatten:
        freq = nltk.FreqDist(make_flat(docs))
    else:
        freq = nltk.FreqDist(docs)
    testcloud = freq.most_common(size)
    freqdf = pd.DataFrame(testcloud, columns=['Word', 'Frequency'])
    dataa = freqdf.set_index('Word').to_dict()['Frequency']
    wc = WordCloud(background_color='white', width=800, height=400, max_words=200).generate_from_frequencies(dataa)
    plt.figure(figsize=(12,12))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    return plt

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
    return df, documents


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

def plot_pca_kmeans(k, df, lst_input, documents):
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

    range_ = [i for i in range(len(dff))]
    dff['range'] = range_
    
    df = dff.sort_values(by='label2')
    df = df[['tsne1', 'tsne2', 'label', 'name', 'symbol', 'range']]
    df = df.astype({'label': 'int'})


    for a in range(k):
        l1 = df.loc[df['label'] == a]

        valuesl1 = l1['range'].values

        testdocs = []
        for i in valuesl1:
            testdocs.append(documents[i])
        fig = make_wc(testdocs)

        fig.savefig('wcs/wc_class_{}.png'.format(a),bbox_inches='tight')

    return px.scatter(df, x='tsne1', y='tsne2', color="label", hover_data=['name'], symbol='symbol')
    