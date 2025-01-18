# 1. Wyświetl polski alfabet (tylko małe litery, także litery ze znakami diakrytycznymi)
# wraz z punktami kodowymi dla każdej litery.

# Polski alfabet (małe litery z diakrytycznymi znakami)
polski_alfabet = [
    'a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'q', 'r', 's', 'ś', 't', 'u', 'v', 'w',
    'x', 'y', 'z', 'ź', 'ż'
]

# Wyświetlenie liter alfabetu oraz ich punktów kodowych
for litera in polski_alfabet:
    print(litera + ": " + str(ord(litera)))
