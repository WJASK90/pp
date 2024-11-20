# Napisz program sumujący pobrane liczby od użytkownika wg wytycznych:
# • program powinien pobierać od użytkownika liczby całkowite,
# • niepodanie liczby powinno zakończyć wprowadzanie danych,
# • program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych.

number = int(input("Podaj liczbę: "))
print("Liczba to: " + str(number))

n = int(input("Ile liczb chcesz podać? "))

# Pętla do pobierania liczb
for i in range(n):
    liczba = int(input(f"Podaj liczbę {i+1}: "))
    print(f"Podana liczba {i+1} to: {liczba}")