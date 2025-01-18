import module

# print(dir(module))
# help(module)

print("Czy to jest ciąg znaków?", module.is_string("test"))
print("Suma elementów listy:", module.sum_list_elem([3, 4, 5, 2, 83]))

print(module.__name__) #otrzymujemy nazwe modulu

#PROSZE PAMIETAC ze przy kazdym imporcie np. import module (importuje wszystko co jest w module.py) powoduje uruchomienie
# calego kodu module.py, wiec nawet jak zaimportujemy wiecej niz raz np trzy razy import module to kody jest wykonywany TYLKO RAZ
