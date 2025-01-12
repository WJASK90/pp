# 1. Napisz funkcję, która pozbędzie się z listy powtarzających się elementów.

#Zbiór (Set) nie może mieć duplikatów ale przy wywołaniu nie powoduje błędów więc przemienie
#listę w zbiór w funkcji

def remove_duplicates(example_list):
    return list(set(example_list))

my_list = [1, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7, 8]
print(remove_duplicates(my_list))