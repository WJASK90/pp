# WZÓR

print("*        *", "**      **", "***    ***", "****  ****", "**********", "****  ****", "***    ***", "**      **", "*        *", sep="\n")

# OBLICZ ILE CZASU GODZIN POTRZEBA ABY POBRAĆ PLIK O ROZMIARZE 13 TB, A PLIK 194 MB UDAŁO SIĘ POBRAĆ W 5 SEKUND. WYNIK ZAOKRĄGLIJ DO PEŁNYCH GODZIN.

number_b = 1000000 #1 TB to 1000000 MB
#(194 * 12 * 60) = 139680 poniewaz 194 MB * 12 bo 5 sekund miesci sie 12 razy w 1 minucie * 60 minut czyli 1 godzina
number_a = 139680
wynik = number_b // number_a
print((wynik) * 13) #razy 13 poniewaz mamy 13 TB

# NAPISZ SKRYPT POZWALAJACY ZASYMULOWAC ZYSKI Z LOKAT BANKOWYCH

#Wartosc poczatkowa 30000
start = 30000

#oprocentowanie 7.5%, na trzy kwartaly
print("Wartosc z oprocentowania 7,5% po 1Q", 30000 * 1.01875, "zł")
print("Wartosc z oprocentowania 7,5% po 2Q", 30000 * 1.01875 * 1.01875, "zł")
print("Wartosc z oprocentowania 7,5% po 3Q", 30000 * 1.01875 * 1.01875 * 1.01875, "zł")
print("Wartosc z oprocentowania 7,5% po 4Q", 30000 * 1.01875 * 1.01875 * 1.01875 * 1.01875, "zł")
#po roku mamy 32314.075973510742 zł
rok_1 = 32314.075973510742
print(round(rok_1 - start)) #zysk z całego roku z oprocentowania 7,5%

#oprocentowanie 8%, na trzy kwartaly
print("Wartosc z oprocentowania 8% po 1Q", 30000 * 1.02, "zł")
print("Wartosc z oprocentowania 8% po 2Q", 30000 * 1.02 * 1.02, "zł")
print("Wartosc z oprocentowania 8% po 3Q", 30000 * 1.02 * 1.02 * 1.02, "zł")
print("Wartosc z oprocentowania 8% po 4Q", 30000 * 1.02 * 1.02 * 1.02 * 1.02, "zł")
#po roku mamy 32472.9648 zł
rok_2 = 32472.9648
print(round(rok_2 - start)) #zysk z całego roku z oprocentowania 8%

#oprocentowanie 8.25%, na trzy kwartaly
print("Wartosc z oprocentowania 8,25% po 1Q", 30000 * 1.020625, "zł")
print("Wartosc z oprocentowania 8,25% po 2Q", 30000 * 1.020625 * 1.020625, "zł")
print("Wartosc z oprocentowania 8,25% po 3Q", 30000 * 1.020625 * 1.020625 * 1.020625, "zł")
print("Wartosc z oprocentowania 8,25% po 4Q", 30000 * 1.020625 * 1.020625 * 1.020625 * 1.020625, "zł")
#po roku mamy 32552.628583012374 zł
rok_3 = 32552.628583012374
print(round(rok_3 - start)) #zysk z całego roku z oprocentowania 8,25%


