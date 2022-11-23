import random

with open("english-adjectives.txt") as f:
    adjectives = f.read()

with open("animals.txt") as f:
    animals = f.read()

adjectives = adjectives.split('\n') #these adjectives were taken from https://gist.github.com/hugsy/8910dc78d208e40de42deb29e62df913
animals = animals.split('\n')

adjective = random.choice(adjectives)
animal = random.choice(animals)
number = random.choice((1,2,3,4,5,6,7,8,9,0))

print(adjective.capitalize()+animal.capitalize()+str(number))