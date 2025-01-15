# 1. Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.

# def pow(numbers, exponent): #funkcja przyjmuje liste numbers i drugi parametr do jakiej liczby potegi beda podnoszone
#     numbers = numbers[:] # zabezpieczenie przed modyfikacja listy, jeśli nie to by nachodziły na siebie wartości (przykład na tablicy, nagranie 07.12)
#     for i in range(len(numbers)):
#         numbers[i] = numbers[i] ** exponent
#     return numbers
#
#
# numbers = [1, 2, 3]
# print(pow(numbers, 2))
#
# print(pow(numbers, 5))

# WERSJA 2

# def pow2(numbers, exponent): #funkcja przyjmuje liste numbers i drugi parametr do jakiej liczby potegi beda podnoszone
#     result = [] #nie ma zagrozenia ze lista bedzie modyfikowana, bo nie ma odnosnien do result ponizej
#     for n in numbers:
#         result.append(n ** exponent)
#     return result
#
# numbers = [1, 2, 3]
# print(pow2(numbers, 2))
#
# print(pow2(numbers, 5))

# WERSJA 3

def pow3(numbers, exponent):
    return [x ** exponent for x in numbers]

numbers = [1, 2, 3]
print(pow3(numbers, 2))

print(pow3(numbers, 5))

numbers_2 = [10, 20]
print(pow3(numbers_2, 2))