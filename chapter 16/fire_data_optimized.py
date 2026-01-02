import csv
import plotly.express as px
from pathlib import Path

# Define path using Pathlib for cross-platform compatibility
file_path = Path("fire_data/world_fires_7_day.csv")

# Use a context manager ('with open...') to handle file opening/closing safely
# 'encoding="utf-8"' ensures we handle text characters correctly
with file_path.open(encoding="utf-8") as f:
    reader = csv.reader(f)
    headers = next(reader)

    # Retrieve indexes dynamically
    try:
        lats_idx = headers.index("latitude")
        lons_idx = headers.index("longitude")
        brights_idx = headers.index("brightness")
    except ValueError as e:
        print(f"Error finding required headers: {e}")
        exit()

    lats, lons, brights = [], [], []

    # Iterate row by row (streaming) instead of loading everything at once
    for row in reader:
        try:
            # Convert all numerical data immediately
            lat = float(row[lats_idx])
            lon = float(row[lons_idx])
            bright = float(row[brights_idx])
        except ValueError:
            # Skip rows with missing or malformed data
            print(f"Skipping malformed row: {row}")
            continue

        lats.append(lat)
        lons.append(lon)
        brights.append(bright)

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
