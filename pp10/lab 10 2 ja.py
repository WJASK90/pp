# Napisz program, który zasymuluje 16 rzutów kostką do gry a następnie
# wyświetli poniższe informacje:
# • zestaw wylosowanych wyników,
# • wyrzucaną wartość za 8 razem,
# • liczbę wyrzuconych szóstek,
# • maksymalną liczbę wyrzuconych tych samych wartości pod rząd.

import random

ZAKRES = 16
rzuty = []

for i in range(ZAKRES):
    rzuty.append(random.randint(1,6))
    # print(random.randint(1,6), end= " ")

print("Mamy następujące wyniki po ", ZAKRES, "rzutach kośćmi: ", rzuty)
print("Ósmy rzut dał nam wynik ", rzuty[7])

#usuwamy RANGE z dopisanego do listy rzuty po to aby nie robilo nam z tego integer
szóstki = 0
for i in rzuty:
    if i == 6:
        szóstki += 1

print("Liczba wyrzuconych 6 to ", szóstki)
#pamietaj for I in RZUTY czyli WARTOSCI w LISCIE RZUTY sa brane pod uwage!



print("Maksymalna liczba wyrzuconych tych samych wartość pod rząd to ")


# szóstki = 0
#
# for rzuty in range(1,16):
#     if rzuty == 6:
#         szóstki = +1

# print(wyniki)