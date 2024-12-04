liczby = [] #lista do przechowywania liczb
suma_parzystych = 0

while True:
    # Pobieranie liczby od użytkownika
    print("Cześć! Podaj liczbę całkowitą, lub naciśniej Enter aby zakończyć")
    liczba = input("Twoja liczba: ")
    if liczba == "":
        break

if liczba % 2 == 0:
    suma_parzystych += liczba