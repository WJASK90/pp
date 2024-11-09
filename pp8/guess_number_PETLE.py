#gra toczy sie dopoki nie zostanie odganieta liczba

import random

counter = 1
number = random.randint(1, 10)
guess = int(input("Zgadnij jaką liczbę mam na myśli (1-10): "))
# te += 1 to inkrementacja o 1!!!
while guess != number:
    guess = int(input("Nie, to nie ta. Spróbuj jeszcze raz: "))
    counter += 1

print("Brawo! Udało Ci się już za " + str(counter) + " razem.")