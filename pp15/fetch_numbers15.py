numbers = []
counter = 1

for i in range(5):
    number = int(input("Podaj liczbę całkowitą: "))
    numbers.append(number)

print(numbers)

while True:
    if counter > 5:
        break
    try:
        number = int(input("Podaj liczbę całkowitą: "))
        numbers.append(number)
        counter += 1
    except:
        print("To nie jest liczba całkowita! :O Spróbuj ponownie :) ")

print(numbers)