# Napisz grę w zgadywanie liczby z przedziału od 1 do 10. Gracz powinien dostać
# 3 szanse. Po nieudanej próbie, gracz powinien otrzymać podpowiedź np.
# o parzystości zgadywanej liczby itp..

# import random
#
# number = random.randint(1, 10)
# guess = int(input("Zgadnij jaką liczbę mam na myśli (od 1 do 10): "))
#
# if guess == number:
#     print("Brawo, dokładnie taką liczbę miałem na myśli!")
# if guess != number:
#     print("Niestety, nie udało ci się odkryć liczby!")
# if guess != number and guess % 2 == 0:
#     print("Myślałem o liczbie PARZYSTEJ.")
# if guess != number and guess % 2 != 0:
#     print("Myślałem o liczbie NIEPARZYSTEJ.")

import random

number = random.randint(1, 10)
guess = int(input("Zgadnij jaką liczbę mam na myśli (od 1 do 10): "))

if guess == number:
    print("Brawo, dokładnie taką liczbę miałem na myśli!")
else:
    guess = int(input("Masz drugą szansę! Jaką liczbę mam na myśli (od 1 do 10): "))
    if guess != number and guess % 2 == 0:
            print("Liczba którą mam na myśli jest PARZYSTA")
    else:
        print("Liczba którą mam na myśli jest NIEPARZYSTA")
        if guess == number:
            print("Wow, udało ci się za drugim razem!")
    if guess != number:
        guess = int(input("Masz trzecią szansę! Jaką liczbę mam na myśli (od 1 do 10): "))
        if guess > 5:
            print("Liczba którą mam na myśli jest większa od 5!")
        if guess < 5:
            print("Liczba którą mam na myśli jest mniejsza od 5!")
        if guess == number:
            print("Hurra! Udało ci się za trzecim razem!")
        if guess != number:
            print("DAAAAAAAMN, nie udało ci się!")
                            # else:
                            # print("Co za pech! Miałem na myśli liczbę " + str(guess))




