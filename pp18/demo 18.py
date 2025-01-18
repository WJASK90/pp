# txt = "Ala ma kota"
#
# print(txt)
# print(len(txt))
# print(len(''))
# print(len("\n\t\\"))

# txt = """To jest tekst.
#                 Ten tekst ma kilka linii
# Raz dwa trzy."""
#
# print(txt)
#
# txt1 = """a
# b
# c"""
#
# print(len(txt1)) # wynik 5 bo licza sie spacje
# print(len("a\nb\nc"))
#
# print(repr(txt1)) #wynik 'a\nb\nc'

# str1 = "a"
# str2 = "b"
#
# print(str1 + str2)
# print(str2 + str1)
# print(5 * str1)
# print(str1 * 5)
#
# str1 += str2
# str1 *= 10
#
# print(str1)
#
# # punkt kodowy - liczba reprezentujaca dany znak
#
# char1 = "a"
# char2 = " " #spacja
#
# print(ord(char1)) #jaka ma wartosc male a ?
# print(ord(char2))
# print(ord("ę")) #polski znak diaktryczny
# print(hex(ord("ę")))
# print("\u0119") #wartosc heksadecymalna

#znak moze byc zakodowany za pomoca 1, 2, 3 lub 4 bajtow
c = "a"
print(c, ord(c), hex(ord(c)), c.encode())

# znak EURO €
c = "\u20AC"
print(c, ord(c), hex(ord(c)), c.encode())

print(chr(97))
print(chr(945)) #wynik α czyli znak Alfa

print("a" == chr(ord("a"))) #zamiena A na liczbe a potem A na znak

#      0123456789    wartości indeksów
txt = "Ala ma kota." #mozemy po tym indeksowac!

print(txt[7]) #k

for c in txt:
    print(c, end=" ")

print()

for i in range (len(txt)):
    print(i, txt[i])