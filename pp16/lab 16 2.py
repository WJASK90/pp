# Napisz, przetestuj i zastosuj własny moduł do obsługi list liczb całkowitych:
# • stwórz modułu o dowolnej nazwie,
# • dodaj funkcję weryfikującą czy podana lista zawiera wyłącznie liczby całkowite,
# • dodaj funkcję sumującą wszystkie liczby z listy,
# • dodaj funkcję zwracającą iloczyn wszystkich liczb z listy,
# • dodaj testy weryfikujące poprawne działanie napisanych funkcji,
# • zaimportuj utworzony moduł i skorzystaj z jego funkcji.

#tworzymy modul numli i go importujemy

import numli

list = [1, 2, 3, 4, 5]

print("Czy lista zawiera tylko liczby całkowite?", numli.is_list_of_integers(list))
print("Suma elementów listy:", numli.sum_list(list))
print("Iloczyn elementów listy:", numli.product_list(list))

