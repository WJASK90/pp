# Korzystając z odpowiednich modułów napisz skrypt realizujący następujące
# zadania:
# • wyświetl informacje o procesorze komputera,
# • wylosuj 3 niepowtarzalne liczby ze zbioru 1-10,
# • wyznacz sinus 90 stopni.

import platform
from random import sample
import math

#info o procesorze
print(platform.processor())

#losujemy 3 niepowtarzalne liczby ze zbioru 1-10)
def range_of_numbers():
    number = [i for i in range (1,11)]
    three_numbers = sample(number, k=3)
    return three_numbers

print(range_of_numbers())

#wyznaczam sinus 90 stopni

angle = math.radians(90)
sinus = math.sin(angle)

print(sinus)