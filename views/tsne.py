import nltk
import glob, os
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer
import string
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from spellchecker import SpellChecker
import matplotlib.pyplot as plt
from nltk.text import Text
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

# from gensim.parsing.preprocessing import remove_stopwords
pd. set_option('display.max_rows', None)

# from yellowbrick.text import TSNEVisualizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)



from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances, cosine_distances
from sklearn import manifold


import plotly.express as px



#pip installs
#pip install -U gensim

tokenizer = RegexpTokenizer(r'\w+')
sia = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))




def remove_whitespace(text):
    return  " ".join(text.split())

def lemmatization(text): 
    result=[]
    wordnet = WordNetLemmatizer()
    for token,tag in pos_tag(text):
        pos=tag[0].lower()
        
        if pos not in ['a', 'r', 'n', 'v']:
            pos='n'
            
        result.append(wordnet.lemmatize(token,pos))
    
    return result

def stemming(text):
    porter = PorterStemmer()
    result=[]
    for word in text:
        result.append(porter.stem(word))
    return result

#preprocessing with tokenizer
def tok_prepro_docs(docs, nouns=False, stemlem=False):
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
        i = i.replace('ÿ', '')
        i = tokenizer.tokenize(i)
        if nouns:
            tags = nltk.pos_tag(i)
            nouns = [word for word,pos in tags if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS')]
           # i = spell_check(i)
            newd_sw.append(nouns)
            newi = [w for w in nouns if not w.lower() in stop_words]
        else:
            newd_sw.append(i)
            newi = [w for w in i if not w.lower() in stop_words]
        if stemlem:
            newi = lemmatization(newi)
            # newi = stemming(newi)
        newd.append(newi)
    return newd

def no_tok_prepro_docs(docs):
    texts = []
    newd_sw = []
    for i in docs:
        i = i.lower()
        i = remove_whitespace(i)
        # i = remove_stopwords(i)
        date = re.findall(r'(\d+/\d+/\d+)', i)
        date2 = re.findall(r'(\d+\s(?:jan|feb|mar|apr|may|jun|jul|aug|oct|sep|nov|dec|january|february|march|april|may|june|july|august|september|october|november|december|January|February|March|April|May|June|July|August|September|October|November|December)\s\d+)',
                           i)
        dates = (date + date2)
        for x in dates:
            i = i.replace(x, '')
        texts.append(i)
    return texts


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
    ordered_dir = sorted_alphanumeric(os.listdir())
    documents = [open(f).read() for f in ordered_dir]
    tfidf = TfidfVectorizer().fit_transform(documents)
    pca = PCA(n_components=2)
    df = pca.fit_transform(tfidf.todense())
    return df

def plot_tsne_kmeans(k, df):
    """
    This function will take the pca's as input and convert it to a k-means plot
    k  -> number of means (clusters)
    df -> dataframe containing pca values 
    """
    kmeans = KMeans(n_clusters= k)
    label = kmeans.fit_predict(df)
    dff = pd.DataFrame(df, columns=['tsne1', 'tsne2'])
    dff['label'] = [str(i) for i in label]
    dff['label2']= label
    dff['article'] = [i for i in range(845)]
    df = dff.sort_values(by='label2')
    df = df[['tsne1', 'tsne2', 'label', 'article']]
    return px.scatter(df, x='tsne1', y='tsne2', color="label", hover_data=['article']), df
 
def make_bar(docs, size=20, flatten=True):
    if flatten:
        freq = nltk.FreqDist(make_flat(docs))
    else:
        freq = nltk.FreqDist(docs)
    testcloud = freq.most_common(size)
    freqdf = pd.DataFrame(testcloud, columns=['Word', 'Frequency'])
    sns.set(rc={'figure.figsize':(16,11)})
    sns.barplot(x='Frequency',y='Word', data=freqdf)

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
    plt.show()

def make_flat(docs):
    doclist = tok_prepro_docs(docs)
    
    flat_list = [item for sublist in doclist for item in sublist]
    
    return flat_list

def SIA(docs, flatten=False):
    if flatten:
        finaldoc = make_flat(docs)
    else:
        finaldoc = docs
        
    posi = 0
    negi = 0
    neut = 0
    pos_list=[]
    neu_list=[]
    neg_list=[]
    index = []
    
    for text in finaldoc:
        if sia.polarity_scores(text)['compound'] >= 0.33 :
            posi += 1
            pos_list.append(text)
            index.append(1)
        elif sia.polarity_scores(text)['compound'] <= - 0.33 :
            neg_list.append(text)
            negi += 1
            index.append(-1)
        else :
            neut += 1
            neu_list.append(text)
            index.append(0)
            
    sizes = [posi, negi, neut]
    return index

def dummy_fun(doc):
    return doc




def tsneDf(tfidf, metric, labs):
    X = metric(tfidf, tfidf)
    model = manifold.TSNE(random_state=0)
    Y = model.fit_transform(X) 
    df = pd.DataFrame()
    df['labels'] = labs
    df['x'] = Y[:, 0]
    df['y'] = Y[:, 1]
    return df

# def function_tsne(docs, value):


#     sentiment_labels = SIA(no_tok_prepro_docs(docs))

#     tfidf = TfidfVectorizer(
#         analyzer='word',
#         tokenizer=dummy_fun,
#         preprocessor=dummy_fun,
#         token_pattern=None)

#     tfdoc = tfidf.fit_transform(tok_prepro_docs(docs, stemlem=True))

#     if value == "Cosine distance":
#         tdf = tsneDf(tfdoc, cosine_distances, sentiment_labels)
#     else:
#         tdf = tsneDf(tfdoc, euclidean_distances, sentiment_labels)
#     tdf.labels = tdf.labels.astype(str)


#     tdf = tdf.reset_index()

#     return tdf

path_articles = 'data/articles/'
path_resumes = 'data/resumes/txt versions/'
path_docs = 'data/HistoricalDocuments/txt versions/'

def function_tsne(lst_input, value):

    if  lst_input:

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

        docs = documents
        sentiment_labels = SIA(no_tok_prepro_docs(docs))

        tfidf = TfidfVectorizer(
            analyzer='word',
            tokenizer=dummy_fun,
            preprocessor=dummy_fun,
            token_pattern=None)

        tfdoc = tfidf.fit_transform(tok_prepro_docs(docs, stemlem=True))

        if value == "Cosine distance":
            tdf = tsneDf(tfdoc, cosine_distances, sentiment_labels)
        else:
            tdf = tsneDf(tfdoc, euclidean_distances, sentiment_labels)
        tdf.labels = tdf.labels.astype(str)


        tdf = tdf.reset_index()

        return tdf
    else:
        return {}

def plot_tsne(df, lst_input):
    article_list, symbol_lst_article = [], []
    resumes_list, symbol_lst_resumes = [], []
    docs_list, symbol_lst_docs       = [], []
    
    if path_articles in lst_input:
        article_list =  ["article " + str(i) for i in range(845)]    
        symbol_lst_article = ['article' for i in range(845)]
        
    if path_resumes in lst_input:
        resumes_list = sorted_alphanumeric(os.listdir(path_resumes))
        symbol_lst_resumes = ['resume' for i in range(35)]
        
    if path_docs in lst_input:
        docs_list = sorted_alphanumeric(os.listdir(path_docs))
        symbol_lst_docs = ['historical doc' for i in range(2)]

    lst = article_list + resumes_list + docs_list    
    symbol_lst = symbol_lst_article + symbol_lst_resumes + symbol_lst_docs

    df['name'] = lst
    df['symbol'] = symbol_lst
    scatter = px.scatter(df, x='x', y='y', color="labels", color_discrete_map={"-1": 'red', "0": 'blue', "1": 'green'}, hover_data=['name'], symbol='symbol')
    scatter.update_layout(margin=dict(l=0, r=0, b=0, t=0, pad=0), paper_bgcolor='rgba(0,0,0,0)')
    scatter.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(size=12, color="black")))
    return df, scatter


