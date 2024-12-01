# Napisz program pobierający od użytkownika liczbę całkowitą i zwracający
# liczbę jedynek w ciągu bitów reprezentujących tę liczbę.

daj_liczbe = int(input("Podaj proszę liczbę: "))
binarnie = "{:08b}".format(daj_liczbe)

ile_1 = 0
for i in binarnie:
    if i == '1':
        ile_1 += 1
print("Ilość jedynek w zapisie binarnym " + str(daj_liczbe) + " to: " + str(ile_1))