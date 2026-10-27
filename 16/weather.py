from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Choose the file you want to graph
path = Path('weather_data/sitka_weather_2021_full.csv')

with open(path, encoding='utf-8') as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Automatically find the indexes
    date_idx = header_row.index('DATE')
    name_idx = header_row.index('NAME')
    tmax_idx = header_row.index('TMAX')
    tmin_idx = header_row.index('TMIN')

    dates, highs, lows = [], [], []
    station_name = None

    for row in reader:
        try:
            current_date = datetime.strptime(
                row[date_idx], '%Y-%m-%d'
            )
            high = int(row[tmax_idx])
            low = int(row[tmin_idx])

            if station_name is None:
                station_name = row[name_idx]

        except ValueError:
            print(f"Missing data for {row[date_idx]}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Create graph
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(dates, highs, color='red', alpha=0.6, label='High')
ax.plot(dates, lows, color='blue', alpha=0.6, label='Low')

ax.fill_between(
    dates,
    highs,
    lows,
    facecolor='blue',
    alpha=0.1
)

ax.set_title(
    f"Daily High and Low Temperatures\n{station_name}",
    fontsize=20
)

ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()

ax.set_ylabel('Temperature (°F)', fontsize=16)
ax.tick_params(labelsize=12)

ax.legend()

plt.show()