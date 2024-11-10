# własności list
# - jest uporządkowana

numbers = [1, 2, 3]
print(numbers)

# - pozwala przechowywać duplikaty
numbers = [1, 1, 1]
print(numbers)

# - pozwala przechowywac elementy o roznych typach

numbers = [1, "jeden", True, 2.0, 9]
print(numbers)

# - kazdy element list posiada indeks
# - elementy listy są zawsze numerowane od 0

print(numbers[0], numbers[1])

#           0           1       2
fruits = ["apple", "banana", "cherry"]
print(fruits[2])

#           -3       -2        -1
fruits = ["apple", "banana", "cherry"]
print(fruits[-1], fruits[-3])