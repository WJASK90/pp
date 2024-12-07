numbers = []
numbers_total = int(input("Podaj liczbę elementów zbioru: "))
for i in range(numbers_total): #pytamy tyle razy, ile sie zadeklarowal uzytkownik
    number = int(input("Podaj " + str(i + 1) + " element zbioru: ")) #czyli slownie PODAJ PIERWSZY ELEMENT ZBIORU
    numbers.append(number)

numbers_without_duplicates = []
for number in numbers: #przechodzimy po wszystkich elementach listy numbers
    if number not in numbers_without_duplicates:
        numbers_without_duplicates.append(number)


numbers_without_duplicates.sort(reverse=True)
print(numbers_without_duplicates)