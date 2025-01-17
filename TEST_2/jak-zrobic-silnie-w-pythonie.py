def silnia(n):
    if n == 0 or n == 1:  # warunek zakończenia rekurencji
        return 1
    else:
        return n * silnia(n - 1)  # rekurencyjne wywołanie funkcji

# Przykład: obliczamy silnię z 5
print(silnia(5))  # Wydrukuje: 120


# Jak działa ta funkcja?
#
#     Warunek zakończenia: Jeśli n jest równe 0 lub 1, funkcja zwraca 1 (ponieważ 0! = 1! = 1).
#     Rekurencja: Jeśli n > 1, funkcja zwraca n * silnia(n - 1), co powoduje wywołanie funkcji dla n-1, aż osiągnie 1.