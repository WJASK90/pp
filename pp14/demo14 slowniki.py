#klasyczny slownik to ksiazka telefoniczna, dobry przyklad --> slowniki sa ZMIENNE

phones = {"Tomek": 555555, "Ada" : 123123123, "Karol": 444333222} # klucz:wartość
print(phones)


phones1 = {"Tomek": 555555, "Ada" : 123123123, "Karol": 444333222, "Tomek": 99999} # klucz:wartość
print(phones1) #te same klucze nadpisuja wartosc jesli jest inna!

#stworzmy slownik jezyka angielskiego
animals_dict = {
    "kot": "cat",
    "pies": "dog",
    "chomik": "hamster",
}

print(animals_dict["kot"]) #tutaj tez mozemy sie odwolac to danego elementu, ale wpisujemy KLUCZ a nie NUMER INDEKSU
print(animals_dict.get("kot")) #rowniez dostajemy KLUCZ.
#roznica miedzy [] a .get jest taka ze jesli w pierwszym print wpiszemy nieistniejacy klucz, to bedzie ERROR, a .get nie da bledu tylko None. Mozemy wpisac obok inna
#wartosc ktora nam pokaze jak nie bedzie elementu, patrz na dole
print(animals_dict.get("słoń", "brak takiego klucza w słowniku"))
print(animals_dict.get("kot", "brak takiego klucza w słowniku"))

words = ["kot", "lew", "chomik"]

# for word in words:
#     print(word, "->", animals_dict[word]) #wystąpi błąd bo nie mam LEW w słowniku

for word in words:
    if word in animals_dict.keys(): # metoda keys() zwraca wszystkie klucze słownika
        print(word, "->", animals_dict[word])
    else:
        print("Nie znaleziono słowa {} w słowniku".format(word)) #omijamy to używając warunkow if, else itd

for key in animals_dict.keys():
    print(key, "->", animals_dict[key]) #przechodzimy po slowach w slowniku

for value in animals_dict.values():
    print(value) #dostajemy tylko wartości

print()

for PL, EN in animals_dict.items():
    print(PL, "->" ,EN)

#modyfikacje, zmienianie

animals_dict1 = {
    "kot": "cat",
    "pies": "dog",
    "chomik": "hamster",
}

animals_dict1["świnka"] = "pig" #dodajem klucz:wartość
print(animals_dict1)
print(animals_dict1.popitem())
print(animals_dict1)

animals_dict.clear() #czyścimi słownik
print(animals_dict)