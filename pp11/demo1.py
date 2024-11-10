# wymiana

a = 1
b = 4

print("a =", a, "b =", b)

a, b = b, a

print("a =", a, "b =", b)

numbers = [1, 2, 3]
numbers[0], numbers[1] = numbers[1], numbers[0]
print(numbers)

# [4, 5, 2, 1]
# [4, 2, 1, 5]
# [2, 1, 4, 5]
# [1, 2, 4, 5]