# 1. Napisz funkcję, która pozbędzie się z listy powtarzających się elementów.

#Zbiór (Set) nie może mieć duplikatów ale przy wywołaniu nie powoduje błędów więc przemienie
#listę w zbiór w funkcji. Widziałem takie zastosowanie w aplikacji Sololearn.

def remove_duplicates(list_1):
    return list(set(list_1))

list_2 = [1, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7, 8]
print(remove_duplicates(list_2))