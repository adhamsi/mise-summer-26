import csv
import numpy as np

temps = []
with open("weather.csv") as f:
    for row in csv.DictReader(f):
        t = float(row["temp"])
        temps.append(t)

arr = np.array(temps)

print(round(np.mean(arr), 1))  # 30.0
print(np.max(arr))             # 34.1
