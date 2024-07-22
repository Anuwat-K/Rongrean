from dash import Dash,html,dash_table

from . import rongrean_dropdown,bar_chart
import pandas as pd

def create_layout(app:Dash) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
        ]
    )