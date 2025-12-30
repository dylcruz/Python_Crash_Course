import csv
import plotly.express as px
from pathlib import Path

# Open and read CSV file
fire_data = Path("fire_data/world_fires_7_day.csv")
contents = fire_data.read_text().splitlines()
all_fires = csv.reader(contents)

# Prep for parsing data
headers = next(all_fires)
lats, lons, brights = [], [], []
lats_idx = headers.index("latitude")
lons_idx = headers.index("longitude")
brights_idx = headers.index("brightness")

# Parse fire data
for fire in all_fires:
    lats.append(fire[lats_idx])
    lons.append(fire[lons_idx])
    brights.append(float(fire[brights_idx]))

# Plot data
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=brights,
    title="Global Fires - 7 Days",
    color=brights,
    color_continuous_scale="Viridis",
    labels={"color": "Brightness"},
    projection="natural earth",
)

fig.show()
