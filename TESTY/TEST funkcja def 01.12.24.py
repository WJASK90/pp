# https://www.learnpython.org/pl/Funkcje#:~:text=Funkcje%20s%C4%85%20definiowane%20z%20u%C5%BCyciem%20s%C5%82owa%20kluczowego%20def%2C,puste.%20def%20przywitanie%28%29%3A%20print%20%22Pozdrowienia%20z%20mojej%20funckji%21%22

# Funkcje są definiowane z użyciem słowa kluczowego def, po którym umieszcza się nazwę funkcji,
# a potem nawiasy.
# Jeżeli funkcja nie wymaga informacji z zewnątrz nawiasy pozostawiamy puste.

# Aby przerwać działanie funkcji i zwrócić wartość, musisz użyć słowa return,
# a za nim umieścić zwracaną wartość. Jeżeli pominiesz wartość, to funkcja tylko zakończy swoje
# działanie i nic nie zwróci.

imie_1 = "Wojtek"
nazwisko_1 = "Jaskot"

def przywitanie_osoby():
    print("Witaj osobo o imieniu " + imie_1 + " i o nazwisku " + nazwisko_1)

przywitanie_osoby()
