#zadanie 1 skrypt sprawdzający czy pierwiastek kwadratowy z liczby całkowitej pobranej od użytkownika jest także liczbą całkowitą (pierwiastek czyli 0.5 do potegi drugiej)

number = int(input("Podaj liczbę: "))

#modulo 1 zwroci nam wynik 0
if number ** 0.5 % 1 == 0:
    str1 = "Tak"
    str2 = ""
else:
    str1 = "Nie"
    str2 = "nie"

print(str1 + ". pierwiastek kwadratowy z liczby " + str(number) + " " + str2 + " jest liczbą całkowitą.")

