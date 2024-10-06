#Napisz skrypt rysujący prostokąt ze znaków @, liczba kolumn 10 i liczba wierszy 4

char = input("Podaj znak: ")
columns = int(input("Pojad liczbę kolumn: "))
rows = int(input("Podaj liczbę wierszy: "))

print((char * columns + "\n") * rows)

#Pobierz od użytkownika dwie liczby całkowite i wykonaj na nich operacje: dodawania, odejmowania, mnozenia, dzielenia i modulo. Wyswietl na ekranie.

a = int(input("Podaj liczbę całkowitą a: "))
b = int(input("Podaj liczbę całkowitą b: "))

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)

#Stworz drabine na ekranie

print("+" + "-+" * 9, "| " * 10, "+" + "-+" 9, sep="\n")

