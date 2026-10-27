from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path(
    "weather_data/sitka_weather_2021_simple.csv"
)

dates, highs, lows = [], [], []

with open(path, encoding="utf-8") as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        current_date = datetime.strptime(
            row[2], "%Y-%m-%d"
        )

        high = int(row[4])
        low = int(row[5])

        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use("seaborn-v0_8")

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    dates,
    highs,
    color="red",
    alpha=0.5
)

ax.plot(
    dates,
    lows,
    color="blue",
    alpha=0.5
)

ax.fill_between(
    dates,
    highs,
    lows,
    facecolor="blue",
    alpha=0.1
)

ax.set_title(
    "Sitka Daily High and Low Temperatures, 2021",
    fontsize=20
)

ax.set_xlabel("")
fig.autofmt_xdate()

ax.set_ylabel(
    "Temperature (°F)",
    fontsize=14
)

# Same scale for comparison
ax.set_ylim(0, 130)

plt.show()