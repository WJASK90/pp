# 1. Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.

#tworze listę i input gdzie uzytkownik wybiera wskazaną potęgę do której podniesiemy elementy listy

lista_1 = [1,2,3,4,5,6,7,8,9,10]
do_ktorej_p = int(input("Do której potęgi podnosimy liczby? Wpisz numer: "))

#for i in .... po to aby kod przeskakiwał po każdym elemencie listy, zakres i podnosimy do potęgi zmiennej/inputu do_ktorej_p
def do_potegi(lista_1):
    for i in lista_1:
        print(i ** do_ktorej_p)

#wywołujemy funkcję do akcji
do_potegi(lista_1)




# for i in lista_1:
#     print(i ** 2)