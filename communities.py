import pandas as pd


def communities_plot(color):

    dic = {'Mat Bramar': 'grey', 'Anda Ribera': 'grey', 'Rachel Pantanal': 'grey', 'Linda Lagos': 'orange', 'Carla Forluniau': 'grey', 'Cornelia Lais': 'grey',
    'Marin Onda': 'red', 'Isande Borrasca': 'red', 'Axel Calzas': 'red', 'Kare Orilla': 'red', 'Elsa Orilla': 'red', 'Brand Tempestad': 'red', 'Lars Azada': 'red', 'Felix Balas': 'red',
    'Lidelse Dedos': 'red', 'Birgitta Frente': 'red', 'Adra Nubarron': 'red', 'Gustav Cazar': 'red', 'Vira Frente': 'red', 'Willem Vasco-Pais': 'green', 'Ingrid Barranco': 'green',
    'Ada Campo-Corrente': 'green', 'Orhan Strum': 'green', 'Bertrand Ovan': 'purple', 'Emile Arpa': 'purple', 'Varro Awelon': 'purple', 'Dante Coginian': 'purple', 'Albina Hafon': 'purple',
    'Benito Hawelon': 'purple', 'Claudio Hawelon': 'purple', 'Valeria Morlun': 'purple', 'Adan Morlun': 'purple', 'Cecilia Morluniau': 'purple', 'Irene Nant': 'purple', 'Linnea Bergen': 'blue',
    'Lucas Alcazar': 'blue', 'Isak Baza': 'blue', 'Nils Calixto': 'blue', 'Sven Flecha': 'blue', 'Kanon Herrero': 'orange', 'Varja Lagos': 'orange', 'Stenig Fusil': 'orange', 'Hennie Osvaldo': 'orange',
    'Isia Vann': 'orange', 'Edvard Vann': 'orange', 'Felix Resumir': 'orange', 'Loreto Bodrogi': 'orange', 'Hideki Cocinaro': 'orange', 'Inga Ferro': 'orange', 'Ruscella Mies': 'grey',
    'Sten Sanjorge Jr': 'green', 'Sten Sanjorge Jr (tethys)': 'green', 'Henk Mies': 'purple', 'Dylan Scozzese': 'purple', 'Minke Mies': 'orange'}


    df = pd.read_csv('data/networkplot_data/communities.csv').drop(columns=['Unnamed: 0'])
    df.columns=['class 1','class 2','class 3','class 4','class 5', 'class 6']
    df = df.fillna('')
    df_communities = df

    lst_communities = [
                                    {'if': {'row_index': 0,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][0]]),'color': 'black'},{'if': {'row_index': 1,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][1]]),'color': 'white'},
                                    {'if': {'row_index': 2,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][2]]),'color': 'white'},{'if': {'row_index': 3,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][3]]),'color': 'black'},
                                    {'if': {'row_index': 4,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][4]]),'color': 'white'},{'if': {'row_index': 5,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][5]]),'color': 'white'},
                                    {'if': {'row_index': 6,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][6]]),'color': 'white'},{'if': {'row_index': 7,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][7]]),'color': 'white'},
                                    {'if': {'row_index': 8,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][8]]),'color': 'white'},{'if': {'row_index': 9,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][9]]),'color': 'white'},
                                    {'if': {'row_index': 10,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][10]]),'color': 'white'},{'if': {'row_index': 11,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][11]]),'color': 'white'},
                                    {'if': {'row_index': 12,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][12]]),'color': 'white'},

                                    {'if': {'row_index': 0, 'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][0]]),'color': 'white'}, {'if': {'row_index': 1,'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][1]]),'color': 'black'},
                                    {'if': {'row_index': 2, 'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][2]]),'color': 'black'}, {'if': {'row_index': 3,'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][3]]),'color': 'white'},
                                    {'if': {'row_index': 4, 'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][4]]),'color': 'white'}, {'if': {'row_index': 5,'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][5]]),'color': 'white'},
                                    {'if': {'row_index': 6, 'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][6]]),'color': 'black'}, {'if': {'row_index': 7,'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][7]]),'color': 'white'},
                                    {'if': {'row_index': 8, 'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][8]]),'color': 'white'}, {'if': {'row_index': 9,'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][9]]),'color': 'white'},
                                    {'if': {'row_index': 10,'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][10]]),'color': 'white'}, {'if': {'row_index': 11,'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][11]]),'color': 'white'},

                                    {'if': {'row_index': 0, 'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][0]]),'color': 'white'}, {'if': {'row_index': 1,'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][1]]),'color': 'black'},
                                    {'if': {'row_index': 2, 'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][2]]),'color': 'white'}, {'if': {'row_index': 3,'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][3]]),'color': 'white'},
                                    {'if': {'row_index': 4, 'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][4]]),'color': 'black'}, {'if': {'row_index': 5,'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][5]]),'color': 'black'},
                                    {'if': {'row_index': 6, 'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][6]]),'color': 'black'}, {'if': {'row_index': 7,'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][7]]),'color': 'black'},
                                
                                    {'if': {'row_index': 0, 'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][0]]),'color': 'black'}, {'if': {'row_index': 1,'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][1]]),'color': 'black'},
                                    {'if': {'row_index': 2, 'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][2]]),'color': 'white'}, {'if': {'row_index': 3,'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][3]]),'color': 'white'},
                                    {'if': {'row_index': 4, 'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][4]]),'color': 'white'}, {'if': {'row_index': 5,'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][5]]),'color': 'white'},
                                    {'if': {'row_index': 6, 'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][6]]),'color': 'black'}, {'if': {'row_index': 7,'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][7]]),'color': 'black'},

                                    {'if': {'row_index': 0, 'column_id': 'class 5'},'backgroundColor': str(dic[df_communities['class 5'][0]]),'color': 'white'}, {'if': {'row_index': 1,'column_id': 'class 5'},'backgroundColor': str(dic[df_communities['class 5'][1]]),'color': 'white'},
                                    {'if': {'row_index': 2, 'column_id': 'class 5'},'backgroundColor': str(dic[df_communities['class 5'][2]]),'color': 'white'}, {'if': {'row_index': 3,'column_id': 'class 5'},'backgroundColor': str(dic[df_communities['class 5'][3]]),'color': 'white'},
                                    {'if': {'row_index': 4, 'column_id': 'class 5'},'backgroundColor': str(dic[df_communities['class 5'][4]]),'color': 'white'}, {'if': {'row_index': 5,'column_id': 'class 5'},'backgroundColor': str(dic[df_communities['class 5'][5]]),'color': 'white'},

                                    {'if': {'row_index': 0, 'column_id': 'class 6'},'backgroundColor': str(dic[df_communities['class 6'][0]]),'color': 'black'}, {'if': {'row_index': 1,'column_id': 'class 6'},'backgroundColor': str(dic[df_communities['class 6'][1]]),'color': 'white'},
                                    {'if': {'row_index': 2, 'column_id': 'class 6'},'backgroundColor': str(dic[df_communities['class 6'][2]]),'color': 'black'}, {'if': {'row_index': 3,'column_id': 'class 6'},'backgroundColor': str(dic[df_communities['class 6'][3]]),'color': 'black'},
                                    {'if': {'row_index': 4, 'column_id': 'class 6'},'backgroundColor': str(dic[df_communities['class 6'][4]]),'color': 'black'}, {'if': {'row_index': 5,'column_id': 'class 6'},'backgroundColor': str(dic[df_communities['class 6'][5]]),'color': 'white'}
                                                                
                                    ]
    if color == 'Department':
        lst_communities = [
                                    {'if': {'row_index': 0,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][0]]),'color': 'black'},{'if': {'row_index': 1,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][1]]),'color': 'white'},
                                    {'if': {'row_index': 2,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][2]]),'color': 'white'},{'if': {'row_index': 3,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][3]]),'color': 'black'},
                                    {'if': {'row_index': 4,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][4]]),'color': 'white'},{'if': {'row_index': 5,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][5]]),'color': 'white'},
                                    {'if': {'row_index': 6,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][6]]),'color': 'white'},{'if': {'row_index': 7,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][7]]),'color': 'white'},
                                    {'if': {'row_index': 8,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][8]]),'color': 'white'},{'if': {'row_index': 9,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][9]]),'color': 'white'},
                                    {'if': {'row_index': 10,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][10]]),'color': 'white'},{'if': {'row_index': 11,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][11]]),'color': 'white'},
                                    {'if': {'row_index': 12,'column_id': 'class 1'},'backgroundColor': str(dic[df_communities['class 1'][12]]),'color': 'white'},

                                    {'if': {'row_index': 0, 'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][0]]),'color': 'white'}, {'if': {'row_index': 1,'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][1]]),'color': 'black'},
                                    {'if': {'row_index': 2, 'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][2]]),'color': 'black'}, {'if': {'row_index': 3,'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][3]]),'color': 'white'},
                                    {'if': {'row_index': 4, 'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][4]]),'color': 'white'}, {'if': {'row_index': 5,'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][5]]),'color': 'white'},
                                    {'if': {'row_index': 6, 'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][6]]),'color': 'black'}, {'if': {'row_index': 7,'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][7]]),'color': 'white'},
                                    {'if': {'row_index': 8, 'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][8]]),'color': 'white'}, {'if': {'row_index': 9,'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][9]]),'color': 'white'},
                                    {'if': {'row_index': 10,'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][10]]),'color': 'white'}, {'if': {'row_index': 11,'column_id': 'class 2'},'backgroundColor': str(dic[df_communities['class 2'][11]]),'color': 'white'},

                                    {'if': {'row_index': 0, 'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][0]]),'color': 'white'}, {'if': {'row_index': 1,'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][1]]),'color': 'black'},
                                    {'if': {'row_index': 2, 'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][2]]),'color': 'white'}, {'if': {'row_index': 3,'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][3]]),'color': 'white'},
                                    {'if': {'row_index': 4, 'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][4]]),'color': 'black'}, {'if': {'row_index': 5,'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][5]]),'color': 'black'},
                                    {'if': {'row_index': 6, 'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][6]]),'color': 'black'}, {'if': {'row_index': 7,'column_id': 'class 3'},'backgroundColor': str(dic[df_communities['class 3'][7]]),'color': 'black'},
                                
                                    {'if': {'row_index': 0, 'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][0]]),'color': 'black'}, {'if': {'row_index': 1,'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][1]]),'color': 'black'},
                                    {'if': {'row_index': 2, 'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][2]]),'color': 'white'}, {'if': {'row_index': 3,'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][3]]),'color': 'white'},
                                    {'if': {'row_index': 4, 'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][4]]),'color': 'white'}, {'if': {'row_index': 5,'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][5]]),'color': 'white'},
                                    {'if': {'row_index': 6, 'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][6]]),'color': 'black'}, {'if': {'row_index': 7,'column_id': 'class 4'},'backgroundColor': str(dic[df_communities['class 4'][7]]),'color': 'black'},

                                    {'if': {'row_index': 0, 'column_id': 'class 5'},'backgroundColor': str(dic[df_communities['class 5'][0]]),'color': 'white'}, {'if': {'row_index': 1,'column_id': 'class 5'},'backgroundColor': str(dic[df_communities['class 5'][1]]),'color': 'white'},
                                    {'if': {'row_index': 2, 'column_id': 'class 5'},'backgroundColor': str(dic[df_communities['class 5'][2]]),'color': 'white'}, {'if': {'row_index': 3,'column_id': 'class 5'},'backgroundColor': str(dic[df_communities['class 5'][3]]),'color': 'white'},
                                    {'if': {'row_index': 4, 'column_id': 'class 5'},'backgroundColor': str(dic[df_communities['class 5'][4]]),'color': 'white'}, {'if': {'row_index': 5,'column_id': 'class 5'},'backgroundColor': str(dic[df_communities['class 5'][5]]),'color': 'white'},

                                    {'if': {'row_index': 0, 'column_id': 'class 6'},'backgroundColor': str(dic[df_communities['class 6'][0]]),'color': 'black'}, {'if': {'row_index': 1,'column_id': 'class 6'},'backgroundColor': str(dic[df_communities['class 6'][1]]),'color': 'white'},
                                    {'if': {'row_index': 2, 'column_id': 'class 6'},'backgroundColor': str(dic[df_communities['class 6'][2]]),'color': 'black'}, {'if': {'row_index': 3,'column_id': 'class 6'},'backgroundColor': str(dic[df_communities['class 6'][3]]),'color': 'black'},
                                    {'if': {'row_index': 4, 'column_id': 'class 6'},'backgroundColor': str(dic[df_communities['class 6'][4]]),'color': 'black'}, {'if': {'row_index': 5,'column_id': 'class 6'},'backgroundColor': str(dic[df_communities['class 6'][5]]),'color': 'white'}
                                                                
                                    ]
    if color == 'Gender':
        lst_communities = [              {'if': {'row_index': 0,'column_id': 'class 1'},'backgroundColor': 'blue','color': 'white'},{'if': {'row_index': 1,'column_id': 'class 1'},'backgroundColor': 'red','color': 'white'},
                                        {'if': {'row_index': 2,'column_id': 'class 1'},'backgroundColor':'blue','color': 'white'},{'if': {'row_index': 3,'column_id': 'class 1'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 4,'column_id': 'class 1'},'backgroundColor':'blue','color': 'white'},{'if': {'row_index': 5,'column_id': 'class 1'},'backgroundColor': 'red','color': 'white'},
                                        {'if': {'row_index': 6,'column_id': 'class 1'},'backgroundColor':'red','color': 'white'},{'if': {'row_index': 7,'column_id': 'class 1'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 8,'column_id': 'class 1'},'backgroundColor':'blue','color': 'white'},{'if': {'row_index': 9,'column_id': 'class 1'},'backgroundColor': 'red','color': 'white'},
                                        {'if': {'row_index': 10,'column_id': 'class 1'},'backgroundColor':'blue','color': 'white'},{'if': {'row_index': 11,'column_id': 'class 1'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 12,'column_id': 'class 1'},'backgroundColor':'red','color': 'white'},

                                        {'if': {'row_index': 0, 'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 1,'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 2, 'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 3,'column_id': 'class 2'},'backgroundColor': 'red','color': 'white'},
                                        {'if': {'row_index': 4, 'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 5,'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 6, 'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 7,'column_id': 'class 2'},'backgroundColor': 'red','color': 'white'},
                                        {'if': {'row_index': 8, 'column_id': 'class 2'},'backgroundColor': 'red','color': 'white'}, {'if': {'row_index': 9,'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 10,'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 11,'column_id': 'class 2'},'backgroundColor': 'red','color': 'white'},

                                        {'if': {'row_index': 0, 'column_id': 'class 3'},'backgroundColor': 'red','color': 'white'}, {'if': {'row_index': 1,'column_id': 'class 3'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 2, 'column_id': 'class 3'},'backgroundColor': 'red','color': 'white'}, {'if': {'row_index': 3,'column_id': 'class 3'},'backgroundColor': 'red','color': 'white'},
                                        {'if': {'row_index': 4, 'column_id': 'class 3'},'backgroundColor': 'red','color': 'white'}, {'if': {'row_index': 5,'column_id': 'class 3'},'backgroundColor': 'red','color': 'white'},
                                        {'if': {'row_index': 6, 'column_id': 'class 3'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 7,'column_id': 'class 3'},'backgroundColor': 'red','color': 'white'},
                                    
                                        {'if': {'row_index': 0, 'column_id': 'class 4'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 1,'column_id': 'class 4'},'backgroundColor': 'red','color': 'white'},
                                        {'if': {'row_index': 2, 'column_id': 'class 4'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 3,'column_id': 'class 4'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 4, 'column_id': 'class 4'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 5,'column_id': 'class 4'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 6, 'column_id': 'class 4'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 7,'column_id': 'class 4'},'backgroundColor': 'red','color': 'white'},

                                        {'if': {'row_index': 0, 'column_id': 'class 5'},'backgroundColor': 'red','color': 'white'}, {'if': {'row_index': 1,'column_id': 'class 5'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 2, 'column_id': 'class 5'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 3,'column_id': 'class 5'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 4, 'column_id': 'class 5'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 5,'column_id': 'class 5'},'backgroundColor': 'red','color': 'white'},

                                        {'if': {'row_index': 0, 'column_id': 'class 6'},'backgroundColor': 'red','color': 'white'}, {'if': {'row_index': 1,'column_id': 'class 6'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 2, 'column_id': 'class 6'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 3,'column_id': 'class 6'},'backgroundColor': 'red','color': 'white'},
                                        {'if': {'row_index': 4, 'column_id': 'class 6'},'backgroundColor': 'red','color': 'white'}, {'if': {'row_index': 5,'column_id': 'class 6'},'backgroundColor': 'blue','color': 'white'}]
    if color == 'POK':
        lst_communities = [
                                        {'if': {'row_index': 0,'column_id': 'class 1'},'backgroundColor': 'yellow','color': 'black'},{'if': {'row_index': 1,'column_id': 'class 1'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 2,'column_id': 'class 1'},'backgroundColor':'white','color': 'black'},{'if': {'row_index': 3,'column_id': 'class 1'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 4,'column_id': 'class 1'},'backgroundColor':'white','color': 'black'},{'if': {'row_index': 5,'column_id': 'class 1'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 6,'column_id': 'class 1'},'backgroundColor':'white','color': 'black'},{'if': {'row_index': 7,'column_id': 'class 1'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 8,'column_id': 'class 1'},'backgroundColor':'white','color': 'black'},{'if': {'row_index': 9,'column_id': 'class 1'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 10,'column_id': 'class 1'},'backgroundColor':'white','color': 'black'},{'if': {'row_index': 11,'column_id': 'class 1'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 12,'column_id': 'class 1'},'backgroundColor':'white','color': 'black'},

                                        {'if': {'row_index': 0, 'column_id': 'class 2'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 1,'column_id': 'class 2'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 2, 'column_id': 'class 2'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 3,'column_id': 'class 2'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 4, 'column_id': 'class 2'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 5,'column_id': 'class 2'},'backgroundColor': 'yellow','color': 'black'},
                                        {'if': {'row_index': 6, 'column_id': 'class 2'},'backgroundColor': 'yellow','color': 'black'}, {'if': {'row_index': 7,'column_id': 'class 2'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 8, 'column_id': 'class 2'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 9,'column_id': 'class 2'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 10,'column_id': 'class 2'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 11,'column_id': 'class 2'},'backgroundColor': 'white','color': 'black'},

                                        {'if': {'row_index': 0, 'column_id': 'class 3'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 1,'column_id': 'class 3'},'backgroundColor': 'yellow','color': 'black'},
                                        {'if': {'row_index': 2, 'column_id': 'class 3'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 3,'column_id': 'class 3'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 4, 'column_id': 'class 3'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 5,'column_id': 'class 3'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 6, 'column_id': 'class 3'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 7,'column_id': 'class 3'},'backgroundColor': 'white','color': 'black'},
                                    
                                        {'if': {'row_index': 0, 'column_id': 'class 4'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 1,'column_id': 'class 4'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 2, 'column_id': 'class 4'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 3,'column_id': 'class 4'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 4, 'column_id': 'class 4'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 5,'column_id': 'class 4'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 6, 'column_id': 'class 4'},'backgroundColor': 'yellow','color': 'black'}, {'if': {'row_index': 7,'column_id': 'class 4'},'backgroundColor': 'white','color': 'black'},

                                        {'if': {'row_index': 0, 'column_id': 'class 5'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 1,'column_id': 'class 5'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 2, 'column_id': 'class 5'},'backgroundColor': 'yellow','color': 'black'}, {'if': {'row_index': 3,'column_id': 'class 5'},'backgroundColor': 'yellow','color': 'black'},
                                        {'if': {'row_index': 4, 'column_id': 'class 5'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 5,'column_id': 'class 5'},'backgroundColor': 'white','color': 'black'},

                                        {'if': {'row_index': 0, 'column_id': 'class 6'},'backgroundColor': 'yellow','color': 'black'}, {'if': {'row_index': 1,'column_id': 'class 6'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 2, 'column_id': 'class 6'},'backgroundColor': 'yellow','color': 'black'}, {'if': {'row_index': 3,'column_id': 'class 6'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 4, 'column_id': 'class 6'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 5,'column_id': 'class 6'},'backgroundColor': 'white','color': 'black'}]
    if color == 'Military':
        lst_communities = [
                                        {'if': {'row_index': 0,'column_id': 'class 1'},'backgroundColor': 'blue','color': 'white'},{'if': {'row_index': 1,'column_id': 'class 1'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 2,'column_id': 'class 1'},'backgroundColor':'white','color': 'black'},{'if': {'row_index': 3,'column_id': 'class 1'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 4,'column_id': 'class 1'},'backgroundColor':'orange','color': 'white'},{'if': {'row_index': 5,'column_id': 'class 1'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 6,'column_id': 'class 1'},'backgroundColor':'blue','color': 'white'},{'if': {'row_index': 7,'column_id': 'class 1'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 8,'column_id': 'class 1'},'backgroundColor':'blue','color': 'white'},{'if': {'row_index': 9,'column_id': 'class 1'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 10,'column_id': 'class 1'},'backgroundColor':'purple','color': 'white'},{'if': {'row_index': 11,'column_id': 'class 1'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 12,'column_id': 'class 1'},'backgroundColor':'white','color': 'black'},

                                        {'if': {'row_index': 0, 'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 1,'column_id': 'class 2'},'backgroundColor': 'red','color': 'white'},
                                        {'if': {'row_index': 2, 'column_id': 'class 2'},'backgroundColor': 'red','color': 'white'}, {'if': {'row_index': 3,'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 4, 'column_id': 'class 2'},'backgroundColor': 'orange','color': 'white'}, {'if': {'row_index': 5,'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 6, 'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 7,'column_id': 'class 2'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 8, 'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 9,'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 10,'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 11,'column_id': 'class 2'},'backgroundColor': 'blue','color': 'white'},

                                        {'if': {'row_index': 0, 'column_id': 'class 3'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 1,'column_id': 'class 3'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 2, 'column_id': 'class 3'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 3,'column_id': 'class 3'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 4, 'column_id': 'class 3'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 5,'column_id': 'class 3'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 6, 'column_id': 'class 3'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 7,'column_id': 'class 3'},'backgroundColor': 'white','color': 'black'},
                                    
                                        {'if': {'row_index': 0, 'column_id': 'class 4'},'backgroundColor': 'red','color': 'white'}, {'if': {'row_index': 1,'column_id': 'class 4'},'backgroundColor': 'blue','color': 'white'},
                                        {'if': {'row_index': 2, 'column_id': 'class 4'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 3,'column_id': 'class 4'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 4, 'column_id': 'class 4'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 5,'column_id': 'class 4'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 6, 'column_id': 'class 4'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 7,'column_id': 'class 4'},'backgroundColor': 'white','color': 'black'},

                                        {'if': {'row_index': 0, 'column_id': 'class 5'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 1,'column_id': 'class 5'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 2, 'column_id': 'class 5'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 3,'column_id': 'class 5'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 4, 'column_id': 'class 5'},'backgroundColor': 'white','color': 'black'}, {'if': {'row_index': 5,'column_id': 'class 5'},'backgroundColor': 'white','color': 'black'},

                                        {'if': {'row_index': 0, 'column_id': 'class 6'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 1,'column_id': 'class 6'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 2, 'column_id': 'class 6'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 3,'column_id': 'class 6'},'backgroundColor': 'white','color': 'black'},
                                        {'if': {'row_index': 4, 'column_id': 'class 6'},'backgroundColor': 'blue','color': 'white'}, {'if': {'row_index': 5,'column_id': 'class 6'},'backgroundColor': 'white','color': 'black'}]

    return df, lst_communities
