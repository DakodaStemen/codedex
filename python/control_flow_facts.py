# random_fact.py 💖
import random

def random_fact(number: int) -> str:
    if number == 0:
        return 'Flamingos turn pink from eating shrimp.'
    elif number == 1:
        return 'The only food that doesn\'t spoil is honey.'
    elif number == 2:
        return 'Shrimp can only swim backwards.'
    elif number == 3:
        return 'A taste bud\'s life span is about 10 days.'
    elif number == 4:
        return 'It is impossible to sneeze while sleeping.'
    else:
        return 'It is illegal to sing off-key in North Carolina.'

number = random.randint(0, 5)
print(random_fact(number))

