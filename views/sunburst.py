import plotly.graph_objects as go

#this file creates the sunburst diagrams.



#the linked brushing with the other visuaizations with this sunburst file are obtained as follows:
#clicking on a datacell/network node gives an employee name, this name is used as input in this functions below.
#by using the corresponding department as start level of the sunburst, and coloring the employee in black the user gets 
#a quick and fast overview of the place of the employee within the company. 




#used input variables:
#input_name -> the employee member name obtained from table/network node
#first -> boolean whether whole sunburst needs to be created (first) or we have a specific input name

def executive_preprocessing(input_name):
    ########################################## PRE-PROCESSING ################################################### Sunburst 1) Hierarchy of the Executive Department
    # List of labels for the executive department
    labelsb = ['GAStech Board', 'Sangorge JR. (CEO)', 'Bramar', 'Vasco-Pais (ESA)', 'Barranco (CFO)', 'Ribera', 'Strum (COO)', 'L.Lagos', 'Campo-Corrente (CIO)', 'Pantanal']
    # List of parents for the executive department
    parentsb= ['', 'GAStech Board', 'Sangorge JR. (CEO)', 'Sangorge JR. (CEO)', 'Sangorge JR. (CEO)','Barranco (CFO)', 'Sangorge JR. (CEO)','Strum (COO)','Sangorge JR. (CEO)', 'Campo-Corrente (CIO)']
    # Members of the Executive department who have an assistant
    labels_board = ['Sangorge JR. (CEO)', 'Vasco-Pais (ESA)', 'Barranco (CFO)', 'Strum (COO)',  'Campo-Corrente (CIO)']
    # Assistants of the Executive department
    labels_board_ass = ['Bramar','Ribera', 'L.Lagos', 'Pantanal']

    # Color asssistants black and the executive department green
    colorse = ["green"]
    for p in labelsb[1:]:
        if p == input_name:
            colorse.append('black')
        else:
            if p in labels_board_ass:
                colorse.append("grey")
            else:
                colorse.append('green')
    return labelsb, parentsb, colorse

def departments_preprocessing(input_name):
    ############################################# PRE-PROCESSING ################################################ Sunburst 2) Hierarchy of all other departments
    # List of labels for all other departments
    labels = [
            'Board', 
            'Engineering', 'IT', 'Security', 'Facilities', 
            'Dedos', 'Onda', 'Balas', 'Nubarron', 'Haber', 'E. Orilla', 'V. Frente', 'Borrasca', 'Cazar', 'Azada', 'B. Frente', 'Calzas', 'Tempestad', 'K. Orilla',
            'Bergen', 'Forluniau', 'Baza', 'Calixto', 'Flecha', 'Alcazar',
            'Resumir', 'Lais', 'Fusil', 'V. Lagos', 'Osvaldo', 'Bodrogi', 'E. Vann', 'I. Vann', 'Cocinaro', 'Herrero', 'M.Mies', 'Ferro',
            'Ovan', 'Coginian', 'B. Hawelon', 'V. Morlun', 'Nant', 'Hafon', 'Awelon', 'Arpa', 'C. Hawelon', 'H. Mies', 'A. Morlun', 'Scozzesse', 'Morluniau']

    # List of parents for all other departments 
    parents = [
            '', 
            'Board','Board', 'Board', 'Board', 
            'Engineering', 'Engineering','Dedos', 'Dedos', 'Dedos', 'Onda', 'Onda','Onda','Onda', 'Balas', 'Nubarron', 'E. Orilla', 'V. Frente', 'Borrasca', 
            'IT', 'Bergen', 'Bergen','Bergen','Bergen', 'Bergen',
            'Security', 'Resumir','Resumir','Resumir','Resumir','Resumir','Resumir','Fusil', 'V. Lagos', 'Osvaldo', 'Bodrogi', 'E. Vann',
            'Facilities','Ovan','Ovan','Ovan','Ovan','Ovan','Coginian','Coginian',  'B. Hawelon','B. Hawelon', 'V. Morlun', 'Nant', 'Hafon']

    # List of labels for the engineering department
    labels_engineering = ['Engineering','Dedos', 'Onda', 'Balas', 'Nubarron', 'E. Orilla', 'V. Frente', 'Borrasca', 'Cazar', 'Azada', 'B. Frente', 'Calzas', 'Tempestad', 'K. Orilla']
    # List of labels for the IT department
    labels_it = ['IT', 'Bergen', 'Baza', 'Calixto', 'Flecha', 'Alcazar']
    # List of labels for the security department
    labels_security = ['Security', 'Resumir', 'Fusil', 'V. Lagos', 'Osvaldo', 'Bodrogi', 'E. Vann', 'I. Vann', 'Cocinaro', 'Herrero', 'M.Mies', 'Ferro']
    # List of labels for the facility department
    labels_facilities = ['Facilities', 'Ovan', 'Coginian', 'B. Hawelon', 'V. Morlun', 'Nant', 'Hafon', 'Awelon', 'Arpa', 'C. Hawelon', 'H. Mies', 'A. Morlun', 'Scozzesse', 'Morluniau']
    # List of labels for the assistents
    labels_assitents = ['Haber', 'Forluniau', 'Lais']
    # List of labels for the executive department
    labels_executive=['Board']

    # Color each department differently 
    # TODO: Check color choices 
    colors1 = []
    for p in labels:
        if p == input_name:
            colors1.append("black")
        else:
            if p in labels_engineering:
                colors1.append("red")
            elif p in labels_assitents:
                colors1.append("grey")
            elif p in labels_it:
                colors1.append("blue")
            elif p in labels_security:
                colors1.append("orange")
            elif p in labels_facilities:
                colors1.append("purple")
            elif p in labels_executive:
                colors1.append("green")

        
    return labels, parents, colors1


