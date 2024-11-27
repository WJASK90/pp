# Napisz program sumujący pobrane liczby od użytkownika wg wytycznych:
# • program powinien pobierać od użytkownika liczby całkowite,
# • niepodanie liczby powinno zakończyć wprowadzanie danych,
# • program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych.

# Inicjalizacja zmiennych do sumowania liczb parzystych i nieparzystych
suma_parzystych = 0
suma_nieparzystych = 0

while True:
    # Pobieranie liczby od użytkownika
    liczba = input("Podaj liczbę całkowitą (lub naciśnij Enter, aby zakończyć): ")

    # Jeśli użytkownik zostawi puste pole, czyli nie poda liczby, konczymy
    if liczba == "":
        break

    # Próbujemy przekonwertować dane wejściowe na liczbę całkowitą
    try:
        liczba = int(liczba)
    except ValueError:
        print("To nie jest liczba całkowita, spróbuj ponownie.")
        continue

    # Dodawanie liczby do sumy parzystej lub nieparzystej
    if liczba % 2 == 0:
        suma_parzystych += liczba
    else:
        suma_nieparzystych += liczba

# Wyświetlenie sum
print(f"Suma liczb parzystych: {suma_parzystych}")
print(f"Suma liczb nieparzystych: {suma_nieparzystych}")