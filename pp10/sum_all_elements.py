#napisz algorytm ktory zsumuje wszystkie wartosci

total = 0

numbers = [1, 3, 55, 3, 2, 5, 71, 12, 33]

for number in numbers:
    total += number

print("Suma wszystkich elementów listy", numbers, "to", str(total) + ".")

print(sum(numbers))
