# 3. Napisz program przechowujący informacje o pracownikach:
# • możliwe typy osób to: menedżer, zwykła osoba, pracownik,
# • każda z osób powinna posiadać imię,
# • tylko menadżer będzie miał przydzielony projekt,
# • zwykła osoba nie będzie posiadała informacji o wynagrodzeniu.
# Zademonstruj działanie programu przechowując listę różnych typów osób/pracowników.


class Osoba:
    def __init__(self, imie):
        self.imie = imie

    def __str__(self):
        return f"Imię: {self.imie}"


class Pracownik(Osoba):
    def __init__(self, imie, wynagrodzenie):
        super().__init__(imie)
        self.wynagrodzenie = wynagrodzenie

    def __str__(self):
        return f"Imię: {self.imie}, Wynagrodzenie: {self.wynagrodzenie}"


class ZwyklaOsoba(Osoba):
    def __init__(self, imie):
        super().__init__(imie)

    def __str__(self):
        return f"Imię: {self.imie}, Zwykła osoba (brak wynagrodzenia)"


class Menedzer(Pracownik):
    def __init__(self, imie, wynagrodzenie, projekt):
        super().__init__(imie, wynagrodzenie)
        self.projekt = projekt

    def __str__(self):
        return f"Imię: {self.imie}, Wynagrodzenie: {self.wynagrodzenie}, Projekt: {self.projekt}"


# Różne typy osób
osoby = [
    Menedzer("Radosław Miłosz", 10000, "Projekt A"),
    ZwyklaOsoba("Helena Pakulska"),
    Pracownik("Igor Wawrzyk", 5000),
    Menedzer("Kornelia Łodzik", 12000, "Projekt B"),
    ZwyklaOsoba("Sebastian Bąk"),
]

# Wyświetlanie informacji na temat pracowników
for osoba in osoby:
    print(osoba)



