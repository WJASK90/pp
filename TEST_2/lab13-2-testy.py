# Korzystając z rekurencji wypisz na ekranie tabliczkę mnożenie do 100.

def multiple_table(a, b):
    print(a, "X", b , "=", a*b)
    if a == 10 and b == 10: #sprawdzamy czy a i b nie osiagnely wartosci 10
        return
    elif a == 10: #sprawdz czy a to 10 i tez wyjdz
        multiple_table(1, b +1) #jesli a osiaga 10 to a sie resetuje i liczy od 1 a b leci dalej
    else:
        multiple_table(a + 1, b)

multiple_table(1, 1)



#wersja alternatywna

# def multiple_table(a, b):
#     if a > 10:  # zakończenie po osiągnięciu 10 dla a
#         return
#     if b > 10:  # zakończenie po osiągnięciu 10 dla b
#         multiple_table(a + 1, 1)  # resetujemy b i przechodzimy do kolejnego a
#     else:
#         print(a, "X", b, "=", a * b)  # wypisanie wyniku
#         multiple_table(a, b + 1)  # rekurencyjnie przechodzimy do następnego b
#
# multiple_table(1, 1)

#WYTLUMACZENIE
#Dlaczego ta wersja jest lepsza?
    #
    # Lepsza czytelność: warunki zatrzymania rekurencji są teraz łatwiejsze do zrozumienia.
    # Uproszczona logika: po prostu resetujemy b przy przekroczeniu wartości 10 i przechodzimy do kolejnej wartości a.
    # Efektywność: proces wyjścia z rekurencji jest bardziej jednoznaczny.