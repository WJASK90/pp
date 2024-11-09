#Wyświetl liczby od 1 do 100 z pominięciem liczb podzielnych przez 3
#zastosowałem modulo, używając // dzieliło wartości
for i in range(0, 100):
    if (i % 3):
        print(i, end=" ")