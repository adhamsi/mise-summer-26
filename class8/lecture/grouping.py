import csv
import matplotlib.pyplot as plt

rows = []
with open("weather.csv") as f:
    for row in csv.DictReader(f):
        row["rainfall"] = int(row["rainfall"])
        rows.append(row)

# Grouping: total rainfall per city
totals = {}
for row in rows:
    c = row["city"]
    r = row["rainfall"]
    totals[c] = totals.get(c, 0) + r

print(totals["Kumasi"])  # 158

# A dictionary of totals is one plt.bar away from a chart
cities = list(totals.keys())
values = list(totals.values())

plt.bar(cities, values)
plt.ylabel("total rainfall (mm)")
plt.savefig("plot.png")
