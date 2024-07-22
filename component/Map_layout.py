from dash import Dash,html,dcc,Input,Output
import plotly.express as px
import json
import pandas as pd

df = pd.read_csv('rongrean.csv')
with open('data/Mapthailand.json') as json_file:
    geo_json= json.load(json_file)

def create_map(app:Dash):
    fig = px.choropleth_mapbox(
        df,
        geojson=geo_json,
        featureidkey="properties.name",
        locations="province",
        color="totalstd",
        color_continuous_scale="sunsetdark",
        hover_name="schools_province",
        mapbox_style="open-street-map",
        center={"lat": 14.11, "lon": 100.35},
        zoom=5,
        labels={
            "province": "Province",
            "totalstd": "นักเรียนทั้งหมด",
        },
    )

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return html.Div(dcc.Graph(figure=fig))
