# 2. Napisz funkcję zamieniającą 3 listy na 1 krotkę bez powtarzających się elementów.
# Przykład: [1, 2], [1, 1], [4, 4, 4] -> (1, 2, 4)




lista_1 = [1, 1, 3]
lista_2 = [4, 5, 5]
lista_3 = [7, 7, 7]

def pierwsza_lista(lista_1):
    for i in range(len(lista_1)):
        if i != 1:
            print(lista_1[i])
            lista_1 = tuple
def druga_lista(lista_2):
    for i in range(len(lista_2)):
        if i != 5:
            print(lista_2[i])
            lista_2 = tuple
def trzecia_lista(lista_3):
    for i in range(len(lista_3)):
        if i != 7:
            print(lista_3[i])
            lista_3 = tuple

pierwsza_lista(lista_1)
druga_lista(lista_2)
trzecia_lista(lista_3)



#JAK ZMIENIC LISTE W KROTKE
# letters = tuple("Ala ma kota.")
# print(letters) #dostajemy KROTKE