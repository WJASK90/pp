#skrypt o danych użytkownika takie jak: imię, wiek ora miasto

imię = "Wojtek"
lat = "32"
miasto = "Krakowa"

print("To jest " + str(imię) + " , ma " + str(lat) + " i jest z " + str(miasto) + ".")

#wersja wykładowcy
name = "Wiola"
age = 23
city = "Szczecin"

print("Mam na imię " + name + ".")
print("Mam", age, "lata.")
print("Moje miasto to", city + ".")

#KWADRATY oblicz pole powierzchni, obwód oraz długość przekątnej dla kwadratów o długościach boku: 2, 7, 11 oraz 10

a = 2
b = 7
c = 11
d = 19

print("Pole powierzchni to " + str(a ** 2) + " lub " + str(b ** 2) + " lub " + str(c ** 2) + " lub " + str(d ** 2) + ".")
print("Obwód to " + str(a * 4) + " lub " + str(b * 4) + " lub " + str(c * 4) + " lub " + str(d * 4) + ".")
print("Przekątna to " + str((a ** 2 + a ** 2) ** 0.5) + " lub " + str((b ** 2 + b ** 2) ** 0.5) + " lub " + str((c ** 2 + c ** 2) ** 0.5) + " lub " + str((d ** 2 + d ** 2) ** 0.5) + ".")

#wersja wykładowcy

a = 2 #kwadrat 1
print("Kwadrat o długości boku równej", a)
print("- obwód", 4 * a)
print("- pole powierzchni", a ** 2)
print("- długość przekątnej", a * 2 ** 0.5)

b = 7 #kwadrat 2

print("Kwadrat o długości boku równej", b)
print("- obwód", 4 * b)
print("- pole powierzchni", b ** 2)
print("- długość przekątnej", b * 2 ** 0.5)

c = 11 #kwadrat 3

print("Kwadrat o długości boku równej", c)
print("- obwód", 4 * c)
print("- pole powierzchni", c ** 2)
print("- długość przekątnej", c * 2 ** 0.5)

d = 19 #kwadrat 4

print("Kwadrat o długości boku równej", d)
print("- obwód", 4 * d)
print("- pole powierzchni", d ** 2)
print("- długość przekątnej", d * 2 ** 0.5)

#wyznacz zysk 3 letniej lokaty bankowej wg założeń: 46567.00 zł, oprocentowanie stałe roczne 7.5%, coroczna kapitalizacja odsetek

Inwestowanie = 46567.
Oprocentowanie = 1.075

#wersja wykładowcy

own_funds = 46_567.
deposit = own_funds
factor = 1.075

deposit = deposit * factor #po roku #tak samo deposit *= factor
deposit = deposit * factor #po dwoch latach
deposit = deposit * factor #po trzech latach

print("Zysk z inwestycji wynosi", round(deposit - own_funds, 2), "zł.")

