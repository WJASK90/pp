# 1. Napisz wyszukiwarkę numerów telefonów:
# • zdefiniuj słownik par imię -> numer telefonu,
# • zapytaj użytkownika o imię,
# • wyświetl użytkownikowi numer telefonu lub informację o jego braku.

#klasyczny slownik to ksiazka telefoniczna, dobry przyklad --> slowniki sa ZMIENNE

phones_1 = {"Tomasz": 39555, "Agata": 39666, "Karol": 39777, "Cezary": 39888} # klucz:wartość

select_name = input("Potrzebujesz numeru telefono do kogo? Wybierz imię Tomasz/Agata/Karol/Cezary: ")
for i in phones_1:
    if i in phones_1.keys():
        print(phones_1.get(select_name, "Brak takiej osoby w książce telefonicznej"))
        break



