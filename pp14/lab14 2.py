# 2. Napisz funkcję zamieniającą 3 listy na 1 krotkę bez powtarzających się elementów.
# Przykład: [1, 2], [1, 1], [4, 4, 4] -> (1, 2, 4)

def merge_list_without_duplicate(source, target):
    for element in source:
        if element not in target:
            target.append(element)

def transform_data(list1, list2, list3):
    result = []
    merge_list_without_duplicate(list1, result)
    merge_list_without_duplicate(list2, result)
    merge_list_without_duplicate(list2, result)
    return tuple(result) #podczas zwracania konwertujemy w zwrotke/tuple

print(transform_data(list1=[1, 2], list2=[1, 1], list3=[4, 4, 4]))
print(transform_data(list1=[1, 2, 3], list2=[1, 2, 3], list3=[4, 5, 6]))
print(transform_data(list1=["Ala" , "ma"], list2=["Ala", "ma", "kota"], list3=["Mysz"]))