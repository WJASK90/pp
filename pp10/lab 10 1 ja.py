# Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
# • skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
# • pobrać kolejne elementy i zapisać je do listy,
# • wyświetlić w podsumowaniu jakie imiona pobrał od użytkownika.


# list_of_names = []
#
# names = input("Podaj imię które dodamy do listy: ")
# list_of_names.append(names)
#
# print(list_of_names)

# OR DO THIS

list_of_names = []
names = int(input("Podaj liczbę imion które wprowadzimy do listy: "))
for i in range(names):
    list_of_names.append(input("Podaj " + str(i + 1) + " imię: "))

print("Pobrane imiona: " + str(list_of_names))