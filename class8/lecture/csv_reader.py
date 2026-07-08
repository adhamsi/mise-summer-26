import csv

with open("weather.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Each row is a list of strings:
# ['day', 'city', 'temp', 'rainfall']
# ['1', 'Accra', '28.1', '0']
# ...
# Convert with float(row[2]), int(row[0]), etc.
