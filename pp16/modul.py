"""This is my own module... """  # dajemy to wewnatrz funkcji aby opsiac co ona robi, po prostu taka jest konwencja


def is_string(val):
    """Simple string validator""" #jak wyzej
    return isinstance(val,
                      str)  # isinstance sprawdza czy wartosc value jest faktycznie stringiem, zwroci nam True lub False


def sum_list_elem(list):  # funkcja ktora zsumuje wszystkie elementy listy
    sum = 0
    for elem in list:  # przechodzimy po elementach listy i dodajemy go do sumy poprzez +=, zamiast "for I in..." damy elem bo inaczej sugeruje uzywanie index
        sum += elem
    return sum  # lista liczb zostanie zsumowana


# print(dir())  # wywola liste stringow, nazw, elementy dostepne w tym pliku. Te elementy nazywaja sie WLASCIWOSCI
# print(__name__)  # co jest pod taka wlasciwoscia? wynik --> __main__

if __name__ == '__main__':  # uruchamiamy bezposrednio ten modul
    print(is_string('abc') == True)
    print(is_string(123) == False)
    print(sum_list_elem([1, 1, 1]) == 3)
    print(sum_list_elem([]) == 0)

#importujemy do MAIN.PY !!!