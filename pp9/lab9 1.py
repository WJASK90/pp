# Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
# określonego przez użytkownika.

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

# wersja wykladowcy
range_from = int(input("od: "))
range_to = int(input("do: "))

for i in range(range_from,range_to+1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i)

# kolejna wersja

print("Liczby z zakresu od", range_from, "do", range_to, "podzielne przez 3 lub 5 lub 7 to:", end=" ")
for i in range(range_from,range_to+1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print(", ", end="")
        print(i, end=" ")
print(".")

# wersja 2 usprawniona
is_first = True

print("Liczby z zakresu od", range_from, "do", range_to, "podzielne przez 3 lub 5 lub 7 to:", end=" ")
for i in range(range_from,range_to+1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        if not is_first:
            print(", ", end="")
        print(i, end=" ")
    is_first = False
print(".")