import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from dash import dcc
from ast import literal_eval

def create_histogram(start_day, start_hour, end_day, end_hour, name, kind):

    dic = {'Mat Bramar': 'black', 'Anda Ribera': 'black', 'Rachel Pantanal': 'black', 'Linda Lagos': 'orange', 'Carla Forluniau': 'black', 'Cornelia Lais': 'black',
    'Marin Onda': 'red', 'Isande Borrasca': 'red', 'Axel Calzas': 'red', 'Kare Orilla': 'red', 'Elsa Orilla': 'red', 'Brand Tempestad': 'red', 'Lars Azada': 'red', 'Felix Balas': 'red',
    'Lidelse Dedos': 'red', 'Birgitta Frente': 'red', 'Adra Nubarron': 'red', 'Gustav Cazar': 'red', 'Vira Frente': 'red', 'Willem Vasco-Pais': 'green', 'Ingrid Barranco': 'green',
    'Ada Campo-Corrente': 'green', 'Orhan Strum': 'green', 'Bertrand Ovan': 'purple', 'Emile Arpa': 'purple', 'Varro Awelon': 'purple', 'Dante Coginian': 'purple', 'Albina Hafon': 'purple',
    'Benito Hawelon': 'purple', 'Claudio Hawelon': 'purple', 'Valeria Morlun': 'purple', 'Adan Morlun': 'purple', 'Cecilia Morluniau': 'purple', 'Irene Nant': 'purple', 'Linnea Bergen': 'blue',
    'Lucas Alcazar': 'blue', 'Isak Baza': 'blue', 'Nils Calixto': 'blue', 'Sven Flecha': 'blue', 'Kanon Herrero': 'orange', 'Varja Lagos': 'orange', 'Stenig Fusil': 'orange', 'Hennie Osvaldo': 'orange',
    'Isia Vann': 'orange', 'Edvard Vann': 'orange', 'Felix Resumir': 'orange', 'Loreto Bodrogi': 'orange', 'Hideki Cocinaro': 'orange', 'Inga Ferro': 'orange', 'Ruscella Mies': 'black',
    'Sten Sanjorge Jr': 'green', 'Sten Sanjorge Jr (tethys)': 'black', 'Henk Mies': 'purple', 'Dylan Scozzese': 'purple', 'Minke Mies': 'orange'}
    
    begin_date = "{} {}:00:00".format(start_day, start_hour)
    end_date = "{} {}:00:00".format(end_day, end_hour)

    df = pd.read_csv('data/networkplot_data/alldays.csv')
    df = df.set_index('Day')
    lis = list(df.loc[begin_date: end_date]['Network'])

    l = []
    for row in lis:
        for row2 in literal_eval(row):
            l.append(row2)
    
    df = pd.DataFrame(l, columns=['Source', 'Target', 'Weight'])
    
    if kind == 'source':
        df = df[df['Source'] == name]
        df = df[['Target', 'Weight']]
        return dcc.Graph(figure=go.Figure(go.Bar(x=list(df['Target']), y=list(df['Weight']))))
        # return dcc.Graph(figure=px.bar(x=list(df['Target']), y=list(df['Weight'])))

    elif kind =='target':
        df = df[df['Target'] == name]
        
        # col = []
        # lst_target = list(df['Source'])
        # for row in lst_target:
        #     col.append(dic[row])

        df = df[['Source', 'Weight']]

        return dcc.Graph(figure=go.Figure(go.Bar(x=list(df['Source']), y=list(df['Weight']))))

def create_histogram_department(start_day, start_hour, end_day, end_hour, departments, direction, name, kind):
    begin_date = "{} {}:00:00".format(start_day, start_hour)
    end_date = "{} {}:00:00".format(end_day, end_hour)

    df = pd.read_csv('data/networkplot_data/per_department.csv')
    df = df.set_index(['Department', 'Direction', 'Date'])
    lis = list(df.loc[departments].loc[direction].loc[begin_date: end_date]['Network'])

    l = []
    for row in lis:
        for row2 in literal_eval(row):
            l.append(row2)
    df = pd.DataFrame(l, columns=['Source', 'Target', 'Weight'])

    if kind == 'source':
        df = df[df['Source'] == name]
        return dcc.Graph(figure=go.Figure(go.Bar(x=list(df['Target']), y=list(df['Weight']))))

    elif kind == 'target':
        df = df[df['Target'] == name]
        return dcc.Graph(figure=go.Figure(go.Bar(x=list(df['Source']), y=list(df['Weight']))))

