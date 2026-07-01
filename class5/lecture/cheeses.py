cheeses = [['cheddar', 'edam', 'gouda'],
           ['edam', 'gouda', 'cheddar'],
           ['gouda', 'cheddar', 'edam']]

# Add a fourth friend's preferences
cheeseDan = ['mozzarella', 'cheddar', 'ricotta']
cheeses.append(cheeseDan)
print(cheeses)

# Dimensions
print(len(cheeses))        # 4 rows
print(len(cheeses[0]))     # 3 columns

# Print each row on its own line
for rank in cheeses:
    print(rank)

# Find all different cheeses
diffCheeses = []
for rank in cheeses:
    for cheese in rank:
        if cheese not in diffCheeses:
            diffCheeses.append(cheese)

print(diffCheeses)
