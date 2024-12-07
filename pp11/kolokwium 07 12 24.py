# napisz skrypt tworzacy i wyswietlajacy liczbe liczb calkowitych z zakresu podanego przez uzytkownika.
# przykladowo dla podanych liczb 1 i 5 na ekranie powinno pokazac sie  [1, 2, 3 ,4 ,5 ]

lista_1 = []

value_a = int(input("Podaj minimum zakresu liczb: "))
value_b = int(input("Podaj maksimum zakresu liczb: "))
for i in range(value_a, value_b+1):
    lista_1.append(i)

print(lista_1)