#treshold on number of occurences
treshold = 2

def create_wordcloud(input_docs, names, filename):
    d = dict(Counter(input_docs))
    
    maximum = max(d.values())
    
    dic = {}

    for k, v in d.items():
        if k in names:
                dic[k] = maximum
        elif v > treshold:
            dic[k]  = v

    wordcloud = WordCloud(background_color='white', width = 1000, height = 500)
    wordcloud.generate_from_frequencies(frequencies=dic)

    wordcloud.to_file(filename)

# create dictionary for each type of document with as key file name, and value the corresponding document
def makeDocDict():
    ordered_dir = sorted_alphanumeric(os.listdir("data/HistoricalDocuments/txt versions"))
    ordered_dir2 = sorted_alphanumeric(os.listdir("data/articles"))
    ordered_dir3 = sorted_alphanumeric(os.listdir("data/resumes/txt versions"))
    hist = {f : [open("data/HistoricalDocuments/txt versions/{}".format(f), encoding="utf-8").read()] for f in ordered_dir}
    art = {f : [open("data/articles/{}".format(f), encoding="latin-1").read()] for f in ordered_dir2}
    resumes = {f : [open("data/resumes/txt versions/{}".format(f), encoding="utf-8").read()] for f in ordered_dir3}

    art = dict((k, remove_whitespace(str(v).lower()).rstrip().replace('\\n','')) for k,v in art.items())
    hist = dict((k, str(v).lower().rstrip().replace('\\n','')) for k,v in hist.items())
    resumes = dict((k, remove_whitespace(str(v).lower()).rstrip().replace('\\n','')) for k,v in resumes.items())
    return hist, art, resumes

