from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Path to file
path = Path('weather_data/san_francisco_weather_2021.csv')

with open(path, encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Find indexes
    date_index = header_row.index("DATE")
    tmax_index = header_row.index("TMAX")
    tmin_index = header_row.index("TMIN")

    dates, highs, lows = [], [], []

    for row in reader:
        try:
            current_date = datetime.strptime(
                row[date_index], "%Y-%m-%d"
            )
            high = int(row[tmax_index])
            low = int(row[tmin_index])
        except ValueError:
            print(f"Missing data for {row[date_index]}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the temperatures
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(dates, highs, color='red', alpha=0.6, label='High')
ax.plot(dates, lows, color='blue', alpha=0.6, label='Low')

ax.fill_between(dates, highs, lows,
                facecolor='blue', alpha=0.1)

ax.set_title(
    "Daily High and Low Temperatures, San Francisco (2021)",
    fontsize=20
)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()

ax.set_ylabel("Temperature (°F)", fontsize=16)
ax.tick_params(labelsize=12)

ax.legend()

plt.show()