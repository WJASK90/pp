#REKURENCJA - Tabliczka mnozenia

#rekurencja = mechanizmy ktory wywoluje sam siebie

# 2. Korzystając z rekurencji wypisz na ekranie tabliczkę mnożenie do 100.

# 1 x 1 = 1

def show_operation(a, b):
    print(a, "x", b, "=", a * b) #graficznie a x b = a*b
    if a == 10 and b == 10:
        return
    elif a == 10:
       show_operation(a, b + 1)
    else:
        show_operation(a + 1, b)

#wchodzimy z dwoma liczbami, sprawdza warunek czy czasem a i b nie maja wartosci 10, jak obydwa osiagna 10 to zatrzymujemy operacje

show_operation(1, 1)

