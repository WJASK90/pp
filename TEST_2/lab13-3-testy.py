 # 3. Napisz skrypt symulujący uproszczone działanie gry losowej "jednoręki bandyta",
# w tym celu:
# • za każdym "pociągnięciem" losuj 3 litery ze zbioru od A do E,
# • kontynuuj losowania do momentu wystąpienia 3 takich samych liter np. A A A,
# • wyświetl informację o wynikach poszczególnych losowań oraz numer próby,
# • przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
# większą liczbę liter.

import random

FIRST_SYMBOL = 'A'
LAST_SYMBOL = 'H'
NUMBER_OF_LETTERS = 4

# kod znaku A to 65 ord("A") --> wartosc ascii?

def draw_letter(): #wylosuj litere
    # return chr(random.randint(ord('A'), ord('E'))) #wersja od A do E
    return chr(random.randint(ord(FIRST_SYMBOL), ord(LAST_SYMBOL)))

def draw_row(): #wylosuj wiersz liter
    return [draw_letter() for _ in range(NUMBER_OF_LETTERS)] #zamiast oryginalnego 6 dajemy NUMBER_OF_LETTERS

def check(row): #sprawdzamy wiersz
    first_element = row[0]
    for element in row:
        if first_element != element:
            return False
    return True


# print(ord("A")) #ord = wartosc liczbową
#
# print(chr(65)) #zmieniamy wartosc na znak

# print(draw_letter()) #losowanie jednej litery

# print(draw_row()) #losowanie wiersza/serii liter (3)

# print(check(draw_row())) #wywolulejmy w funkcji

#piszemy mechanizm ktory bedzie wykonywal funkcje do momentu az nie trafimy (PETLA WHILE!!! z counterem)

counter = 1
while True:
    row = draw_row()
    print(row, counter)
    if check(row):
        break
    counter += 1

#petla zatrzymuje sie kiedy sa wylosowane takie same litery

#PYTANIE:
# • przemyśl jak dużo zmian trzeba wprowadzić w skrypcie, aby losować z większego zbioru liter, a także
# większą liczbę liter.
#ODPOWIEDZ:
#draw_letter - zakres do powiekszenia i wiekszy zakres draw_row
