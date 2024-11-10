numbers = [4, 5, 2, 1, 123, 9, 40, 39, 38, 100, 0, 0, 0, 111]
swapped = True

while swapped:
    swapped = False
    for i in range(len(numbers) - 1):  # dlaczego -1? Bo chcemy iterować
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True

print(numbers)

numbers = [4, 5, 2, 1]
numbers.sort(reverse=True)

print(numbers)
numbers = ["C", "A", " ", "B"]
numbers.sort(reverse=True)

print(numbers)
