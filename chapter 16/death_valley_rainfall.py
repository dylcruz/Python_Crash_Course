from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

precipitation, dates = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        daily_precip = float(row[3])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        precipitation.append(daily_precip)

# Plot the daily precipitation
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, precipitation, color='blue')

# Format plot
ax.set_title("Daily Precipitation, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Precipitation (in)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()