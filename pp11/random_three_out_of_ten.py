# wylosuj 3 liczby ze zbioru 1-10, bez powtórzeń posortuj wynik

import random

random_numbers = []
for i in range(3):
    random_numbers.append(random.randint(1, 10))
random_numbers.sort()
print(random_numbers)

#ale tak daje nam powtorzenia, wariant jak zrobic zeby nie bylo

import random

random_numbers = []
counter = 3
while counter:
    number = random.randint(1, 10)
    if number not in random_numbers:
        random_numbers.append(number)
        counter -= 1
random_numbers.sort()
print(random_numbers)

#najlepszy wariant!!!

import random

numbers = [i for i in range(1, 11)]
random_numbers = random.sample(numbers, 3) #losowanie liczb ze zbioru bez powtorzen
random_numbers.sort()
print(random_numbers)