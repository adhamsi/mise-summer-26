import csv

# Load and convert types once
rows = []
with open("weather.csv") as f:
    for row in csv.DictReader(f):
        row["day"] = int(row["day"])
        row["temp"] = float(row["temp"])
        row["rainfall"] = int(row["rainfall"])
        rows.append(row)

# Filter: keep only Accra rows
accra = []
for row in rows:
    if row["city"] == "Accra":
        accra.append(row)

print(len(accra))  # 14

# Filter: keep only rainy rows (rainfall > 0)
rainy = []
for row in rows:
    if row["rainfall"] > 0:
        rainy.append(row)

print(len(rainy))  # 17
