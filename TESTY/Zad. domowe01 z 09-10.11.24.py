# Napisz program sumujący pobrane liczby od użytkownika wg wytycznych:
# • program powinien pobierać od użytkownika liczby całkowite,
# • niepodanie liczby powinno zakończyć wprowadzanie danych,
# • program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych.

suma_parzystych = 0
suma_nieparzystych = 0
liczby = [] #lista do przechowywania liczb

while True:
    # Pobieranie liczby od użytkownika
    print("Cześć! Podaj liczbę całkowitą, lub naciśniej Enter aby zakończyć")
    liczba = input("Twoja liczba: ")
    if liczba == "":
        break

    liczba = int(liczba)

    # Jeśli użytkownik zostawi puste pole, czyli nie poda liczby, konczymy
    if liczba % 2 == 0:
        suma_parzystych += liczba
    else:
        suma_nieparzystych += liczba

print("Suma liczb parzystych: " + str(suma_parzystych))
print("Suma liczb nieparzystych: " + str(suma_nieparzystych))