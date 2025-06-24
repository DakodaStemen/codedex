# ----- Dictionary 

artwork = {
    "name": "Warwick Castle: The East Front",
    "artist": "Giovanni Antonio Canal",
    "date": 1752    
}

"""
print(artwork["name"])
print(artwork["artist"])
print(artwork["date"])
"""

# Methods
print('Keys:', artwork.keys())
print('Values:', artwork.values())
print('Items:', artwork.items())



# ----- Sets 

my_fruits = {"Strawberries", "Blueberries", "Bananas", "Grapes"}

bff_fruits = {"Grapes", "Apples", "Cherries"}

union_fruits = my_fruits.union(bff_fruits)
intersection_fruits = my_fruits.intersection(bff_fruits)
difference_fruits = my_fruits.difference(bff_fruits)

print(union_fruits)
print(intersection_fruits)
print(difference_fruits)