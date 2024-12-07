name = input("Jak masz na imię? ") #funkcja input do ktorej dajem ciag znakow i zwraca wartosc zapisana
print("Witaj {}!".format(name))

print("raz", "dwa", "trzy")

def introduce(first_name, last_name): #napis USAGE z liczba nad def oznacza ile razy funkcja jest uzywana w kodzie
    print("Cześć, jestem", first_name, last_name + ".")

introduce("Wojciech", "Jaskot")
#jesli napiszesz dwa razy introduce(first_name: "Wojciech", first_name: "Jaskot") to oszaleje bo nie ma last_name i wyjdzie blad

print("raz", "dwa", "trzy", sep="-")

#jestli napisze introduce("Marcin") bez nazwsika to wyjdzie defaultowa/domyslna wartosc czyli wynik --> Marcin Jaskot
