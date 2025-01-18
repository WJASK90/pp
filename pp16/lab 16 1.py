# Korzystając z odpowiednich modułów napisz skrypt realizujący następujące
# zadania:
# • wyświetl informacje o procesorze komputera,
# • wylosuj 3 niepowtarzalne liczby ze zbioru 1-10,
# • wyznacz sinus 90 stopni.

import platform
from random import sample
import math

#info o procesorze
print("Procesor:", platform.processor())

#losujemy 3 niepowtarzalne liczby ze zbioru 1-10)

print("Losowanie:", random.sample(range(1,11), k=3))

#wyznaczam sinus 90 stopni

print("Sinus 90 stopni:", math.sin(math.radians(90)))


