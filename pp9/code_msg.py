# rozszyfruj wiadomość
# szyfr: dla każdego znaku zmieniono 4 bit na przeciwny
# bity liczymy od najmniej znaczącego
# Xq|`gf(bm{|(nibfq)

#aby odkryc wartosc numeru to uzywamy funkcji ord jak np print(ord("c")) da nam 99, a zeby z liczby miec znak piszemy chr(99)
print(ord("c")), chr(99)

print("{:08b}".format(ord("c"))) #bierzemy liczbe w formacie i zamienamy ja w bity! A 4 bit musimy zmienic na przeciwny, wg cwiczenia
# 01100011 -> chcemy zmienic 4 bit (od prawej)
# 00001000 -> maska pozwala nam wyizolować dany bit
# 01101011 -> używamy XORa (alternatywa rozłączna), do zmiany bitu!

print("{:08b}".format(1 << 3))
print("{:08b}".format(ord("c") ^ (1 << 3)))

print()

str = "Xq|`gf(bm{|(nibfq)"
for c in str:
    print(chr(ord(c) ^ (1 << 3)), end="")

