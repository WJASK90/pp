numbers = [1, 2, 3] #LISTA bo []
numbers = (1, 2, 3) #KROTKA bo () i wartosc numbers = 1, 2, 3 bedzie tak interpretowana domyslnie jako KROTKA, puste nawiasy () to tez KROTKA

#ale numbers = (1) to liczba, chociaz jak napiszemy numbers = (1,) to wtedy mamy KROTKE z jednym elementem

for number in numbers:
    print(number) #dostajemy wartosci krotki czyli 1, 2, 3

print(numbers[1:]) #robimy wycinek --> przy wycinkach tworzy sie KOPIA bo krotka jest NIEZMIENNA wynik: (2, 3)

numbers = tuple(x for x in range(10) if x % 2 == 0)
print(numbers) #wynik (0, 2, 4, 6, 8)

numbers = (1, 2, 3)

# numbers[0] = 999 # dostaniemy blad, bo nie jest przewidziana zmiana bo KROTKA/Tuple jest NIEZMIENNA
# del numbers[0] # dostaniemy blad, bo nie jest przewidziana zmiana bo KROTKA/Tuple jest NIEZMIENNA
# del numbers # bedzie dzialac bo pozbywamy sie CALEJ KROTKI, elementy KROTKI/Tuple sa NIEZMIENNE

numbers_b = [1, 2, 3]
print(len(numbers))
print(numbers * 2)
numbers = tuple(numbers_b) #konwertujemy LISTE w KROTKE patrz plik demo14 2




