# . Dokonaj odpowiednich zmian w programie do rzucania kośćmi do gry (dices.py), aby
# zabezpieczyć zmienne instancji przed przypadkowym nadpisaniem (enkapsulacja).


import random

class Dice:
    def __init__(self):
        self.__value = None

    def get_value(self):
        return self.__value

    def throw(self):
        self.__value = random.randint(1, 6)

    def __str__(self):
        return f"[{self.__value}]" #zwracam jako ciag znakow wyrzucony wynik np. [4]

class DicePair:
    def __init__(self):
        self.__pair = [Dice(), Dice()]

    def throw(self):
        self.__pair[0].throw() #bierzemy obiekt o indeksie zero i rzucam, PIERWSZA KOSC
        self.__pair[1].throw() #bierzemy obiekt o indeksie jeden i rzucam, DRUGA KOSC

    def __str__(self):
        return str(self.__pair[0]) + str(self.__pair[1])

    def is_double(self):
        return self.__pair[0].get_value() == self.__pair[1].get_value() #czy na dwoch kosciach sa te same wartosci

dices = DicePair()
counter = 1

while True: #rzucamy do momentu uzyskania dubletu
    dices.throw() #rzuc koscmi
    print(dices) #tu sie zbieraja wyniki, czyli to co wyszlo na rzutach
    if dices.is_double(): #w wypadku dubletu zatrzymaj
        break
    counter += 1