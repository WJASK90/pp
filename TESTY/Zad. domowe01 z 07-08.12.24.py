# 1. Napisz funkcję, która pozbędzie się z listy powtarzających się elementów.

def death_to_duplicates(list):
    no_duplicates = []
    for i in list:
        if i not in no_duplicates: #jeśli elementu nie ma w liście to zostaje dodany do no_duplicates, w ten sposób nie ma duplikatów
            no_duplicates.append(i)
    return no_duplicates #można by przemienić liste na Set/Zbiór ale na zajęciach ich nie mieliśmy, widziałem je w aplikacji Sololearn wtedy duplikaty są ignorowane przy wywoływaniu

example_list = [1, 1, 2, 3, 4, 4, 5, 6, 6, 6]
print(death_to_duplicates(example_list))