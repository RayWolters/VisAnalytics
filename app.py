import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# test df
df_email = pd.read_csv("data/email headers.csv", encoding="cp1252")

# test figure
fig = px.histogram(df_email, x=df_email["Subject"])

import plotly.graph_objects as go

labelsb = ['GAStech Board', 'Sangorge JR. (CEO)', 'Bramar', 'Vasco-Pais (ESA)', 'Barranco (CFO)', 'Ribera', 'Strum (COO)', 'L.Lagos', 'Campo-Corrente (CIO)', 'Pantanal']
parentsb= ['', 'GAStech Board', 'Sangorge JR. (CEO)', 'Sangorge JR. (CEO)', 'Sangorge JR. (CEO)','Barranco (CFO)', 'Sangorge JR. (CEO)','Strum (COO)','Sangorge JR. (CEO)']
labels_board = ['Sangorge JR. (CEO)', 'Vasco-Pais (ESA)', 'Barranco (CFO)', 'Strum (COO)',  'Campo-Corrente (CIO)']
labels_board_ass = ['Bramar','Ribera', 'L.Lagos', 'Pantanal']

colorse = ["green"]
for p in labelsb[1:]:
    if p in labels_board_ass:
        colorse.append("black")
    else:
        colorse.append('green')
        
labels = ['GAStech',
          'Board', 
          'Engineering', 'IT', 'Security', 'Facilities', 
          'Dedos', 'Onda', 'Balas', 'Nubarron', 'Haber', 'E. Orilla', 'V. Frente', 'Borrasca', 'Cazar', 'Azada', 'B. Frente', 'Calzas', 'Tempestad', 'K. Orilla',
         'Bergen', 'Forluniau', 'Baza', 'Calixto', 'Flecha', 'Alcazar',
         'Resumir', 'Lais', 'Fusil', 'V. Lagos', 'Osvaldo', 'Bodrogi', 'E. Vann', 'I. Vann', 'Cocinaro', 'Herrero', 'M.Mies', 'Ferro',
         'Ovan', 'Coginian', 'B. Hawelon', 'V. Morlun', 'Nant', 'Hafon', 'Awelon', 'Arpa', 'C. Hawelon', 'H. Mies', 'A. Morlun', 'Scozzesse', 'Morluniau']

parents = ['', 
           'GAStech', 
           'Board','Board', 'Board', 'Board', 
           'Engineering', 'Engineering','Dedos', 'Dedos', 'Dedos', 'Onda', 'Onda','Onda','Onda', 'Balas', 'Nubarron', 'E. Orilla', 'V. Frente', 'Borrasca', 
          'IT', 'Bergen', 'Bergen','Bergen','Bergen', 'Bergen',
          'Security', 'Resumir','Resumir','Resumir','Resumir','Resumir','Resumir','Fusil', 'V. Lagos', 'Osvaldo', 'Bodrogi', 'E. Vann',
          'Facilities','Ovan','Ovan','Ovan','Ovan','Ovan','Coginian','Coginian',  'B. Hawelon','B. Hawelon', 'V. Morlun', 'Nant', 'Hafon']

labels_engineering = ['Engineering','Dedos', 'Onda', 'Balas', 'Nubarron', 'E. Orilla', 'V. Frente', 'Borrasca', 'Cazar', 'Azada', 'B. Frente', 'Calzas', 'Tempestad', 'K. Orilla']
labels_it = ['IT', 'Bergen', 'Baza', 'Calixto', 'Flecha', 'Alcazar']
labels_security = ['Security', 'Resumir', 'Fusil', 'V. Lagos', 'Osvaldo', 'Bodrogi', 'E. Vann', 'I. Vann', 'Cocinaro', 'Herrero', 'M.Mies', 'Ferro']
labels_facilities = ['Facilities', 'Ovan', 'Coginian', 'B. Hawelon', 'V. Morlun', 'Nant', 'Hafon', 'Awelon', 'Arpa', 'C. Hawelon', 'H. Mies', 'A. Morlun', 'Scozzesse', 'Morluniau']
labels_assitents = ['Haber', 'Forluniau', 'Lais']
labels_executive=['Board']

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

fig = go.Figure(
    go.Sunburst(
     labels=labels,
     parents=parents,
    marker=dict(colors=colors1),
        maxdepth=3,
        insidetextorientation='horizontal'

    )
)

# fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))
# fig.update_layout(uniformtext=dict(minsize=10, mode='hide'))
fig2 = go.Figure(
    go.Sunburst(
     labels=labelsb,
     parents=parentsb,
    marker=dict(colors=colorse),
    
    insidetextorientation='tangential'
    )
)

# fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

app.layout = html.Div(
    [
        # Navbar with title of dashboard
        dbc.Navbar([
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col([
                                    html.H1("Visual Analytics Group 30"),
                                ],
                            ),
                        ],
                    ),
                ],
            # Put title in the middle
            className = "justify-content-center g-0",
            ), 
        ], className = "bg-dark text-white"),
            dbc.Row([
                dbc.Col([
                    html.H2("Settings", className="text-center bg-danger text-white p-0 mt-0 ml-0 mr-0"),
                    dcc.Dropdown(className = "m-4"),
                    dcc.Dropdown(className = "m-4"),
                ], width = {'size': 3}, className="border bl border-top-0 border-bottom-0"),
                dbc.Col(
                    [
                        html.H2("Plot", className = "text-center bg-danger text-white p-0 mt-0 ml-0 mr-0"),
                        dcc.Graph(figure=fig, className = "m-4"),
                        html.H2("Plot", className = "text-center bg-danger text-white p-0 mt-0 ml-0 mr-1"),
                        dcc.Graph(figure=fig2, className = "m-5"),
                    ]
                    ),
            ],
        className="vh-100 g-0",
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)