def sunburst_departments(input_name, first):
    dic_facilities = {'Carla Forluniau': 'IT', 'Cornelia Lais': 'Security',
    'Marin Onda': 'Engineering', 'Isande Borrasca': 'Engineering', 'Axel Calzas': 'Engineering', 'Kare Orilla': 'Engineering', 'Elsa Orilla': 'Engineering', 'Brand Tempestad': 'Engineering', 'Lars Azada': 'Engineering', 'Felix Balas': 'Engineering',
    'Lidelse Dedos': 'Engineering', 'Birgitta Frente': 'Engineering', 'Adra Nubarron': 'Engineering', 'Gustav Cazar': 'Engineering', 'Vira Frente': 'Engineering',  'Bertrand Ovan': 'Facilities', 'Emile Arpa': 'Facilities', 'Varro Awelon': 'Facilities', 'Dante Coginian': 'Facilities', 'Albina Hafon': 'Facilities',
    'Benito Hawelon': 'Facilities', 'Claudio Hawelon': 'Facilities', 'Valeria Morlun': 'Facilities', 'Adan Morlun': 'Facilities', 'Cecilia Morluniau': 'Facilities', 'Irene Nant': 'Facilities', 'Linnea Bergen': 'IT',
    'Lucas Alcazar': 'IT', 'Isak Baza': 'IT', 'Nils Calixto': 'IT', 'Sven Flecha': 'IT', 'Kanon Herrero': 'Security', 'Varja Lagos': 'Security', 'Stenig Fusil': 'Security', 'Hennie Osvaldo': 'Security',
    'Isia Vann': 'Security', 'Edvard Vann': 'Security', 'Felix Resumir': 'Security', 'Loreto Bodrogi': 'Security', 'Hideki Cocinaro': 'Security', 'Inga Ferro': 'Security', 'Ruscella Mies': 'Security',
    'Henk Mies': 'Facilities', 'Dylan Scozzese': 'Facilities', 'Minke Mies': 'Security', 'Ruscella Mies Haber':'Engineering'}

   
    
    dups = {'Varja Lagos': 'V. Lagos', 'Edvard Vann':'E. Vann', 'Isia Vann':'I. Vann', 'Minke Mies':'M.Mies',
       'Benito Hawelon':'B. Hawelon', 'Valeria Morlun':'V. Morlun', 'Claudio Hawelon':'C. Hawelon', 'Henk Mies':'H. Mies',
       'Adan Morlun':'A. Morlun', 'Birgitta Frente':'B. Frente', 'Vira Frente':'V. Frente', 'Ruscella Mies Haber':'Haber', 
       'Ruscella Mies':'Haber', 'Elsa Orilla':'E. Orilla', 'Kare Orilla':'K. Orilla'}
    

    if not first:
        if input_name in dups.keys():
            name_in = dups[input_name]
        else:
            name_in = input_name.split()[1]
        fac = dic_facilities[input_name]
    else:
        name_in = ''
               
    ################################# CREATING PLOT ################################################################### Sunburst 2) All other departments
    labels, parents, colors1 = departments_preprocessing(name_in)
    layout = go.Layout(
        margin = go.layout.Margin(
            l=0,
            r=0,
            b=0,
            t=0,
            pad=0,
        ),    
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    )
    if first:
        fig = go.Figure(
            go.Sunburst(
            labels=labels,
            parents=parents,
            marker=dict(colors=colors1),
                maxdepth=4,
                insidetextorientation='tangential'

            ),
            layout = layout,
        )
    else:
        fig = go.Figure(
            go.Sunburst(
            labels=labels,
            parents=parents,
            level = fac,
            marker=dict(colors=colors1),
                maxdepth=4,
                insidetextorientation='tangential'

            ),
            layout = layout,
        )

    return fig


    ################################ CREATING PLOT ################################################################### Sunburst 1) Only the executive board
def sunburst_executive(input_name, first):
    executives = {'Sten Sanjorge Jr.': 'Sangorge JR. (CEO)', 'Sten Sanjorge Jr': 'Sangorge JR. (CEO)', 'Sten Sanjorge Jr (tethys)': 'Sangorge JR. (CEO)', 'Willem Vasco-Pais': 'Vasco-Pais (ESA)', 'Ingrid Barranco': 'Barranco (CFO)',
                  'Ada Campo-Corrente': 'Campo-Corrente (CIO)', 'Orhan Strum': 'Strum (COO)', 'Mat Bramar': 'Bramar', 'Anda Ribera': 'Ribera','Linda Lagos': 'L.Lagos', "Rachel Pantanal": "Pantanal"}
	
    if not first:
        name_in = executives[input_name]
    else:
        name_in = ''
        
    labelsb, parentsb, colorse = executive_preprocessing(name_in)
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

    fig2 = go.Figure(
        go.Sunburst(
        labels=labelsb,
        parents=parentsb,
        marker=dict(colors=colorse),
        insidetextorientation='tangential',
        maxdepth=4,

        ),
        layout=layout,
    )
    return fig2
