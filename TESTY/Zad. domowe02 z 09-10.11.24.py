# Napisz program, który wylosuje kilka serii liczb całkowitych i wyświetli je
# na ekranie, przy czym:
# • program zapyta użytkownika o zakres minimum oraz maksimum, DONE
# • będzie losował odpowiednie liczby z zakresu podanego przez użytkownika, DONE
# • będzie losował liczbę liczb do wylosowania z zakresu podanego przez użytkownika, --> czyli wybierze iles tam liczb z wylosowanego zakresu
# • będzie losował liczbę serii liczb do wylosowania z zakresu podanego przez użytkownika,
# • wyświetli wylosowane serie liczb.

import random

value_1 = int(input("Podaj minimum zakresu liczb: "))
value_2 = int(input("Podaj maksimum zakresu liczb: "))
liczba_serii = int(input("Podaj liczbę serii: "))
liczba_liczb_w_serii = int(input("Podaj liczbę liczb serii: "))
for i in range(liczba_serii):
    seria = [random.randint(value_1, value_2) for _ in range(liczba_liczb_w_serii)]
    print("Seria " + str(i+1) + ": " + str(seria))