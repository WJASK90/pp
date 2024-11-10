list_1 = [9]
list_2 = list_1  # operacja kopiuje nazwe listy a NIE jest zawartosc (2 nazwy ale 1 lista). Aby sobie z tym uporac trzeba uzyc WYCINKOW (slice)
list_2[0] = 13
print(list_1)

list_1 = [9]
list_2 = list_1[:]  # kopiuje całą listę
list_2[0] = 13
print(list_1)

# wycking (slicing)
# lista[start:end]

numbers = [10, 8, 6, 4, 2] #indesk od lewej do prawego liczym 0, 1, 2 itd
new_numbers = numbers[1:4] #od indeksu do indeksu
print(new_numbers)

#          -5  -4 -3 -2 -1     od prawej do lewej liczymy: -1, -2, -3 itd
numbers = [10, 8, 6, 4, 2]
new_numbers = numbers[-4:4] #od indeksu do indeksu
print(new_numbers)

numbers = [10, 8, 6, 4, 2]
new_numbers = numbers[3:len(numbers)]
print(new_numbers)

numbers = [10, 8, 6, 4, 2]
new_numbers = numbers[:] #taki zapis oznacza kopiowanie calej listy
print(new_numbers)

#operatory in, not in

numbers = [1, 2, 3, 4, 5]
print(5 in numbers)
print(6 not in numbers)

# wyrazenia listowe BARDZO WAZNE, BEDA CZESTO UZYWANE ! ! ! ! ! ! ! !

numbers = [1, 2, 3, 4, 5]
for i in range(1, 101):
    numbers.append(i)

print(numbers)

numbers = [i ** 2 for i in range (1, 101)]
print(numbers)

numbers = [i for i in range(1, 101) if i % 2 == 0] #mamy numery parzyste w tym rangu
print(numbers)

# 1 - 300 <-- w tym rangu ile liczb jest podzielnych przez 3 i 7 jednoczesnie
print(len([i for i in range(1, 301) if i % 3 == 0 and i % 7 == 0]))