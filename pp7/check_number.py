# skrypt pobiera liczbę od użytkownika
# wyświetla informacje czy dana liczba jest parzysta, podzielna przez 5 i 7

number = int(input("Podaj liczbę: "))
print("Liczba jest: ")

if number % 2 == 0:
    print(" - parzysta")
else:
    print(" - nieparzysta")

if number % 5 == 0:
    print(" - podzielna przez 5")
else:
    print(" - niepodzielna przez 5")

if number % 7 == 0:
    print(" - podzielna przez 7")
else:
    print(" - niepodzielna przez 7")
