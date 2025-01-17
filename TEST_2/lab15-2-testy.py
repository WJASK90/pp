# 2. Napisz program pobierający od użytkownika 3 liczby zmiennoprzecinkowe.
# Uwzględnij możliwość pomyłki użytkownika.


numbers = []
counter = 1

while True: #dopoki jest spelniany warunek
    if counter > 3:
        break
    try: #tutaj badamy sytuacje wyjatkowo, pobieramy liczbe, zapisujemy zmiennia i pobieramy input typo float
        number = float(input("Podaj {} liczbę zmiennoprzecinkową: ".format(counter)))
        numbers.append(number)
        counter += 1
    except:
        print("Podana wartość jest niepoprawna, spróbuj ponownie!")

print(numbers)


#1