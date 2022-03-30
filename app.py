import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
from sunburst import sunburst_departments, sunburst_executive
app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# test df
df_email = pd.read_csv("data/email headers.csv", encoding="cp1252")

# TODO: Fix styling 
app.layout = html.Div(
    children = [
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
                ], width = {'size': 2}, className="border bl border-top-0 border-bottom-0"),
                dbc.Col(
                    [
                        html.H2("Plot", className = "text-center bg-danger text-white p-0 mt-0 ml-0 mr-0"),
                    ], width = {'size': 6}, className="border bl border-top-0 border-bottom-0",
                    ),
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.H2("Plot", className = "text-center bg-danger text-white p-0 mt-0 ml-0 mr-0"),
                                        dcc.Graph(figure=sunburst_executive(), className = "h-75"),
                                    ], width = {'size': 6},
                                ),
                                dbc.Col(
                                    [
                                        html.H2("Plot", className = "text-center bg-danger text-white p-0 mt-0 ml-0 mr-0"),
                                        dcc.Graph(figure=sunburst_departments(), className = "h-75"),
                                    ], width = {'size': 6},
                                ),
                            ], className = "g-0 h-25",
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.H2("Plot", className = "text-center bg-danger text-white p-0 mt-0 ml-0 mr-0"),
                                        dcc.Graph(figure=sunburst_departments(), className = "h-75"),
                                    ], 
                                ),
                            ], className = "g-0 h-75",
                        ),
                    ], width = {'size': 4}, className = "h-100"
                ),
            ], className = "vh-100 g-0",
        ),
    ],
)

if __name__ == "__main__":
    app.run_server(debug=True)