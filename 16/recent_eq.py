from pathlib import Path
import json

import plotly.express as px

path = Path('eq_data/all_month.geojson')

contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

title = all_eq_data['metadata']['title']

all_eq_dicts = all_eq_data['features']

mags = []
lons = []
lats = []
eq_titles = []

for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']

    if mag is None or mag < 0:
        continue

    mags.append(mag)
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])

fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    color=mags,
    hover_name=eq_titles,
    title=title,
    projection='natural earth',
    color_continuous_scale='Viridis',
    labels={'color': 'Magnitude'},
)

fig.show()