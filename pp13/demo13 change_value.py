# def change_value(n): #tu bierzemy jakby kopie tej wartosci
#     print("przed zmianą:", n)
#     n += 1
#     print("po zmianie" , n)
#
# value = 7
# change_value(value)
# print(value) #wyswietli sie 7, bo to n traktujemy jako zmienna lokalna

# wynik:
# przed zmianą: 7
# po zmianie 8
# 7

# def change_value(my_list_1): #tu bierzemy jakby kopie tej wartosci
#     my_list_1 = [0, 0]
#
#
# my_list_2 = [1, 2]
# change_value(my_list_2)
# print(my_list_2)

#czemu wynik to [1, 2]?

# my_list_2 = [1, 2] to specjalna wartosc zmienna. Why? Bo jak wchodzimy do funkcji change_value, nie robimy kopii listy w nawiasie, robimy kopie referencji
# do tej listy, ale nie listy.

def change_value(my_list_1):
    my_list_1[0] = 999 #indeks 0 to pierwsza liczba, wiec wynik bedzie [999, 2]


my_list_2 = [1, 2]
change_value(my_list_2)
print(my_list_2)