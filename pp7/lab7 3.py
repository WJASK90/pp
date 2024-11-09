#zadanie 3 - napisz gre w zgadywanie liczby od 1 do 10, gracz ma 3 szanse, po nieudanej probie nalezy sie podpowiedz np liczba do odgadnieca ma byc parzysta itd

import random
number = random.randint(1, 10)
msg = "Zgadnij jaką liczbę mam na myśli (od 1 do 10): "
guess = int(input(msg))

if guess == number:
    print("Gratulacje! Odgadłeś poprawną liczbę!")
else:
    msg = "Masz kolejną szansę, moja liczba jest: "
    if number & 2 == 0:
        msg = msg + "parzysta: "
    else:
        msg = msg + "nieparzysta: "
    guess = int(input(msg))
    if guess == number:
        print("Gratulacje! Udało ci się odgadnąć za drugim razem!")
    else:
        msg = "Masz ostatnią szansę moja liczba jest "
        if number > 5:
            msg += "większa niż "
        else:
            msg += "mniejsza lub równa "
        msg += "pięć: "
        guess = int(input(msg))
        if guess == number:
            print("Gratulacje! Udało się za trzecim razem!")
        else:
            print("Co za pech, myślałem o liczbie " + str(number) + ".")