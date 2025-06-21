# solar_system.py

from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

if random_planet == 'Mercury':
    r = 2440
elif random_planet == 'Venus':
    r = 6052
elif random_planet == 'Earth':
    r = 6371
elif random_planet == 'Mars':
    r = 3390
elif random_planet == 'Saturn':
    r = 58232
else:
    r = "Oops! An error occured."

area = float(4 * pi * r**2)     # ':,' add commas to output | '.4f' = fixed at 4 decimal
print(f"{random_planet} has a radius of {r}. This means the area is {area:,.4f}")
