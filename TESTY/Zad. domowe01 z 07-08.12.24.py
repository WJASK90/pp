# 1. Napisz funkcję, która pozbędzie się z listy powtarzających się elementów.

def smierc_duplikatom(list):
    bez_duplikatow = []
    for i in list:
        if i not in bez_duplikatow:
            bez_duplikatow.append(i)
    return bez_duplikatow

lista_przykladowa = [1, 1, 2, 3, 4, 4, 5, 6, 6, 6]
print(smierc_duplikatom(lista_przykladowa))