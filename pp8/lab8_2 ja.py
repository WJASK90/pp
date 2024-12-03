# Napisz skrypt wyświetlający na ekranie macierz. Rozmiar macierzy oraz
# znak z jakiej będzie zbudowana powinien określić użytkownik.

size = int(input("Podaj rozmiar: "))
mark = input("Podaj znak: ")

for i in range(size):
    for j in range(size):
        print(mark, end=" ")
    print()