# get concordance of word and search in all documents
def concor(word, docArt, docHist, docResumes, width=700, max_lines=350):
    if docArt:
        tokenizer2 = RegexpTokenizer('\s+', gaps=True)
        l = []
        for key, value in docArt.items():
            i = tokenizer2.tokenize(value)
            yo = Text(i)
            listy = yo.concordance_list(word, width=width, lines=max_lines)
            if listy:
                l.append('\n{j}, {z} result(s) found, shown below:'.format(z=len(listy), j=key))
                for x in range(min(len(listy), max_lines)):
                    l.append(([f'Result {x+1}: ', listy[x].line.encode('ascii','ignore').decode('unicode_escape')]))
    if docHist:
        s = []
        for key, value in docHist.items():
            i2 = tokenizer2.tokenize(value)
            yo2 = Text(i2)
            listz = yo2.concordance_list(word, width=width, lines=max_lines)
            if listz:
                s.append('\n{j}, {z} result(s) found, shown below:'.format(z=len(listz), j=key))
                for x in range(min(len(listz), max_lines)):
                    s.append(([f'Result {x+1}: ', listz[x].line.encode('utf-8','ignore').decode('utf-8')]))
    if docResumes:
        t = []
        for key, value in docResumes.items():
            i3 = tokenizer2.tokenize(value)
            yo3 = Text(i3)
            lista = yo3.concordance_list(word, width=width, lines=max_lines)
            if lista:
                t.append('\n{j}, {z} result(s) found, shown below:'.format(z=len(lista), j=key))
                for x in range(min(len(lista), max_lines)):
                    t.append(([f'Result {x+1}: ', lista[x].line.encode('ascii','ignore').decode('unicode_escape')]))
    return l, s, t

# calling the methods for concordance
def print_text_of_words(word_val):
    hist, art, resumes = makeDocDict()
    # flatten list of lists
    return [i for e in concor(word_val, art, hist, resumes) for i in e]