# Napisz program sumujący pobrane liczby od użytkownika wg wytycznych:
# • program powinien pobierać od użytkownika liczby całkowite,
# • niepodanie liczby powinno zakończyć wprowadzanie danych,
# • program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych.

# s = 0

# # Pętla do wprowadzania liczb
# while True:
#     # Pobranie liczby od użytkownika
#     liczba = input("Podaj liczbę całkowitą (lub naciśnij Enter, aby zakończyć): ")
#     # Jeśli użytkownik nie podał liczby, zakończ pętlę
#     if int(liczba) == "":
#         print("Koniec pobierania liczb")
#         break
#         s += liczba
#         print("Suma podanych liczb to: " + str(s))

# s = 0
#
# while True:
#     liczba = input("Proszę o podanie liczby całkowitej (lub naciśniej Enter, aby zakończyć): ")
#     liczba = int(liczba)
#     if s == s += liczba:
#         print("Ok!")
#     else int(liczba) == "":
#         print("Koniec pobierania liczb")

while True:
    liczba = int(input("Podaj liczbę lub naciśnij Enter aby zakończyć: "))
    int(liczba)
    if int(liczba) == "":
        break
    if int(liczba) == liczba % 2 == 0:
        print("To jest liczba parzysta")
    else:
        print("To jest liczba nieparzysta")

