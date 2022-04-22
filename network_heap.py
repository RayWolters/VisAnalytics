import pandas as pd
from ast import literal_eval

#this file provides the functions needed to create network visualizations based on user input (clicked on heatmap)

def prepare_data_heap(day, inter, only_pok):
    """
    prepare the data you want to plot, inputs consist of data obtained from clicking on heatmap.
    day -> specific date selected by user
    inter -> interval selected by user
    only_pok -> boolean whether you want to visualize only the network containing POK members or the whole network
    """
    if len(day) ==16:
        day = day + ':00'

    df = pd.read_csv('data/networkplot_data/network_data_{}.csv'.format(inter)).set_index('Day')

    lis = literal_eval(df.loc[day]['Network'])
    pok_names = ['Loreto Bodrogi', 'Hennie Osvaldo', 'Isia Vann', 'Edvard Vann', 'Minke Mies', 'Ruscella Mies', 'Sten Sanjorge Jr (tethys)', 'Sten Sanjorge Jr']

    l = []
    for row in lis:
        l.append(row)

    return create_elements_heap(l, pok_names, only_pok)

def create_elements_heap(l, pok_names, only_pok):
    """
    create the elements of the prepared data
    in this function the nodes/edges are created with corresponding colors obtained from the dictionary
    l -> network data
    pok_names -> names of pok members
    only_pok -> boolean whether you want to visualize only the network containing POK members or the whole network
    """  
    dic = {'Mat Bramar': 'black', 'Anda Ribera': 'black', 'Rachel Pantanal': 'black', 'Linda Lagos': 'orange', 'Carla Forluniau': 'black', 'Cornelia Lais': 'black',
    'Marin Onda': 'red', 'Isande Borrasca': 'red', 'Axel Calzas': 'red', 'Kare Orilla': 'red', 'Elsa Orilla': 'red', 'Brand Tempestad': 'red', 'Lars Azada': 'red', 'Felix Balas': 'red',
    'Lidelse Dedos': 'red', 'Birgitta Frente': 'red', 'Adra Nubarron': 'red', 'Gustav Cazar': 'red', 'Vira Frente': 'red', 'Willem Vasco-Pais': 'green', 'Ingrid Barranco': 'green',
    'Ada Campo-Corrente': 'green', 'Orhan Strum': 'green', 'Bertrand Ovan': 'purple', 'Emile Arpa': 'purple', 'Varro Awelon': 'purple', 'Dante Coginian': 'purple', 'Albina Hafon': 'purple',
    'Benito Hawelon': 'purple', 'Claudio Hawelon': 'purple', 'Valeria Morlun': 'purple', 'Adan Morlun': 'purple', 'Cecilia Morluniau': 'purple', 'Irene Nant': 'purple', 'Linnea Bergen': 'blue',
    'Lucas Alcazar': 'blue', 'Isak Baza': 'blue', 'Nils Calixto': 'blue', 'Sven Flecha': 'blue', 'Kanon Herrero': 'orange', 'Varja Lagos': 'orange', 'Stenig Fusil': 'orange', 'Hennie Osvaldo': 'orange',
    'Isia Vann': 'orange', 'Edvard Vann': 'orange', 'Felix Resumir': 'orange', 'Loreto Bodrogi': 'orange', 'Hideki Cocinaro': 'orange', 'Inga Ferro': 'orange', 'Ruscella Mies': 'black',
    'Sten Sanjorge Jr': 'green', 'Sten Sanjorge Jr (tethys)': 'black', 'Henk Mies': 'purple', 'Dylan Scozzese': 'purple', 'Minke Mies': 'orange'}

    lst =[]
    all_names = []

    if only_pok:
        searchfor = pok_names
    else:
        searchfor = dic.keys()

    for row in l:
        if row[0] in searchfor or row[1] in searchfor:
            all_names.append(row[0])
            all_names.append(row[1])
            lst.append((row[0], row[1]))
          
    edges_tuples = tuple(lst)
    lall_names = list(set(all_names))
    l2 = []
    for row in lall_names:
        if row in pok_names:
            c = dic[row] + '_pok'
        else:
            c = dic[row]
        l2.append((row, row, c))
    nodes_tuple = tuple(l2)

    nodes = [
        {'data': {'id': short, 'label': label},'classes' : color} for short, label, color in nodes_tuple]
    edges = [{'data': {'source': source, 'target': target}} for source, target in edges_tuples]

    elements =  nodes + edges
    return elements



