# 1. Napisz funkcję podnoszącą do wskazanej potęgi wszystkie elementy wskazanej listy.


def power_upper(list, power):
# numbers = numbers[:] # zabezpieczenie przed modyfikacja listy, jeśli nie to by nachodziły na siebie wartości
    for i in range(len(list)):
        list[i] = list[i] ** power
    return list

list = [1, 2, 3, 4, 5]

print(power_upper(list, 2))
