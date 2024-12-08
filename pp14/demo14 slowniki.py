#klasyczny slownik to ksiazka telefoniczna, dobry przyklad

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
