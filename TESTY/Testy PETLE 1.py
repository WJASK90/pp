# PETLA "WHILE"
# wykonuje sie dopoki spelniony jest pewien warunek logiczny
from dis import RETURN_CONST
from idlelib.autocomplete import FORCE
from zipfile import sizeEndCentDir

counter = 0
while counter < 5:
        print(counter, end=" ")
        counter += 1


print("***")

counter = 5
while counter < 12:
        print(counter, end=" ")
        counter += 1


print("***")

# PETLA "FOR"
# sluzy w Pythonie do iteracji po sekwencji (np lista, krotka tuple, lancuch string)
# lub innych interowalnych obiektrach

for i in range(0, 5):
    print(i)


print("***")

# FUNKCJA RANGE()
# zwraca szczegolny typ obiektu jakim jest generator
# generator tworzy liczby calkowite
# mozemy go wykorzystac w petli

for i in range(0, 6, 2):
    print(i, end=" ")


print("***")

# Funkcja range() posiada 3 argumenty: wartosc poczatkowa, wartosc konczowa, krok o jaki zmienia sie
# wartosc z kazdym obrotem petli. Jesli zmiana nastepuje co 1, nie musimy podawac trzeciego argumentu

# instrukcje "BREAK" i "CONTINUE"
# za pomoca instrukcji BREAK wychodzimy z najblizszej petli WHILE lub FORCE

for i in range(0, 10):
    print(i, end=" ")
    if (i >= 3):
        break


print("***")

# za pomoca instrukcji CONTINUE przechodzimy do nastepnego kroku w petli

for i in range(0, 10):
    if (i % 2 == 0):
        continue
    print(i, end=" ")


print("***")

# Petle z galezia "ELSE"
# za blokiem kodu zawierajacym petle mozemy uzyc w instrukcji ELSE
# kod po klauzuli ELSE jest wykonany zawsze po normalnym zakonczeniu dzialania petli
# wyjatkiem niewykonania sie kodu po ELSE jest wyjscie z petli za pomoca BREAK lub RETURN

for i in range(5):
    print(i, end=" ")
else:
    print("koniec")


print("***")
