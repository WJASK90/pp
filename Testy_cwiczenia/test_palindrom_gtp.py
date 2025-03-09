# Ćwiczenie:
#
# Napisz funkcję is_palindrome(s: str) -> bool, która sprawdza, czy podany łańcuch znaków (string) jest palindromem. Palindrom to słowo, zdanie lub liczba, która czytana od tyłu jest taka sama jak od przodu (np. "kajak", "madam", "level").
#
# Podpowiedzi:
#
# Funkcja powinna ignorować spacje i wielkość liter, więc "A man a plan a canal Panama" to również palindrom.
# Zwróć True, jeśli tekst jest palindromem, w przeciwnym razie False.

# PRZYKŁAD:
# is_palindrome("kajak") # powinno zwrócić True
# is_palindrome("hello") # powinno zwrócić False
# is_palindrome("A man a plan a canal Panama") # powinno zwrócić True

import re

def is_palindrome(s: str) -> bool:
    # Usuwamy wszystko, co nie jest literą
    clean_string = re.sub(r'[^a-zA-Z]', '', s.lower()) #mozliwe dzieki import re
    return clean_string == clean_string[::-1]


print(is_palindrome("Panama"))
print(is_palindrome("oko"))
print(is_palindrome("zakaz"))
print(is_palindrome("Robert"))