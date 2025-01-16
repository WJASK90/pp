# 1. Napisz funkcję, która pozbędzie się z listy powtarzających się elementów.

#Zbiór (Set) nie może mieć duplikatów ale przy wywołaniu nie powoduje błędów więc przemienie
#listę w zbiór w funkcji. Widziałem takie zastosowanie w aplikacji Sololearn.

#test z chatgpt
# def remove_duplicates(list_1):
#     return list(set(list_1))
#
# list_2 = [1, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7, 8]
# print(remove_duplicates(list_2))

def smierc_duplikatom(list):
    bez_duplikatow = []
    for i in list:
        if i not in bez_duplikatow:
            bez_duplikatow.append(i)
    return bez_duplikatow

lista_przykladowa = [1, 1, 2, 3, 4, 4, 5, 6, 6, 6]
print(smierc_duplikatom(lista_przykladowa))






































#
# def remove_duplicates_2(list):
#     unique_list = []  # Tworzymy nową listę
#     for item in list:  # Przechodzimy przez wszystkie elementy w liście
#         if item not in unique_list:  # Sprawdzamy, czy element już się pojawił
#             unique_list.append(item)  # Jeśli nie, dodajemy go do nowej listy
#     return unique_list  # Zwracamy listę bez duplikatów
#
# # Przykład użycia:
# original_list = [1, 2, 3, 2, 4, 5, 3, 6, 1]
# result = remove_duplicates_2(original_list)
# print(result)  # Wynik: [1, 2, 3, 4, 5, 6]