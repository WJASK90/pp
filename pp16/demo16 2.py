# import math as m
#
# print(m.pi)
# print(math.pi) #nie dziala bo obowiozuje tutaj nazwa m

# from math import pi as PI
#
# print(PI)


import math
print(dir(math)) #dostajemy liste ze wszystkim atrybutami i modułami

import random

print(random.randint(1,3))

print(random.random()) #najbardziej klasyczna funkcja, wylosuje nam liczbe typu float od 0.0 do 1.0 czyli:
# losuje liczbe z przedialu [0.0, 1.0)

from random import random, seed #seed, ziarno czyli losowosc generatora liczb pseudolosowych

seed(1)

for i in range(5):
    print(random())

from random import choice, sample

lst = [i for i in range (1,11)]

print(choice(lst)) #wybiera jedną liczbę ze zbioru



