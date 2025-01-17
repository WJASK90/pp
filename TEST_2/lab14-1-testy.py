# 1. Napisz wyszukiwarkę numerów telefonów:
# • zdefiniuj słownik par imię -> numer telefonu,
# • zapytaj użytkownika o imię,
# • wyświetl użytkownikowi numer telefonu lub informację o jego braku.

phones = {
    "Adam": 123123123,
    "Karol": 222333444,
    "Mariola": 777777777,
    "Iza": 990990990
}

while True:
    name = input("Podaj imię: ")
    if name == "":
        break
    if name in phones:
        print("Telefon:", phones[name])
    else:
        print("Nie znaleziono telefonu dla imienia", name)