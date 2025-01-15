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