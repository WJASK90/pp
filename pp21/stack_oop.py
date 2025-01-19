class Stack: # definiowanie klasy stosu --> bedzie mogla miec rozne zachowania, mozemy zdefiniowac metode init (NIE SA POTRZEBNE NAWIASY w porowaniu do funkcji
    def __init__(self): #specjalna funkcja w programowaniu obiektowy, mowimy na nie KONSTRUKTORY - ich celem jest inicjalizacja obiektu! !! #TU ZDEFINIOWALISMY SOBIE KONSTRUKTORA !!!
        self.__stack_list = [] # TU MAM ENKAPSULACJE CZYLI __ #lista do przechowywania elementow, dajemy podwojny podkreslnik i to oznacza ze ta zmienna ma status ZMIENNEJ NIE PUBLICZNEJ (Prywatnej), czysto umownie, nie wolno dodac drugiego __ z tylu bo to inna konwencja
#to nam daje to ze jak to tak nazwiemy to spoza klasy nie bedziemy miec dostepu do tej wlasciwosci

    def push(self, item): # DODAJEMY METODE DO UMIESZCZANIA ELEMENTU NA STOSIE (ZACHOWANIE)
        self.__stack_list.append(item)

    def pop(self): # DODAJEMY METODE DO SCIAGANIA ELEMENTU ZE STOSU
        item = self.__stack_list[-1]
        del self.__stack_list[-1]
        return item

stack_obj = Stack()
stack_obj.push(3)
stack_obj.push(2)
stack_obj.push(1)

# stack_obj.--stack_list.append(222) #stack object, odwolam sie do stack list i zrobie append 222, wynikiem bedzie blad bo jest zabezpieczenie __ !
# musimy uzywac metody push i pop. PO TO JEST ENKAPSULACJA, uzytkownik musi uzywac tylko nasz interfejs

print(stack_obj.pop())
print(stack_obj.pop())
print(stack_obj.pop())


# stack_obj = Stack() #tu musza byc nawiasy okragle #tworzac obiekt, jest wywolywany KONSTRUKTOR ktory inicjalizuje
# stack_obj.stack_list.append(1)
# stack_obj.stack_list.append(1)
# stack_obj.stack_list.append(1) #wynikiem będzie 3, bo tworzymy stos wiec bierze wynik trzech linii i go "uklada" razem, ale piszac self.stack_list, jak damy self.__stack_list to nie bedzie dzialac
# print(len(stack_obj.stack_list)) #wez obiekt stack_obj i sprawdz ile tam jest elementow, czyli funkcja LEN, powinno dac 0

# piszac self.stack_list to nam stackuje, jak damy self.__stack_list to nie bedzie dzialac, ale mozna to obejsc metoda