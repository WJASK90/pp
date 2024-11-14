#Ustal czy liczby są podzielne przez 3,4, 7, 13)
print(14196 % 3 ==0)
print(14196 % 4 ==0)
print(14196 % 7 ==0)
print(14196 % 13 ==0)
print(14199 % 3 ==0)
print(14199 % 4 ==0)
print(14199 % 7 ==0)
print(14199 % 13 ==0)

#Skrypt który oblicza inwestycje
print("Poczatkowa wartosc inwestycji", 14_000.,"zł")
print("Wartość inwestycji po pierwszym roku", 14_000. * 1.4, "zł")
print("Wartość inwestycji po drugim roku", (14_000. * 1.4) - 1_500, "zł")
print("Wartość inwestycji po trzecim roku", round(((14_000. * 1.4) - 1_500) * 1.12, 2), "zł")

#Wyliczenie wartosci dziesetnych nastepujacych liczb, zapisanych w roznych systemach liczbowych
print(0o777)
print(0b1011)
print(0xFFF)

#Wersja wykladowcy:
print(0o777)
print(7 * 8 ** 2 + 7 * 8 ** 1 + 7 * 8 ** 0)
print(0b1011)
print(1 * 2 ** 3 + 0 * 2 ** 2 + 1 * 2 ** 1 + 1 * 2 ** 0)
print(0xFFF)
print (15 * 16 ** 2 + 15 * 16 ** 1 + 15 * 16 ** 0)

#system piątkowy
print(1 * 5 ** 2 + 2 * 5 ** 1 + 3 * 5 ** 0)