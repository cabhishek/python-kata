places = ["times square", "white house", "machu picchu"]
cities = ["New York", "DC", "Peru"]

print(list(zip(places, cities)))

from itertools import zip_longest

# Unequal list size or missing values
places = ["times square", "white house"]
cities = ["New York", "DC", "Peru"]

print(list(zip_longest(places, cities)))
