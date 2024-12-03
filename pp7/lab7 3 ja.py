# Napisz grę w zgadywanie liczby z przedziału od 1 do 10. Gracz powinien dostać
# 3 szanse. Po nieudanej próbie, gracz powinien otrzymać podpowiedź np.
# o parzystości zgadywanej liczby itp..

import random

number = random.randint(1, 10)
guess = int(input("Zgadnij jaką liczbę mam na myśli (od 1 do 10): "))

if guess == number:
    print("Brawo, dokładnie taką liczbę miałem na myśli!")
if guess != number and guess % 2 == 0:
    print("Niestety, myślałem o liczbie PARZYSTEJ.")
if guess != number and guess % 2 != 0:
    print("Niestety, myślałem o liczbie NIEPARZYSTEJ.")