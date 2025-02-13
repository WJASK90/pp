# Napisz funkcję sprawdzającą, czy podany ciąg znaków jest palindromem
# (czy czyta się tak samo od przodu i od tyłu). Ignoruj wielkość liter oraz spacje.

#definiuje funkcję
def palindrom(sample: str):
    change = sample.lower().replace(" ", "")
    return change == change[::-1]

#lista słów
samples = ["oko", "łóżko", "zakaz", "Robert", "Ala", "palindrom", "atak kata"]

#sprawdzanie palindromu
for sample in samples:
    if palindrom(sample):
        print(f'"{sample}" to palindrom :)')
    else:
        print(f'"{sample}" to nie palindrom :(')