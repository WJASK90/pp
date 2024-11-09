#zadanie 1 skrypt sprawdzający czy pierwiastek kwadratowy z liczby całkowitej pobranej od użytkownika jest także liczbą całkowitą


#zadanie 2 napisz skrypt wyznaczający ocenę jaką otrzyma student


#zadanie 3 - napisz gre w zgadywanie liczby od 1 do 10, gracz ma 3 szanse, po nieudanej probie nalezy sie podpowiedz np liczba do odgadnieca ma byc parzysta itd

import random

number = random.randint(1, 10)
guess = int(input("Uwaga, masz 3 szanse! Zgadnij jaką liczbę mam na myśli (od 1 do 10): "))

if guess == number:
    print("Brawo, dokładnie taką liczbę miałem na myśli!")
else:
    print("Niestety, myślałem o liczbie " + str(number) + ".")