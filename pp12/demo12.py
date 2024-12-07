name = input("Jak masz na imię? ") #funkcja input do ktorej dajem ciag znakow i zwraca wartosc zapisana
print("Witaj {}!".format(name))

print("raz", "dwa", "trzy")

def introduce(first_name, last_name): #napis USAGE z liczba nad def oznacza ile razy funkcja jest uzywana w kodzie
    print("Cześć, jestem", first_name, last_name + ".")

introduce("Wojciech", "Jaskot")
