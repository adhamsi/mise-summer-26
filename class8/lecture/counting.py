import csv

rows = []
with open("weather.csv") as f:
    for row in csv.DictReader(f):
        row["rainfall"] = int(row["rainfall"])
        rows.append(row)

rainy = [row for row in rows if row["rainfall"] > 0]

# Counting: how many rainy days did each city have?
counts = {}
for row in rainy:
    c = row["city"]
    counts[c] = counts.get(c, 0) + 1

print(counts)
# {'Accra': 7, 'Kumasi': 9, 'Tamale': 1}
