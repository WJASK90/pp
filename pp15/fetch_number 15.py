# numbers = []
#
# for i in range(5):
#     number = int(input("Podaj liczbę całkowitą: "))
#     numbers.append(number)
#
# print(numbers)

#działa poprawnie, ale co jeśli użytkownik nie zrobi tego co chcemy? Może ktoś wpiszę A i program padnie
#musimy zapobiec takiej sytuacji, pobierajmy liczby tylko poprawne,
# zmieniamy na pętle WHILE zamiast używać FOR, no i z WHILE musimy mieć COUNTER aby zliczyć
# 5 wpisanych danych

numbers = []
counter = 1

while True:
    if counter > 5: #potrzebujemy 5 danych
        break
    try:
        number = int(input("Podaj liczbę całkowitą: "))
        numbers.append(number) #dodaje ale pozniej dopiszemy EXCEPT na wypade błędów
        counter += 1 #zwiekszamy o 1 licznik az do 5, wtedy sie zatrzyma bo BREAK
    except:
        print("To nie jest liczba całkowita! Spróbuj ponownie")

print(numbers)