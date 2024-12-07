# 1. Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
# ilość razy, w poziomie lub w pionie.

#funkcja aby wywolywac gwiazdki *

sign_choice = input("Wpisz znak: ")
multiple = int(input("Ile razy wyświetlić znak? " ))
# vert =
# hor =

def show_sign(how_many): #dodajemy how_many czyli ile razy wyswietlic
    print(sign_choice * multiple)

show_sign(5)
show_sign(8)
show_sign(1)