# 1. Utwórz funkcję o nazwie safe_int(), która pobiera pojedynczy argument arg.
# Jeśli to możliwe, funkcja powinna przekonwertować podany argument na typ int
# i zwrócić go. Jeśli jednak nie jest to możliwe (tj. jeśli wystąpi wyjątek), funkcja
# powinna zwrócić None.

arg1 = input("Podaj pojedyńczy element, które przekonwertujemy na liczbę całkowitą: ")

def safe_int(arg):
    try:
        return print(int(arg))
    except:
        return print("None")

safe_int(arg1)


#1