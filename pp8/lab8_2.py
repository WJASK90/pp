#Napisz skrypt wyświetlający na ekranie macierz. Rozmiar macierzy oraz znak z jakiej będzie zbudowana powinien określić użytkownik

size = int(input("Podaj rozmiar: "))
sign = input("Podaj znak: ")

i = (size * size) * sign

for i in range(0, 6):
    print(i, end=" " * size )



