# 1. Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.

lista_1 = [1,2,3,4,5,6,7,8,9,10]
do_ktorej_p = int(input("Do której potęgi podnosimy liczby? Wpisz numer: "))

def do_potegi(lista_1):
    for i in lista_1:
        print(i ** do_ktorej_p)


do_potegi(lista_1)




# for i in lista_1:
#     print(i ** 2)