import random

# Wprowadzenie do programu
print("Brydżowa ręka")
print()
print("Program losuje przykładową rękę")
print("13 kart dla jednego gracza brydża.")
print()
print("Wyświetlane są:")
print("- karty pogrupowane według kolorów")
print("- liczba punktów Miltona-Worka")
print()
print("Naciśnij ENTER aby losować rękę.")
print("Wpisz X aby zakończyć program.")
print()


# Dane kart
kolory = ["Piki", "Kiery", "Kara", "Trefle"]

wartosci = [
    "A", "K", "D", "W",
    "10", "9", "8", "7",
    "6", "5", "4", "3", "2"
]

punkty_figur = {
    "A": 4,
    "K": 3,
    "D": 2,
    "W": 1
}


# Główna pętla programu
while True:

    wybor = input("\nTwój wybór: ").strip().upper()

    # Zakończenie programu
    if wybor == "X":
        print("Koniec programu.")
        break

    # Obsługa błędnych danych
    if wybor != "":
        print("UWAGA! Naciśnij ENTER lub wpisz X.")
        continue

    try:

        # Tworzenie talii
        talia = []

        for kolor in kolory:
            for wartosc in wartosci:
                karta = (kolor, wartosc)
                talia.append(karta)

        # Losowanie ręki
        reka = random.sample(talia, 13)

        # Grupowanie kart
        grupy = {}

        for kolor in kolory:
            grupy[kolor] = []

        for kolor, wartosc in reka:
            grupy[kolor].append(wartosc)

        # Sortowanie kart
        for kolor in kolory:

            grupy[kolor].sort(
                key=lambda karta: wartosci.index(karta)
            )

        # Liczenie punktów
        punkty = 0

        for kolor, wartosc in reka:

            if wartosc in punkty_figur:
                punkty += punkty_figur[wartosc]


        # Wyświetlanie wyników
        print()

        for kolor in kolory:

            if grupy[kolor]:
                karty = " ".join(grupy[kolor])
            else:
                karty = "–"

            print(f"{kolor}: {karty}")

        print()
        print("Pkt:", punkty)

    except Exception as blad:
        print("Wystąpił nieoczekiwany błąd.")
        print("Treść błędu:", blad)