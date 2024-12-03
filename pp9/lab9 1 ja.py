# Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
# określonego przez użytkownika

# value_1 = int(input("Podaj minimum zakresu liczb: "))
# value_2 = int(input("Podaj maksimum zakresu liczb: "))
#
# for i in range(value_1, value_2 + 1):
#     if i % 3:
#         print(i, end= "")
#     if i % 5:
#         print(i, end = "")
#     if i % 7:
#         print(i, end = "")

value_1 = int(input("Podaj początek zakresu liczb, sprawdzimy czy są podzielne przez 3, 5 lub 7: "))
value_2 = int(input("Podaj koniec zakresu liczb, sprawdzimy czy są podzielne przez 3, 5 lub 7: "))
for i in range(value_1,value_2+1):
    if i % 3 == 0:
        print(i)
    elif i % 5 == 0:
        print(i)
    elif i % 7 == 0:
        print(i)
    else:
        print(end="")