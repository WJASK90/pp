print("Sumator-Multiplikator")
print("Program oblicza sumę lub iloczyn wielu dodatnich liczb.")
print("Dozwolone jest używanie tylko jednego rodzaju działania: + albo *")
print("Przykłady:")
print("  3 + 4 + 7 + 0.5")
print("  2 * 3 * 4 * 0.33\n")

while True:
    tekst = input("Podaj wyrażenie arytmetyczne: ").strip()

    # Usuwam spacje
    czesci = tekst.split()

    # 3 elementy: liczba operator liczba?
    if len(czesci) < 3:
        print("UWAGA! Wyrażenie musi mieć co najmniej dwie liczby i jeden operator.")
        print("Spróbuj ponownie.\n")
        continue

    # Sprawdzam: operatory poprawne i jednolite
    operatory = []
    liczby = []

    blad = False

    for i in range(len(czesci)):
        if i % 2 == 0:
            # liczba
            try:
                liczba = float(czesci[i])
                if liczba < 0:
                    print("UWAGA! Wszystkie liczby muszą być dodatnie.")
                    blad = True
                    break
                liczby.append(liczba)
            except ValueError:
                print("UWAGA! W miejscu liczby podano niepoprawną wartość.")
                blad = True
                break
        else:
            # operator
            if czesci[i] not in ["+", "*"]:
                print("UWAGA! Dozwolone operatory to tylko + lub *.")
                blad = True
                break
            operatory.append(czesci[i])

    if blad:
        print("Spróbuj ponownie.\n")
        continue

    # Sprawdzam: operatory
    if len(set(operatory)) != 1:
        print("WAŻNE! W wyrażeniu musi być tylko jeden rodzaj działania.")
        print("Albo same +, albo same *.\n")
        continue

    # Wynik
    if operatory[0] == "+":
        wynik = 0
        for x in liczby:
            wynik += x
    else:
        wynik = 1
        for x in liczby:
            wynik *= x

    # Formatowanie: liczba całkowita to int
    if isinstance(wynik, float) and wynik.is_integer():
        wynik = int(wynik)

    print(f"Wynik: {wynik}")
    break
