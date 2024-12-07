# 2. Napisz skrypt pobierający od użytkownika serię liczb całkowitych, a
# następnie wyświetl je w kolejności malejącej pozbywając się wcześniej
# duplikatów.

import random

lista_elementów = []

ZAKRES_1 = int(input("Podaj minimum zakresu: "))
ZAKRES_2 = int(input("Podaj maksimum zakresu: "))
SERIA = int(input("Podaj serię liczb całkowitych: "))
for i in range(SERIA):
    lista_elementów = [random.randint(ZAKRES_1, ZAKRES_2) for j in range(SERIA)]
    print("Stworzona seria: ", lista_elementów)

lista_elementów.sort(reverse=True)
print("Lista w kojeności malejącej: ", lista_elementów)


# sortowanie w kolejnosci malejacej SERIA.sort(reverse=True)

