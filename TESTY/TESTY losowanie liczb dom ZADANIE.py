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
for i in range(value_1,value_2+1):
    print(i)

number = random.randint(value_1, value_2)

print("Liczba wylosowana z zakresu to: " + str(number))


