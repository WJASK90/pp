# Napisz funkcję usuwającą duplikaty z dowolnej listy elementów
#
# Przykład:
# print(remove_duplicates(["Ala", "Zosia", "Zosia", "Marek"]))
#
# ["Ala", "Zosia", "Marek"]


def remove_duplicates(list):
    never_duplicates = []
    for i in list:
        if i not in never_duplicates:
            never_duplicates.append(i)
    return never_duplicates

names_list = ["Ala", "Zosia", "Zosia", "Marek"]
print(remove_duplicates(names_list))