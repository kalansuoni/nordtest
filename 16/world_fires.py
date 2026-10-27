from pathlib import Path
import csv

import plotly.express as px

# Read the fire data.
path = Path('world_fires_1_day.csv')

with open(path, encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print(header_row)

    lat_index = header_row.index('latitude')
    lon_index = header_row.index('longitude')
    bright_index = header_row.index('brightness')

    lats, lons, brights = [], [], []

    for row in reader:
        try:
            lat = float(row[lat_index])
            lon = float(row[lon_index])
            bright = float(row[bright_index])
        except ValueError:
            continue
        else:
            lats.append(lat)
            lons.append(lon)
            brights.append(bright)

# Create the map.
title = 'Global Fires - 1 Day'

fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=brights,
    color=brights,
    title=title,
    color_continuous_scale='Hot',
    labels={'color': 'Brightness'},
    projection='natural earth',
)

fig.update_layout(
    title_font_size=24
)

fig.show()