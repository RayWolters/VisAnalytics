import plotly.graph_objects as go
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


# TODO: Comment code @Ray
# TODO: Check color choice
# TODO: Add interactions
def heatmap():
    path = 'data/articles/'

    documents = [open(path + f, 'r').read() for f in os.listdir(path)]
    tfidf = TfidfVectorizer().fit_transform(documents)
    arr = tfidf.toarray()

    fig3 = go.Figure(data=go.Heatmap(z=cosine_similarity(arr)))
    return fig3