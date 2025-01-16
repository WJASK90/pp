#chatgpt

# Stwórz funkcję, która przyjmuje listę liczb i zwraca tylko te liczby, które są większe niż średnia arytmetyczna tej listy.
# Instrukcje:
#
# Funkcja powinna przyjmować listę liczb (może to być lista liczb całkowitych lub
# zmiennoprzecinkowych).
#Wewnątrz funkcji oblicz średnią
# arytmetyczną tych liczb.
# Funkcja powinna zwrócić nową listę, która zawiera tylko te liczby, które są większe
# niż obliczona średnia.

# LISTA_LICZB = [10, 20, 30, 40, 50]
# suma = 0
#
# def srednia_listy():
#     lista_suma = []
#     for liczba in LISTA_LICZB:
#         if liczba not in lista_suma:
#             lista_suma.append(liczba)
#         elif:
#
#     return lista_suma



# LISTA_LICZB = [10, 20, 30, 40, 50]
#
# def lista_srednia():
#     lista_tylko_srednia = []
#     srednia = sum(LISTA_LICZB) / len(LISTA_LICZB)
#     for i in LISTA_LICZB:
#         if i > srednia:
#             lista_tylko_srednia.append(i)
#     return lista_tylko_srednia
#
#
# print(lista_srednia())


#LEPSZA WERSJA
# A - Zmiana warunku: if i > srednia: — teraz uwzględniamy tylko liczby większe niż średnia.
# B - Przyjęcie listy jako argumentu — funkcja teraz przyjmuje
# listę liczb jako argument, dzięki czemu jest bardziej elastyczna.

# def lista_srednia(lista):
#     lista_tylko_srednia = []
#     srednia = sum(lista) / len(lista)
#     for i in lista:
#         if i > srednia:
#             lista_tylko_srednia.append(i)
#     return lista_tylko_srednia
#
# # Testowanie funkcji
# LISTA_LICZB = [10, 20, 30, 40, 50]
# print(lista_srednia(LISTA_LICZB))  # wynik: [30, 40, 50]

# W Pythonie argumenty funkcji to po prostu zmienne, które przyjmują wartości przekazywane
# do funkcji w momencie jej wywołania. Ty jako programista możesz nadać im dowolne nazwy.
# Python nie przypisuje domyślnych typów do nazw argumentów, ale działa na podstawie
# danych, które do nich przekazujesz.

# ZADANIE
# Stwórz funkcję, która przyjmuje listę liczb i zwraca sumę liczb, które są liczbami nieparzystymi.
# Szczegóły:
#
#     Funkcja ma przyjmować listę liczb (mogą być zarówno całkowite, jak i zmiennoprzecinkowe).
#     Funkcja powinna obliczyć sumę tylko tych liczb, które są liczbami nieparzystymi (jeśli liczba jest liczbą całkowitą).
#     Funkcja powinna zwrócić wynik tej sumy.
#
# Przykłady:
#
#     Dla listy [1, 2, 3, 4, 5] wynik powinien być 9 (1 + 3 + 5).
#     Dla listy [10, 15, 20, 25] wynik powinien być 40 (15 + 25).
#     Dla listy [2.5, 3.5, 4.5, 5.5] funkcja powinna zwrócić 0 (nie ma liczb całkowitych nieparzystych).

#i % 2 != 0 cyfra nieparzysta
def suma_nieparzystych(lista):
    LISTA_NIEPARZYSTYCH = []
    for i in lista:
        if i == int(i) and i % 2 != 0:
            LISTA_NIEPARZYSTYCH.append(i)
        else:
            for i in LISTA_NIEPARZYSTYCH:
                sum(LISTA_NIEPARZYSTYCH)
    return sum(LISTA_NIEPARZYSTYCH)

lista_przyklad_111 = [1, 2, 3, 4, 5] #ma dać 9
lista_przyklad_222 = [10, 15, 20, 25] #ma dać 40
lista_przyklad_333 = [2.5, 3.5, 4.5, 5.5] #ma dać 0

print(suma_nieparzystych(lista_przyklad_111))
print(suma_nieparzystych(lista_przyklad_222))
print(suma_nieparzystych(lista_przyklad_333))

#POPRAWIONA WERSJA:

def suma_nieparzystych_1(lista):
    LISTA_NIEPARZYSTYCH_1 = []
    for i in lista:
        if i == int(i) and i % 2 != 0:  # Sprawdzamy, czy liczba jest całkowita i nieparzysta
            LISTA_NIEPARZYSTYCH_1.append(i)  # Dodajemy do listy liczb nieparzystych
    return sum(LISTA_NIEPARZYSTYCH_1)  # Suma liczb nieparzystych

lista_przyklad_111 = [1, 2, 3, 4, 5] #ma dać 9
lista_przyklad_222 = [10, 15, 20, 25] #ma dać 40
lista_przyklad_333 = [2.5, 3.5, 4.5, 5.5] #ma dać 0

print(suma_nieparzystych_1(lista_przyklad_111))
print(suma_nieparzystych_1(lista_przyklad_222))
print(suma_nieparzystych_1(lista_przyklad_333))
