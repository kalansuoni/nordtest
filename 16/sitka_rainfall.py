from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Weather data file
path = Path("weather_data/sitka_weather_2021_full.csv")

with open(path, encoding="utf-8") as f:
    reader = csv.reader(f)

    header_row = next(reader)

    date_index = header_row.index("DATE")
    prcp_index = header_row.index("PRCP")

    dates = []
    rainfall = []

    for row in reader:
        try:
            current_date = datetime.strptime(
                row[date_index],
                "%Y-%m-%d"
            )

            precip = float(
                row[prcp_index]
            )

        except ValueError:
            print(
                f"Missing data for {row[date_index]}"
            )

        else:
            dates.append(current_date)
            rainfall.append(precip)

# Create graph
plt.style.use("seaborn-v0_8")

fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(
    dates,
    rainfall,
    color="blue"
)

# Format graph
ax.set_title(
    "Daily Rainfall in Sitka - 2021",
    fontsize=20
)

ax.set_xlabel("")
fig.autofmt_xdate()

ax.set_ylabel(
    "Precipitation (inches)",
    fontsize=14
)

ax.tick_params(
    axis="both",
    which="major",
    labelsize=12
)

plt.show()