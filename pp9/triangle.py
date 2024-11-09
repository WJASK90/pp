# pobieramy od użytkownika długości 3 odcników
# sprawdź czy można z nich zbudować trójkąt
# sprawdź jaki to będzie trójkąt ze względu na boki (różnoboczny, równoboczny, równoramienny)
# sprawdź jaki to będzie trójkąt ze względu na kąty (prostokątny, ostrokątny, rozwarty)

print("Podaj długości 3 odcinków (liczby całkowite)")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a + b > c and a + c> b and b + c > a:
    print("Z tych odcików można zbudować trójkąt", end=" ")
    if a == b == c and b == c:
        print("równoboczny", end=" ")
    elif a == b or a == c or b == c:
        print("równoramienny", end=" ")
    else:
        print("różnoramienny", end=" ")
    if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or c ** 2 + a ** 2 == b ** 2:
        print("prostokątny", end=" ")
    elif a ** 2 + b ** 2 < c ** 2 or b ** 2 + c ** 2 < a ** 2 or c ** 2 + a ** 2 < b ** 2:
        print("rozwartokątny")
    else:
        print("ostrokątny.")
