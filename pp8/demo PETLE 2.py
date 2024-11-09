#SILNIA 3! = 1 * 2 * 3 = 6 (silnia = factorial)

number = 5

factorial = 1
for i in range(1, number + 1):
    factorial *= i # factorial = factorial * i

while number:
    factorial *= number
    number -= 1 # number = number - 1

print(factorial)