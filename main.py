from dash import Dash,html,dcc,Input,Output
import plotly.express as px
import pandas as pd
import json
import plotly.graph_objects as go


df = pd.read_csv('rongrean.csv')
with open('data/Mapthailand.json') as json_file:
    geo_json= json.load(json_file)

dropdown = []
for i, j in zip(df.schools_province.tolist(), df.province.tolist()):
    dropdown.append({"label": i, "value": j})


app = Dash()

app.layout = [
    html.H1(children='School Dashboard'),
    html.H3(children='นักเรียนที่จบชั้นมัธยมศึกษาปีที่ 6 ปีการศึกษา 2566'),
    dcc.Dropdown(id='dropdown', placeholder='จังหวัด', options=dropdown),
    dcc.Graph(id='graph-content'),
    dcc.Graph(id='map')
]

@app.callback(
    Output('graph-content', 'figure'),
    Input('dropdown', 'value')
)
def update_graph(value):
    dff = df[df.province==value]
    sex = ['เพศ']
    male = dff['totalmale']
    female = dff['totalfemale']
    fig = go.Figure(
        data=[
            go.Bar(name='ชาย', x=sex, y=male, yaxis='y', offsetgroup=1),
            go.Bar(name='หญิง', x=sex, y=female, yaxis='y', offsetgroup=2, marker_color=px.colors.qualitative.Dark24[1])
        ],
        layout={
        'yaxis': {'title': 'จำนวนนักเรียน'}
        }
    )

    fig.update_layout(barmode='group')

    return fig

@app.callback(
    Output("map", "figure"),
    Input("dropdown", "value"),
)
def display_choropleth(dropdown):
    data = df
    if dropdown != None:
        data = df[df["province"] == dropdown]

    fig = px.choropleth_mapbox(
        data,
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

    return fig


if __name__ == '__main__':
    app.run(debug=True)