# 1. Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.

def pow(numbers, exponent): #funkcja przyjmuje liste numbers i drugi parametr do jakiej liczby potegi beda podnoszone
    numbers = numbers[:] # zabezpieczenie przed modyfikacja listy, jeśli nie to by nachodziły na siebie wartości (przykład na tablicy, nagranie 07.12)
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** exponent
    return numbers


numbers = [1, 2, 3]
print(pow(numbers, 2))

print(pow(numbers, 5))