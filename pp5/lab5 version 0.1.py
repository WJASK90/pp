#skrypt o danych użytkownika takie jak: imię, wiek ora miasto

imię = "Wojtek"
lat = "32"
miasto = "Krakowa"

print("To jest " + str(imię) + ", ma " + str(lat) + " i jest z " + str(miasto) + ".")

#KWADRATY oblicz pole powierzchni, obwód oraz długość przekątnej dla kwadratów o długościach boku: 2, 7, 11 oraz 10

a = 2
b = 7
c = 11
d = 19

print("Pole powierzchni to " + str(a ** 2) + " lub " + str(b ** 2) + " lub " + str(c ** 2) + " lub " + str(d ** 2) + ".")
print("Obwód to " + str(a * 4) + " lub " + str(b * 4) + " lub " + str(c * 4) + " lub " + str(d * 4) + ".")
print("Przekątna to " + str((a ** 2 + a ** 2) ** 0.5) + " lub " + str((b ** 2 + b ** 2) ** 0.5) + " lub " + str((c ** 2 + c ** 2) ** 0.5) + " lub " + str((d ** 2 + d ** 2) ** 0.5) + ".")

#wyznacz zysk 3 letniej lokaty bankowej wg założeń: 46567.00 zł, oprocentowanie stałe roczne 7.5%, coroczna kapitalizacja odsetek

own_funds = 46_567.
deposit = own_funds
factor = 1.075

deposit = deposit * factor #po roku #tak samo deposit *= factor
deposit = deposit * factor #po dwoch latach
deposit = deposit * factor #po trzech latach

print("Zysk z inwestycji wynosi", round(deposit - own_funds, 2), "zł.")