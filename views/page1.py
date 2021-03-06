from matplotlib import markers
import nltk
import glob, os
import re
import numpy as np
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer
import string
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt
from nltk.text import Text
import plotly.graph_objects as go
import plotly.express as px

nltk.download('vader_lexicon')
nltk.download('stopwords')

tokenizer = RegexpTokenizer(r'\w+')
sia = SentimentIntensityAnalyzer()
stop_words = set(stopwords.words('english'))



#this file will provide the visualizations for page 1. The most important function is create_visualizations_page1(). 
#the rest are helper functions for preprocessing

#removes spaces
def remove_whitespace(text):
    return  " ".join(text.split())

#lemitizing
def lemmatization(text): 
    result=[]
    wordnet = WordNetLemmatizer()
    for token,tag in pos_tag(text):
        pos=tag[0].lower()
        if pos not in ['a', 'r', 'n', 'v']:
            pos='n'    
        result.append(wordnet.lemmatize(token,pos))
    return result

#reduce words to their stem version
def stemming(text):
    porter = PorterStemmer()
    result=[]
    for word in text:
        result.append(porter.stem(word))
    return result

#sort file names on alphanumeric 
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

#preprocessing with tokenizer
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

#sentiment analysis
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

    for text in finaldoc:
        if sia.polarity_scores(text)['compound'] >= 0.33 :
            posi += 1
            pos_list.append(text)
        elif sia.polarity_scores(text)['compound'] <= - 0.33 :
            neg_list.append(text)
            negi += 1
        else :
            neut += 1
            neu_list.append(text)
            
    sizes = [posi, negi, neut]
    return sizes, pos_list, neg_list, neu_list


#visualizations
def make_pie(docs):
    #make the pie chart.
    labels = 'Positive', 'Negative', 'Neutral'
    sizes, _, _, _ = SIA(docs)
    
    colors = ['blue', 'orange', 'lightgrey']
    layout = go.Layout(
        margin = go.layout.Margin(
            l=0,
            r=0,
            b=0,
            t=0,
            pad = 0,
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    fig = go.Figure(data=[go.Pie(labels=['Positive', 'Negative', 'Neutral'],
                                 values=sizes)], layout=layout)
    fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=15,
                      marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    return fig
    
def make_bar(docs, indicator, size=20, flatten=True):
    #make bar chart
    if flatten:
        freq = nltk.FreqDist(make_flat(docs))
    else:
        freq = nltk.FreqDist(docs)
    testcloud = freq.most_common(size)
    freqdf = pd.DataFrame(testcloud, columns=['Word', 'Frequency'])
    freqdf['category'] = ['negative' if i in ['died', 'death'] else 'neutral' for i in freqdf.Word]
    if indicator:
        fig = px.bar(freqdf, x="Frequency", y="Word", orientation='h', color_discrete_sequence=['orange']*len(freqdf) )
    else:

        fig = px.bar(freqdf, x="Frequency", y="Word", color='category', orientation='h', color_discrete_map={'negative': 'orange','neutral': 'lightgrey'}, category_orders={'Word': freqdf.Word[::-1]})
    return fig



#makes a flat list of a nested one
def make_flat(docs):
    doclist = tok_prepro_docs(docs)
    flat_list = [item for sublist in doclist for item in sublist]
    return flat_list

#read file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        read = f.read()
        return read


def create_visualizations_page1(plot, filter):
    """
    This function creates the visualization of page 1.
    plot -> the kind of plot (bar/pie)
    filter -> which articles to use in analyze (all articles or only pok related)
    """
    ordered_dir = sorted_alphanumeric(os.listdir("data/articles"))
    documents = [open("data/articles/{}".format(f)).read() for f in ordered_dir]

    if filter =='All articles':
        if plot == 'pie':
            return make_pie(documents)
        elif plot == 'bar':
            _, _, neg_articles, _ = SIA(documents)
            return make_bar(neg_articles, False)

    elif filter == 'Filter on POK':
        pok_only = []
        pok_only_dict = {}

        for index, item in enumerate(no_tok_prepro_docs(documents)):
            if 'pok' in item or 'protectors of kronos' in item:
                pok_only.append(item)
                pok_only_dict[index] = item

        _, _, neg_word_list, _ = SIA(pok_only, flatten=True)
        if plot == 'pie':
            return make_pie(pok_only)
        elif plot == 'bar':
            return make_bar(neg_word_list, True) 

def makeDocDict(docs):
    testdict = {}
    for index, item in enumerate(docs):
        item = remove_whitespace(item)
        i = item.lower()
        if 'pok' in i:
            testdict[index] = item
    return testdict

def concor(word, docdict, width=80, max_lines=25):
    tokenizer2 = RegexpTokenizer('\s+', gaps=True)
    l = []
    for key, value in docdict.items():
        i = tokenizer2.tokenize(value)
        yo = Text(i)
        listy = yo.concordance_list(word, width=width, lines=200)
        if listy:
            l.append('\nArticle {j}.txt, {z} result(s) found, shown below:'.format(z=len(listy), j=key))
            for x in range(min(len(listy), max_lines)):
                l.append(([f'Result {x+1}: ', listy[x].line.encode('ascii','ignore').decode('unicode_escape')]))
    return(l)

def print_text_of_words(word_val, width=80):
    ordered_dir = sorted_alphanumeric(os.listdir("data/articles"))
    documents = [open("data/articles/{}".format(f)).read() for f in ordered_dir]

    return concor(word_val, makeDocDict(documents), width)