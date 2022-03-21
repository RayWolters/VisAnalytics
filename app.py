import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
app = dash.Dash(__name__, suppress_callback_exceptions=True)
df_email = pd.read_csv("data/email headers.csv", encoding="cp1252")
fig = px.histogram(df_email, x=df_email["Subject"])

app.layout = html.Div(
    children = [
        html.H1(
            children="Visual Analytics - GROUP 30 - Dashboard",
            className="header-title",
        ),
        html.P(
            children = "A simple plot to test this",
        ),
        dcc.Graph(
            figure = fig,
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)