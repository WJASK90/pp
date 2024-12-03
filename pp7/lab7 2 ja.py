# Napisz skrypt wyznaczający ocenę jaką otrzyma student, ze względu na ilość
# otrzymanych punków z kolokwium:
# • ocena bardzo dobra (5,0), jeżeli student otrzymał 95 lub więcej punktów,
# • jeżeli punktów jest mniej niż 95, ale więcej niż 84 studentowi przysługuje ocena ponad dobra
# (4,5),
# • ocena dobra (4,0) przyznawana jest dla ilości punktów z przedziału [70, 84],
# • jeżeli student otrzymał więcej niż 60 ale mniej niż 70 to przysługuje mu ocena dość dobra
# (3,5),
# • ocena dostateczna jest dla studentów z punktowym wynikiem równym przynajmniej 60 ale
# powyżej 50 punktów,
# • wszystkie wyniki równe 50 i mniej punktów wiążą się z otrzymaniem oceny niedostatecznej
# (2.0).

points = int(input("Podaj punktacje od 0 do 100: "))

print("Twoja ocena jest...")

if points >= 95:
    print("... BARDZO DOBRA")
if points < 90 and points > 84:
    print("... PONAD DOBRA")
if points > 70 and points <= 84:
    print("... DOBRA")
if points > 60 and points < 70:
    print("... DOŚĆ DOBRA")
if points > 50 and points <= 60:
    print("... DOSTATECZNA")
if points <= 50:
    print("... NIEDOSTATECZNA")
