# Napisz program, który wylosuje kilka serii liczb całkowitych i wyświetli je
# na ekranie, przy czym:
# • program zapyta użytkownika o zakres minimum oraz maksimum, DONE
# • będzie losował odpowiednie liczby z zakresu podanego przez użytkownika, DONE
# • będzie losował liczbę liczb do wylosowania z zakresu podanego przez użytkownika, --> czyli wybierze iles tam liczb z wylosowanego zakresu
# • będzie losował liczbę serii liczb do wylosowania z zakresu podanego przez użytkownika,
# • wyświetli wylosowane serie liczb.

import random

counter = 1

value_1 = int(input("Podaj minimum zakresu liczb: "))
value_2 = int(input("Podaj maksimum zakresu liczb: "))

liczba_serii = int(input("Podaj liczbę liczb serii: "))
liczba_liczb_w_serii = int(input("Podaj liczbę serii: "))
for i in range(value_1,value_2+1):
    print(i)

number = random.randint(value_1, value_2)





















#DEF? PATRZ DEMO PP7!!!
# BY CHAT GPT
# import random
#
#
# def losuj_serie():
#     # Pobieranie zakresu od użytkownika
#     min_value = int(input("Podaj minimalną wartość zakresu: "))
#     max_value = int(input("Podaj maksymalną wartość zakresu: "))
#
#     # Sprawdzanie, czy zakres jest poprawny
#     if min_value >= max_value:
#         print("Zakres minimum nie może być większy lub równy maksimum.")
#         return
#
#     # Losowanie liczby liczb do wylosowania
#     liczba_liczb = int(input("Ile liczb chcesz wylosować w jednej serii? "))
#
#     # Losowanie liczby serii
#     liczba_serii = int(input("Ile serii liczb chcesz wylosować? "))
#
#     # Losowanie i wyświetlanie serii
#     for i in range(liczba_serii):
#         seria = [random.randint(min_value, max_value) for _ in range(liczba_liczb)]
#         print(f"Seria {i + 1}: {seria}")
#
#
# # Uruchomienie programu
# losuj_serie()