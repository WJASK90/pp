#wycinki

txt = "Ala ma kota."

print(txt[4:6]) #ma
print(txt[7:]) #kota
print(txt[-1:])
print(txt[2::3])

print(ord('a'))
print(ord('z'))

#teraz wyswietlimy alfabet iterujac

# alphabet = ""
# for i in range(ord('a'), ord('z')+1):
#     print(chr(i), end="")
#
# print(alphabet)

alphabet = ""
for i in range(ord('a'), ord('z')+1):
    alphabet += chr(i)

print(alphabet)
print("A" not in alphabet) #wynik  True

print("cba" in alphabet)

#del alphabet usunie wszystko

alphabet = alphabet + ">"
print(alphabet) #ciag znakow ktory laczy nowy ze starym

print(min([1, 2, 3]))
print(max([1, 2, 3]))
print(min("abcABC")) #wynik A bo ma najmniejszą wartość kodową ASCII

#funkcja index zwraca wartosc ASCII

# print(alphabet.index("W"))
print(alphabet.index("c"))
print("aaabbbccc".index("c"))
print([1,2,3].index(3))
print(list(alphabet))
print("Ala ma kota") #ile jest spacji? uzywamy count
print("Ala ma kota.".count("a")) #wynik 3 !!! :-O
