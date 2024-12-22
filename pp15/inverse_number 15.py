# while True:
#     number = int(input("Podaj liczbę całkowitą: "))
#     print("Odwrotna liczba to", 1 / number)

#znowu mogą być błędy pisane przez użytkownika, wiec pierw identyfikujemy kod
#który może stwarzać problemy tam dajemy TRY... EXCEPT...

#tym razemy wykorzystajmy komunikaty VALUEERROR, ZERODIVISIONERROR itp
while True:
    try:
        number = int(input("Podaj liczbę całkowitą: "))
        print("Odwrotna liczba to", 1 / number)
    except ValueError: #jeśli będzie VaLueError czyli brak liczby całkowitej
        print("To nie jest liczba całkowita")
    except ZeroDivisionError:
        print("Błąd dzielenia przez zero")
    except:
        print("Coś poszło nie tak...")