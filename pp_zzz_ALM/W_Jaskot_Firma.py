print("Firma")
print("Program wczytuje pracowników i relacje służbowe między nimi,")
print("a następnie pozwala zadawać pytania o zwierzchników i podwładnych.\n")

# Pracownik
class Pracownik:
    def __init__(self, pid, imie, nazwisko):
        self.pid = pid
        self.imie = imie
        self.nazwisko = nazwisko
        self.szef = None
        self.podwladni = []


# Wczytywanie pracowników
pracownicy = {}

try:
    n = int(input("Podaj liczbę pracowników: "))
except ValueError:
    print("UWAGA! Liczba pracowników musi być liczbą całkowitą!")
    exit()

for _ in range(n):
    linia = input().strip()
    try:
        pid, imie, nazwisko = linia.split(",")
        pid = int(pid)
    except:
        print("UWAGA! Niepoprawny format danych pracownika.")
        exit()

    pracownicy[pid] = Pracownik(pid, imie, nazwisko)

# Wczytywanie relacji
try:
    r = int(input("Podaj liczbę relacji zwierzchnik-podwładny: "))
except ValueError:
    print("UWAGA! Liczba relacji musi być liczbą całkowitą.")
    exit()

for _ in range(r):
    linia = input().strip()
    try:
        szef_id, pod_id = linia.split()
        szef_id = int(szef_id)
        pod_id = int(pod_id)
    except:
        print("UWAGA! Niepoprawny format relacji.")
        exit()

    if szef_id not in pracownicy or pod_id not in pracownicy:
        print("UWAGA! Relacja zawiera nieistniejący identyfikator.")
        exit()

    pracownicy[pod_id].szef = szef_id
    pracownicy[szef_id].podwladni.append(pod_id)


# Menu nawigacyjne
while True:
    print("\nProjekt Firma")
    print("A – zwierzchnik")
    print("B – podwładni")
    print("X – wyjście z programu")

    wybor = input("Wybierz opcję: ").strip().upper()

    if wybor == "X":
        print("Zamykanie programu...")
        break

    # Zwierzchnik
    if wybor == "A":
        try:
            pid = int(input("Podaj identyfikator pracownika: "))
        except ValueError:
            print("UWAGA! Identyfikator musi być liczbą.")
            continue

        if pid not in pracownicy:
            print("UWAGA! Nie ma takiego pracownika.")
            continue

        prac = pracownicy[pid]

        if prac.szef is None:
            print("Prezes")
        else:
            sz = pracownicy[prac.szef]
            print(f"{sz.imie} {sz.nazwisko}")
        continue

    # Podwładni
    if wybor == "B":
        try:
            pid = int(input("Podaj identyfikator pracownika: "))
        except ValueError:
            print("UWAGA! Identyfikator musi być liczbą.")
            continue

        if pid not in pracownicy:
            print("UWAGA! Nie ma takiego pracownika.")
            continue

        prac = pracownicy[pid]
        liczba = len(prac.podwladni)
        print(f"Liczba bezpośrednich podwładnych: {liczba}")
        continue

    print("Nieznana opcja. Spróbuj ponownie.")
