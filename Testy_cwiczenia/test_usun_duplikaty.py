# Ćwiczenie:
# Napisz funkcję remove_duplicates(lst: list) -> list, która usuwa duplikaty z listy, zachowując kolejność elementów.
#
# Opis: Funkcja powinna przyjąć listę (może zawierać różne typy danych: liczby, napisy, itp.), a następnie zwrócić nową listę,
# w której wszystkie duplikaty zostały usunięte, ale zachowana zostaje kolejność, w jakiej elementy występowały w oryginalnej liście.

#PRZYKLAD UZYCIA
# print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
# # Powinno zwrócić [1, 2, 3, 4, 5]
#
# print(remove_duplicates(['apple', 'banana', 'apple', 'orange', 'banana']))
# # Powinno zwrócić ['apple', 'banana', 'orange']

# Podpowiedzi:
# Możesz użyć zestawu (set), żeby śledzić, które elementy już widziałeś.
# Zestaw pozwala na szybkie sprawdzanie, czy element występuje, ale nie zachowuje kolejności, więc musisz zbudować
# listę wynikową, która usunie duplikaty, zachowując oryginalną kolejność.

def remove_duplicates(list):
    no_duplicates = []
    for i in list:
        if i not in no_duplicates:
            no_duplicates.append(i)
    return no_duplicates


print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates(["apple", "banana", "apple", "orange", "banana"]))




