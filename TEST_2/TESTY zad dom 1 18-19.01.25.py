# Napisz funkcję sprawdzającą, czy podany ciąg znaków jest palindromem
# (czy czyta się tak samo od przodu i od tyłu). Ignoruj wielkość liter oraz spacje.


def is_palindrome(s):
    # Usuwamy spacje i zmieniamy na małe litery
    s = s.replace(" ", "").lower()

    # Porównujemy ciąg z jego odwrotnością
    return s == s[::-1]

# Testowanie funkcji
test_string = input("Podaj ciąg znaków do sprawdzenia, czy jest palindromem: ")
if is_palindrome(test_string):
    print("Tak, to jest palindrom!")
else:
    print("Nie, to nie jest palindrom!")
