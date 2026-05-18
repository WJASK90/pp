print("Szach czy nie?")
print("Program który pozwala ustawić dwie wieże oraz jednego hetmana na szachownicy cyfrowej,")
print("następnie sprawdza, czy wybrane pole jest szachowane (czy nie).\n")

# Pozycje na start
w1 = "a1"
w2 = "h1"
h = "d1"

# Sprawdzanie poprawności pola
def poprawne_pole(p):
    if len(p) != 2:
        return False
    kol, rzad = p[0], p[1]
    return kol in "abcdefgh" and rzad in "12345678"

# Funkcja sprawdzająca: figura atakuje pole
def wieza_atakuje(figura, pole):
    return figura[0] == pole[0] or figura[1] == pole[1]

def hetman_atakuje(figura, pole):
    # Hetman = wieża + goniec
    if wieza_atakuje(figura, pole):
        return True
    # ukośne
    return abs(ord(figura[0]) - ord(pole[0])) == abs(int(figura[1]) - int(pole[1]))

#PĘTLA
while True:
    print("\nProjekt Szach czy nie?")
    print("0 – pozycje figur")
    print("1 – wieża 1")
    print("2 – wieża 2")
    print("3 – hetman")
    print("? – szach?")
    print("X – wyjście z programu")

    wybor = input("Wybierz opcję: ").strip()

    # Wyjście
    if wybor.upper() == "X":
        print("Zamykanie programu...")
        break

    # Pozycje figur
    if wybor == "0":
        print(f"Wieża 1: {w1}")
        print(f"Wieża 2: {w2}")
        print(f"Hetman : {h}")
        continue

    # Zmiana pozycji: wieża 1
    if wybor == "1":
        nowa = input("Podaj nową pozycję wieży 1: ").strip().lower()
        if poprawne_pole(nowa):
            w1 = nowa
            print(f"Wieża 1 ustawiona na {w1}")
        else:
            print("UWAGA! Niepoprawne pole!")
        continue

    # Zmiana pozycji: wieża 2
    if wybor == "2":
        nowa = input("Podaj nową pozycję wieży 2: ").strip().lower()
        if poprawne_pole(nowa):
            w2 = nowa
            print(f"Wieża 2 ustawiona na {w2}")
        else:
            print("UWAGA! niepoprawne pole!")
        continue

    # Zmiana pozycji: hetman
    if wybor == "3":
        nowa = input("Podaj nową pozycję hetmana: ").strip().lower()
        if poprawne_pole(nowa):
            h = nowa
            print(f"Hetman ustawiony na {h}")
        else:
            print("UWAGA! Niepoprawne pole!")
        continue

    # Sprawdzanie szacha CZY nie
    if wybor == "?":
        pole = input("Podaj pole do sprawdzenia: ").strip().lower()
        if not poprawne_pole(pole):
            print("UWAGA! Niepoprawne pole!")
            continue

        szach = (
            wieza_atakuje(w1, pole) or
            wieza_atakuje(w2, pole) or
            hetman_atakuje(h, pole)
        )

        if szach:
            print(f"Pole {pole} JEST szachowane.")
        else:
            print(f"Pole {pole} NIE jest szachowane.")
        continue

    # opcja nieprzewidziana
    print("Nieznana komenda, spróbuj ponownie.")
