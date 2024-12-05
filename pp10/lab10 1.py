# Napisz skrypt, pobierający od użytkownika zbiór imion, w tym celu:
# • skrypt powinien zapytać użytkownika o liczbę elementów zbioru,
# • pobrać kolejne elementy i zapisać je do listy,
# • wyświetlić w podsumowaniu jakie imiona pobrał od użytkownika.

#po pierwsze tworzymy liste (names), potem przechowywam w zmiennej ilosc elementow
#uzywamy INPUT i konwertujemy na liczbe calkowita dzieki INT
#tworzymy petle FOR I IN RANGE(total_elements) gdzie bedziemy pytac o imiona, dodajemy sobie metoda APPEND
#zeby dokleic do listy dane. piszemy I + 1 poniewaz range/zakres zaczyna sie od 0 wiec mamy odliczanie
#od 1 a nie od 0 :) teraz wystarczy wyswietlic odpowiedz i dopisujemy na koncu LISTE names

names = []
total_elements = int(input("Podaj liczbę imion jakie zamierzasz wprowadzić: "))
for i in range(total_elements):
    names.append(input("Podaj " + str(i + 1) + " imię: "))

print("Od użytkownika pobrano następujący zbiór imion:", names)
