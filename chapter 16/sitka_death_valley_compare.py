from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


def get_high_lows(weather_data):
    """Generates plotting data from a CSV for daily high and low temperatures"""
    path = Path(weather_data)
    lines = path.read_text(encoding="utf-8").splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    # Extract dates, high, and low temperatures.
    dates, highs, lows = [], [], []
    date_idx = header_row.index("DATE")
    high_idx = header_row.index("TMAX")
    low_idx = header_row.index("TMIN")

    for row in reader:
        current_date = datetime.strptime(row[date_idx], "%Y-%m-%d")
        try:
            high = int(row[high_idx])
            low = int(row[low_idx])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    return dates, highs, lows


dv_dates, dv_highs, dv_lows = get_high_lows("weather_data/death_valley_2021_full.csv")
si_dates, si_highs, si_lows = get_high_lows("weather_data/sitka_weather_2021_full.csv")

# Plot the high and low temperatures.
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dv_dates, dv_highs, color="red")
ax.plot(dv_dates, dv_lows, color="blue")
ax.plot(si_dates, si_highs, color="red")
ax.plot(si_dates, si_lows, color="blue")
ax.fill_between(dv_dates, dv_highs, dv_lows, facecolor="blue", alpha=0.1)
ax.fill_between(si_dates, si_highs, si_lows, facecolor="blue", alpha=0.1)

# Format plot
ax.set_title(
    "Daily High and Low Temperatures | Death Valley, CA & Sitka, AK | 2021", fontsize=14
)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
