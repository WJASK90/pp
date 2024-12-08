while True:
    try:
        number = int(input("Podaj liczbę całkowitą: "))
        print("Odwrotna liczba to", 1 / number)
    except ValueError: #jezeli wyjdzie blad ze nie ma liczby calkowitej
        print("To nie jest liczba całkowita")
    except ZeroDivisionError: #jak bedzie 0
        print("Błąd dzielenia przez zero")
    except: #błąd nie przewidziany
        print("Coś poszło nie tak...")