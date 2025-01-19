# program symulujący rzuty dwiema kostkami do gry
# rzucamy dwiema kostkami do momentu aż nie wyrzucimy dubletu

import random

class Dice:
    def __init__(self):
        self.value = None

    def throw(self):
        self.value = random.randint(1, 6)

    def __str__(self):
        return f"[{self.value}]" #zwracam jako ciag znakow wyrzucony wynik np. [4]

class DicePair:
    def __init__(self):
        self.pair = [Dice(), Dice()]

    def throw(self):
        self.pair[0].throw() #bierzemy obiekt o indeksie zero i rzucam, PIERWSZA KOSC
        self.pair[1].throw() #bierzemy obiekt o indeksie jeden i rzucam, DRUGA KOSC

    def __str__(self):
        return str(self.pair[0]) + str(self.pair[1])

    def is_double(self):
        return self.pair[0].value == self.pair[1].value #czy na dwoch kosciach sa te same wartosci

dices = DicePair()
counter = 1

while True: #rzucamy do momentu uzyskania dubletu
    dices.throw() #rzuc koscmi
    print(dices) #tu sie zbieraja wyniki, czyli to co wyszlo na rzutach
    if dices.is_double(): #w wypadku dubletu zatrzymaj
        break
    counter += 1


