# 1. Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.

#tworze listę i input gdzie uzytkownik wybiera wskazaną potęgę do której podniesiemy elementy listy + zmienne z zakresami min. i max.

lista_1 = []
zakres_1 = int(input("Podaj minimalny zakres listy: "))
zakres_2= int(input("Podaj maksymalny zakres listy: "))
do_ktorej_p = int(input("Do której potęgi podnosimy liczby? Wpisz numer: "))

#for i in .... po to aby kod przeskakiwał po każdym elemencie listy, zakres-i podnosimy do potęgi zmiennej/inputu do_ktorej_p
def do_potegi():
    for i in range(zakres_1, zakres_2 + 1):
        print(i ** do_ktorej_p)

#wywołujemy funkcję do akcji
do_potegi()

#TEST funkcja wychodzi ale nie pyta uzytkownika o zakres elementow w liscie (a zrozumialem ze to musi byc w kodzie)
# #for i in .... po to aby kod przeskakiwał po każdym elemencie listy, zakres-i podnosimy do potęgi zmiennej/inputu do_ktorej_p
# def do_potegi(lista_1):
#     for i in lista_1:
#         print(i ** do_ktorej_p)
#
# #wywołujemy funkcję do akcji
# do_potegi(lista_1)

#test
# for i in lista_1:
#     print(i ** 2)