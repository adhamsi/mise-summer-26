import csv

# DictReader uses the header row as keys -- no column counting needed
with open("weather.csv") as f:
    for row in csv.DictReader(f):
        print(row["city"], row["temp"])

# Values are still strings -- convert with float(row["temp"])
