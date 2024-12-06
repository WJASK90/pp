prosty_komunikat = "Mam 32 lata!"
proste_komunikaty = "Mieszkam w Rząsce! To w gminie Zabierzów!"

print(prosty_komunikat)
print(proste_komunikaty)


is_student = True
age = 20
is_student and (age < 18)

a = 5
b = 3

print(a & b)

lista_przyklad = [1, 2, 3]
print(lista_przyklad)
print(len(lista_przyklad))

fruits = ["apple", "banana", "orange"]

for i in range(len(fruits)):
    print(fruits[i], end=" ")

print()
print("*" * 10)

for fruit in fruits:
    print(fruit, end=" ")