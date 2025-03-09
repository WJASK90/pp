# Ćwiczenie:
#
# Napisz funkcję fibonacci(n: int) -> int, która oblicza n-ty wyraz ciągu Fibonacciego.
# # Opis: Ciąg Fibonacciego zaczyna się od dwóch pierwszych liczb 0 i 1,
# a każda kolejna liczba jest sumą dwóch poprzednich. Przykładowo:
#
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Twoja funkcja powinna zwrócić n-ty wyraz tego ciągu.
#
# Podpowiedzi:
# # Jeśli n jest równe 0, zwróć 0.
# Jeśli n jest równe 1, zwróć 1.
# Dla innych wartości, każdą kolejną liczbę obliczając jako sumę dwóch poprzednich.

# Przykłady:
# print(fibonacci(0))  # 0
# print(fibonacci(1))  # 1
# print(fibonacci(5))  # 5
# print(fibonacci(10)) # 55


def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n < 1:
        return None
    if n < 3:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(5))
print(fibonacci(10))

#ANALIZA KODU:
#WARUNKI POCZĄTKOWE

# if n == 0:
#     return 0
# if n < 1:
#     return None
# if n < 3:
#     return 1


# Pierwszy warunek (if n == 0): Jeśli n wynosi 0, to funkcja zwróci 0, ponieważ 0-ty element ciągu Fibonacciego to właśnie 0 (zgodnie z definicją ciągu).
# Drugi warunek (if n < 1): Ten warunek jest trochę zbędny, ponieważ wcześniej masz już warunek na n == 0. Ten kod sprawdza, czy n jest mniejsze niż 1, ale nie ma sensu w kontekście ciągu Fibonacciego,
# ponieważ w definicji ciągu nie ma indeksów ujemnych. Można to usunąć, bo ciąg Fibonacciego zaczyna się od n = 0.
# Trzeci warunek (if n < 3): Jeśli n jest mniejsze niż 3 (czyli n == 1 lub n == 2), to zwracasz 1, ponieważ 1-ty i 2-gi element ciągu Fibonacciego to oba 1. To jest prawidłowe, ponieważ:
# Fibonacci(1) = 1
# Fibonacci(2) = 1

# Rekurencyjna część:
# Jeśli n jest większe niż 2, funkcja wywołuje się rekurencyjnie dla dwóch poprzednich liczb ciągu:
#
# fibonacci(n - 1) oblicza (n-1)-ty element ciągu Fibonacciego.
# fibonacci(n - 2) oblicza (n-2)-ty element ciągu Fibonacciego.
# Następnie funkcja zwraca sumę tych dwóch wyników, co odpowiada zasadzie ciągu Fibonacciego, czyli F(n) = F(n-1) + F(n-2).
#
# Działanie kodu na przykładzie:
# Wywołanie fibonacci(0):
#
# n == 0, więc zwróci 0.
# Wywołanie fibonacci(1):
#
# n == 1, więc zwróci 1.
# Wywołanie fibonacci(5):
#
# Dla fibonacci(5), wywołujesz:
# fibonacci(4) + fibonacci(3)
# Dla fibonacci(4), wywołujesz:
# fibonacci(3) + fibonacci(2)
# Dla fibonacci(3), wywołujesz:
# fibonacci(2) + fibonacci(1) → zwróci 1 + 1 = 2
# fibonacci(2) → zwróci 1
# Wynik dla fibonacci(4) → 2 + 1 = 3
# Dla fibonacci(3), wywołujesz:
# fibonacci(2) + fibonacci(1) → zwróci 1 + 1 = 2
# Wynik dla fibonacci(5) → 3 + 2 = 5
# Wywołanie fibonacci(10):
#
# Funkcja będzie wywoływać się rekurencyjnie przez wiele poziomów, aż do podstawowych przypadków (fibonacci(1) i fibonacci(2)), a wynik będzie wynosił 55 po obliczeniu wszystkich kroków.