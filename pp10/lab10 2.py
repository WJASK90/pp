# Napisz program, który zasymuluje 16 rzutów kostką do gry a następnie
# wyświetli poniższe informacje:
# • zestaw wylosowanych wyników,
# • wyrzucaną wartość za 8 razem,
# • liczbę wyrzuconych szóstek,
# • maksymalną liczbę wyrzuconych tych samych wartości pod rząd.

#importujemy modul import random ktorego potrzebujemy w cwiczeniu

import random

DICE_ROLLS_TOTAL = 16
rolls = []

for i in range(DICE_ROLLS_TOTAL):
    rolls.append(random.randint(1, 6))

print("Zbiór wyników po", DICE_ROLLS_TOTAL, "rzutach kostką do gry:", rolls )

print("Za 8. razem wyrzucono wartość", str(rolls[8 - 1])) #odejmujesz 1 bo indeks zaczyna sie od 0

sixes_total = 0 #widzac ile jest szostke, bede zmienial ta wartosc

for roll in rolls:
    if roll == 6:
        sixes_total += 1

print("Liczba wyrzuconych szóstek to", sixes_total )

in_row_value_tmp = rolls[0] #dajemy rolls[0] bo przyjmujemy, tylko jako przyklad, ze najczesciej bedzie 0
in_row_total_tmp = 0
in_row_value = 0
in_row_total = 0

for rolls in rolls:
    if roll == in_row_value_tmp:
        in_row_total_tmp += 1
    else:
        in_row_value_tmp = roll
        in_row_total_tmp > in_row_total
    if in_row_total_tmp > in_row_total:
        in_row_value = in_row_value_tmp
        in_row_total = in_row_total_tmp

print("Pod rząd wyrzucono", in_row_total, "razy wartość", str(in_row_value) + ".")
