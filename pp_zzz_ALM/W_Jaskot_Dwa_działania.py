print("Dwa działania")
print("Program oblicza wartość wyrażenia złożonego z dwóch działań.")
print("Możesz używać cyfr oraz: +  -  *  /")
print("Przykład:  3 + 4 * 7")
print("WAŻNE! Wyrażenie nie może zawierać nawiasów.\n")

# Wczytywanie poprawnego wyrażenia
while True:
    tekst = input("Twoje wyrażenie arytmetyczne: ").strip()
    czesci = tekst.split()

    if len(czesci) != 5:
        print("UWAGA! Musisz zastosować się do formatu (wraz ze spacjami!): liczba operator liczba operator liczba.")
        print("Przykład:  3 + 4 * 7\n")
        continue

    a, op1, b, op2, c = czesci

    # Sprawdzanie liczb
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        print("UWAGA! Wszystkie podane wartości muszą być liczbami dodatnimi.")
        print("Spróbuj ponownie.\n")
        continue

    if a < 0 or b < 0 or c < 0:
        print("WAŻNE! Liczby muszą być dodatnie.")
        print("Spróbuj ponownie.\n")
        continue

    # Sprawdzanie operatorów
    if op1 not in ["+", "-", "*", "/"] or op2 not in ["+", "-", "*", "/"]:
        print("WAŻNE! Operatory których możesz użyć to +  -  *  /")
        print("Spróbuj ponownie.\n")
        continue

    break  # wyrażenie poprawne

print(f"\nWczytano poprawne wyrażenie: {a} {op1} {b} {op2} {c}")
print("Obliczam zgodnie z kolejnością działań...\n")

# Obliczenia
# Najpierw * i /
if op1 in ["*", "/"]:
    if op1 == "*":
        pierwszy = a * b
    else:
        pierwszy = a / b

    # drugi operator
    if op2 == "+":
        wynik = pierwszy + c
    elif op2 == "-":
        wynik = pierwszy - c
    elif op2 == "*":
        wynik = pierwszy * c
    else:
        wynik = pierwszy / c

else:
    # op1 to + lub -
    if op2 in ["*", "/"]:
        if op2 == "*":
            drugi = b * c
        else:
            drugi = b / c

        if op1 == "+":
            wynik = a + drugi
        else:
            wynik = a - drugi

    else:
        # oba działania są + lub -
        if op1 == "+":
            pierwszy = a + b
        else:
            pierwszy = a - b

        if op2 == "+":
            wynik = pierwszy + c
        else:
            wynik = pierwszy - c

if isinstance(wynik, float) and wynik.is_integer():
    wynik = int(wynik)

print(f"Wynik działania: {wynik}")
print("\n=== KONIEC PROGRAMU ===")
