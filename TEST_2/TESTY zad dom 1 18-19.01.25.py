# Napisz funkcję sprawdzającą, czy podany ciąg znaków jest palindromem
# (czy czyta się tak samo od przodu i od tyłu). Ignoruj wielkość liter oraz spacje.


# def is_palindrome(s):
#     # Usuwamy spacje i zmieniamy na małe litery
#     s = s.replace(" ", "").lower()
#
#     # Porównujemy ciąg z jego odwrotnością
#     return s == s[::-1]
#
# # Testowanie funkcji
# test_string = input("Podaj ciąg znaków do sprawdzenia, czy jest palindromem: ")
# if is_palindrome(test_string):
#     print("Tak, to jest palindrom!")
# else:
#     print("Nie, to nie jest palindrom!")


# def palindrom(text: str):
#         transform = text.lower().replace(" ", "")
#         return transform == transform[::-1]
#
# texts = ["oko", "łóżko", "zakaz", "Robert", "Ala", "Palindrom", "Atak kata"]
#
# if palindrom(texts):
#     print("Tak, to jest palindrom!")
# else:
#     print("Nie, to nie jest palindrom!")

# for text in texts:
#     print(f'"{text}" is {palindrom(text)}')

def palindrom(sample: str):
    change = sample.lower().replace(" ", "")
    return change == change[::-1]

samples = ["oko", "łóżko", "zakaz", "Robert", "Ala", "palindrom", "atak kata"]

for sample in samples:
    if palindrom(sample):
        print(f'"{sample}" to palindrom :)')
    else:
        print(f'"{sample}" to nie palindrom :(')
