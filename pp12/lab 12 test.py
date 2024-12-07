# 1. Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
# ilość razy, w poziomie lub w pionie.

#funkcja aby wywolywac gwiazdki *

sign_choice = input("Wpisz znak: ")
multiple = int(input("Ile razy wyświetlić znak? " ))
sign_x_multiple = sign_choice * multiple
direction = input("Czy ma być w PIONIE czy w POZIOMIE? Napisz PI lub PO: ")


def show_sign(how_many): #dodajemy how_many czyli ile razy wyswietlic
    # for i in range(how_many):
        if direction == "PI":
            print(sign_x_multiple, end= "\n")
        if direction == "PO":
            print(sign_x_multiple, end="")


show_sign(1)

#zmien to na listy, wtedy elementy sa wyswietlane po przecinku i mozesz je wyswietlac w pionie lub nie!!!!!!!! dzieki, Krzychu