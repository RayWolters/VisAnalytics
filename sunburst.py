import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go

def executive_preprocessing():
    ########################################## PRE-PROCESSING ################################################### Sunburst 1) Hierarchy of the Executive Department
    # List of labels for the executive department
    labelsb = ['GAStech Board', 'Sangorge JR. (CEO)', 'Bramar', 'Vasco-Pais (ESA)', 'Barranco (CFO)', 'Ribera', 'Strum (COO)', 'L.Lagos', 'Campo-Corrente (CIO)', 'Pantanal']
    # List of parents for the executive department
    parentsb= ['', 'GAStech Board', 'Sangorge JR. (CEO)', 'Sangorge JR. (CEO)', 'Sangorge JR. (CEO)','Barranco (CFO)', 'Sangorge JR. (CEO)','Strum (COO)','Sangorge JR. (CEO)']
    # Members of the Executive department who have an assistant
    labels_board = ['Sangorge JR. (CEO)', 'Vasco-Pais (ESA)', 'Barranco (CFO)', 'Strum (COO)',  'Campo-Corrente (CIO)']
    # Assistants of the Executive department
    labels_board_ass = ['Bramar','Ribera', 'L.Lagos', 'Pantanal']

    # Color asssistants black and the executive department green
    colorse = ["green"]
    for p in labelsb[1:]:
        if p in labels_board_ass:
            colorse.append("black")
        else:
            colorse.append('green')
    return labelsb, parentsb, colorse

def departments_preprocessing():
    ############################################# PRE-PROCESSING ################################################ Sunburst 2) Hierarchy of all other departments
    # List of labels for all other departments
    labels = ['GAStech',
            'Board', 
            'Engineering', 'IT', 'Security', 'Facilities', 
            'Dedos', 'Onda', 'Balas', 'Nubarron', 'Haber', 'E. Orilla', 'V. Frente', 'Borrasca', 'Cazar', 'Azada', 'B. Frente', 'Calzas', 'Tempestad', 'K. Orilla',
            'Bergen', 'Forluniau', 'Baza', 'Calixto', 'Flecha', 'Alcazar',
            'Resumir', 'Lais', 'Fusil', 'V. Lagos', 'Osvaldo', 'Bodrogi', 'E. Vann', 'I. Vann', 'Cocinaro', 'Herrero', 'M.Mies', 'Ferro',
            'Ovan', 'Coginian', 'B. Hawelon', 'V. Morlun', 'Nant', 'Hafon', 'Awelon', 'Arpa', 'C. Hawelon', 'H. Mies', 'A. Morlun', 'Scozzesse', 'Morluniau']

    # List of parents for all other departments 
    parents = ['', 
            'GAStech', 
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
        if p == 'GAStech':
            colors1.append("white")
        if p in labels_engineering:
            colors1.append("red")
        elif p in labels_assitents:
            colors1.append("black")
        elif p in labels_it:
            colors1.append("blue")
        elif p in labels_security:
            colors1.append("orange")
        elif p in labels_facilities:
            colors1.append("purple")
        elif p in labels_executive:
            colors1.append("green")
    return labels, parents, colors1

def sunburst_executive():
    ################################# CREATING PLOT ################################################################### Sunburst 2) All other departments
    labels, parents, colors1 = departments_preprocessing()
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
    fig = go.Figure(
        go.Sunburst(
        labels=labels,
        parents=parents,
        marker=dict(colors=colors1),
            maxdepth=3,
            insidetextorientation='tangential'

        ),
        layout = layout,
    )
    return fig

    ################################ CREATING PLOT ################################################################### Sunburst 1) Only the executive board
def sunburst_departments():
    labelsb, parentsb, colorse = executive_preprocessing()
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
        insidetextorientation='tangential'
        ),
        layout=layout,
    )
    return fig2
