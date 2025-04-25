import random

# First roll
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

# Keep rolling until snake eyes (1 + 1 = 2)
while total != 2:
    print("Nope")
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

print("Snake eyes!")
