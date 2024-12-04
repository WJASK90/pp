#technika wykonywania cwiczen: rozdziel na etapy, dodawaj coraz bardziej skomplikowane kroki
#Wyświetl liczby od 1 do 100 z pominięciem liczb podzielnych przez 3
#zastosowałem modulo, używając // dzieliło wartości
# for i in range(0, 100):
#     if (i % 3):
#         print(i, end=" ")


#for i in range(1,101):
#   print(i)

for i in range(1, 101):
    if i % 3 != 0:
        print(i)