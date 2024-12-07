#wylosuj dowolna liczbe liczby z zakresu od 1 do 99

import random
def generate_numbers(total_numbers):
    numbers = []
    for _ in range(total_numbers):
        numbers.append(random.randint(1, 99)) #dodaj do listy to co wylosujesz
    return numbers

print(generate_numbers(10))
print(generate_numbers(1000))
