#operatory bitowe

a = 5
b = 3

# koniunkcja bitowa
print(a, "&", b, "=", a & b)
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a & b))

# alternatywa bitowa ze znakiem | ktory czytamy "pajp"
print(a, "|", b, "=", a | b)
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a | b))

# koniunkcja rozłączna bitowa (alternatywa rozłączona)
print(a, "^", b, "=", a ^ b)
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a ^ b))

# przesunięcie bitowe w prawo >> (patrz na rezultat w konsoli RUN, przesuwasz o 3 w prawo i 101 "spadly w dol" i masz 0
print(a, ">>", b, "=", a >> b)
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a >> b))

# przesunięcie bitowe w lewo <<
print(a, "<<", b, "=", a << b)
print("{:08b}".format(a))
print("{:08b}".format(b))
print("-" * 8)
print("{:08b}".format(a << b))

# negacja bitowa ~ jezeli bitowo negujemy piatke, to dziesietnie dostajemy -6... Czemu?!
#kazdy pojednyczy bit zostalo zanegowany, 1 zanegowana i zamienila sie w 0,
print(a, "~", b, "=", ~a)
print("{:08b}".format(a))
print("-" * 8)
print("{:08b}".format(~a))