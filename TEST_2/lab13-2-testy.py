# Korzystając z rekurencji wypisz na ekranie tabliczkę mnożenie do 100.

def multiple_table(a, b):
    print(a, "X", b , "=", a*b)
    if a == 10 and b == 10: #sprawdzamy czy a i b nie osiagnely wartosci 10
        return
    elif a == 10: #sprawdz czy b to 10 i tez wyjdz
        multiple_table(1, b +1) #jesli a osiaga 10 to a sie resetuje i liczy od 1 a b leci dalej
    else:
        multiple_table(a + 1, b)

multiple_table(1, 1)