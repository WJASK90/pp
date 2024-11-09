#zadanie 2 napisz skrypt wyznaczający ocenę jaką otrzyma student

points = int(input("Podaj liczbę punktow (1-100): "))

#end=" " znaczy NIE PRZECHODZ DO NOWEJ LINII

print("Twoja ocena jest", end=" ")
if points >= 95:
    print("bardzo dobra (czyli 5,0)")
elif points > 84:
    print("ponad dobra (czyli 4,5)")
elif points >= 70:
    print("dobra (czyli 4,0)")
elif points > 60:
    print("dość dobra (czyli 3,5)")
elif points > 50:
    print("dostateczna (3,0)")
else:
    print("niedostateczna (czyli 2,0)")