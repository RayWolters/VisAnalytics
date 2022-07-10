from tsne import function_tsne
import os 
import re


import nltk
nltk.download('omw-1.4')

def sorted_alphanumeric(path):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(path, key=alphanum_key)

path_articles = 'data/articles/'


documents = []
for i in sorted_alphanumeric(os.listdir(path_articles)):
    documents.append(open(path_articles + i).read())

tfd = function_tsne(documents)

