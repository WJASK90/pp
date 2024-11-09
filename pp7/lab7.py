#zadanie 1 skrypt sprawdzający czy pierwiastek kwadratowy z liczby całkowitej pobranej od użytkownika jest także liczbą całkowitą


#zadanie 2 napisz skrypt wyznaczający ocenę jaką otrzyma student
punktacja = int(input("Otrzymane punkty: "))
print("Ocena to: ")

if punktacja >= 95:
    print(" - Bardzo dobra! Czyli 5, wow!")

if punktacja == 95:
    print(" - Ponad dobra! Czyli 4,5")

if punktacja > 84:
    print(" - Ponad dobra! Czyli 4,5")

if punktacja == 84:
    print(" - Dobra! Czyli 4")

if punktacja >= 70:
    print(" - Dobra! Czyli 4")

if punktacja > 60:
    print(" - Dość dobra! Czyli 3,5")

if punktacja < 70:
    print(" - Dość dobra! Czyli 3,5")

if punktacja == 60:
    print(" - Dostateczna! Czyli 3")

if punktacja > 50:
    print(" - Dostateczna! Czyli 3")

if punktacja <= 50:
    print(" - Niedostateczna! Czyli 2")

#zadanie 3 - napisz gre w zgadywanie liczby od 1 do 10, gracz ma 3 szanse, po nieudanej probie nalezy sie podpowiedz np liczba do odgadnieca ma byc parzysta itd

import random

number = random.randint(1, 10)
guess = int(input("Zgadnij jaką liczbę mam na myśli (od 1 do 10): "))

if guess == number:
    print("Brawo, dokładnie taką liczbę miałem na myśli!")
else:
    print("Niestety, myślałem o liczbie " + str(number) + ".")