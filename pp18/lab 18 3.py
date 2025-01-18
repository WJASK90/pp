#szyfr Cezara? Bierzesz alfabet, przesuwasz na dana liczbe
#w cwiczeniu idziemy od tylu

# 3. Rozszyfruj poniższą wiadomość wiedząc, że została ona zaszyfrowana szyfrem
# cezara z parametrem przesunięcia równym 3.
# VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ

#ABCDEFGHIJKLMNOPQRSTUVWXYZ

delta = 3

# print(ord('A'))
# print(ord('Z'))
#
# for c in range(ord('A') + delta, ord('Z') + 1 + delta):
#     print(chr(c), end="")
#
# print()
#
# for c in range(ord('A') + delta, ord('Z') + 1 + delta):
#     if c > ord('Z'):
#         c -= ord('Z') - ord('A') + 1
#     print(chr(c), end="")

def decode_letter(letter, delta): #funkcja do dekodowania litery
    if letter <'A' or letter > 'Z':
        return letter
    n = ord(letter) - delta
    if n < ord('A'):
        n += ord('Z') - ord('A') + 1
    return chr(n)

print(decode_letter('J', delta))

def decode(string, delta): #funkcja do dekodowania wyrazow
    decoded = ""
    for letter in string:
        decoded += decode_letter(letter, delta)
    return decoded

print(decode("VCBIU", delta))
print(decode("VWXGLD SRGBSORPRZH - SURJUDPLVWD SBWKRQ", delta))


