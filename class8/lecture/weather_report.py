"""Weather report for three cities."""

import csv
import numpy as np
import matplotlib.pyplot as plt


# --- Stage 1: load ---

def load_data(filename):
    rows = []
    with open(filename) as f:
        for row in csv.DictReader(f):
            row["day"] = int(row["day"])
            row["temp"] = float(row["temp"])
            row["rainfall"] = int(row["rainfall"])
            rows.append(row)
    return rows


# --- Stage 2: summarize ---

def city_summary(rows, city):
    temps = []
    total = 0
    rainy = 0
    for row in rows:
        if row["city"] == city:
            temps.append(row["temp"])
            total += row["rainfall"]
            if row["rainfall"] > 0:
                rainy += 1
    return np.mean(temps), total, rainy


# --- Stage 3: visualize ---

def plot_temps(rows, cities):
    for city in cities:
        days = []
        temps = []
        for row in rows:
            if row["city"] == city:
                days.append(row["day"])
                temps.append(row["temp"])
        plt.plot(days, temps, label=city)
    plt.xlabel("day")
    plt.ylabel("temperature (C)")
    plt.legend()
    plt.savefig("plot.png")


# --- Stage 4: report ---

def write_report(rows, cities, filename):
    with open(filename, "w") as f:
        for city in cities:
            t, rain, days = city_summary(rows, city)
            line = city + ": "
            line += str(round(t, 1)) + " C, "
            line += str(rain) + " mm, "
            line += "rainy days: " + str(days)
            f.write(line + "\n")


# --- main program ---

cities = ["Accra", "Kumasi", "Tamale"]
rows = load_data("weather.csv")
plot_temps(rows, cities)
write_report(rows, cities, "report.txt")
print("Report written!")
