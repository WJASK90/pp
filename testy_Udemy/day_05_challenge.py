# Generate the password in sequence. Letters, then symbols, then numbers. If the user wants
#
# 4 letters 2 symbols and 3 numbers then the password might look like this:

# fgdx$*924

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



letters_generator = []
for char in range(0, nr_letters):
    letters_generator.append(random.choice(letters))
# print(letters_generator)

symbols_generator = []
for symbol in range (0, nr_symbols):
    symbols_generator.append(random.choice(symbols))
# print(symbols_generator)

nr_numbers_generator = []
for number in range(0, nr_numbers):
    nr_numbers_generator.append(random.choice(numbers))
# print(nr_numbers_generator)

password_generator = letters_generator + symbols_generator + nr_numbers_generator
random.shuffle(password_generator)
print(password_generator)