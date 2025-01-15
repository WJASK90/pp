#REKURENCJA SUMOWANIE LICZB

def suma(n):
    if n == 1:  # Warunek zakończenia rekurencji
        return 1
    else:
        return n + suma(n - 1)  # Rekurencyjne wywołanie funkcji


print(suma(5))

#w praktyce to tak jakbyśmy dodawali 5 coraz mniejszą o jeden, czyli:
#5 + 4 + 3 + 2 + 1 = 15!!! :O

#REKURENCJA SILNIA (Factorial)

def silnia(n):
    if n == 0:  # Warunek zakończenia rekurencji
        return 1
    else:
        return n * silnia(n - 1)  # Rekurencyjne wywołanie funkcji

print(silnia(5))

#5 x 4 x 3 x 2 x 1 = 120!!!!!!!!!!!!!!! O_o

#WAZNE
# W każdej funkcji rekurencyjnej musisz ustalić warunek, który zatrzyma dalsze wywołania.
# Gdy dojdzie do tego punktu, rekurencja kończy się.

# def inverse_counting(n):
#     if n == 0:
#         return
#     else:
#         return n - 1
#
# print(inverse_counting(5))

#powyzej, Funkcja zwraca tylko n−1n−1,
# ale nie wywołuje samej siebie ponownie, więc rekurencja się nie odbywa.

# Kiedy wywołasz inverse_counting(5), funkcja zwróci wartość 5−1=45−1=4,
# ale nie kontynuuje się dalej. W efekcie nie zobaczysz żadnych wypisanych liczb.

# W tej wersji brakuje najważniejszego elementu, czyli wywołania samej siebie (rekurencji)
# z nowym argumentem, czyli inverse_counting(n - 1).

def inverse_counting(n):
    if n == 0:
        return
    else:
        print(n)
        inverse_counting(n - 1) #Rekurencja!

print(inverse_counting(5))