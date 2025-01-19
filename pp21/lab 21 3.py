# 3. Rozbuduj klasę Stack o następujące metody:
# • empty() - powinna zwracać True jeżeli stos jest pusty, w przeciwnym wypadku zwracać False,
# • size() - powinna zwracać rozmiar stosu,
# • top() - powinna zwracać "górny" element stosu, czyli ten, który zostanie "ściągnięty"
# metodą pop().

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

    def empty(self):
        return len(self.__stack_list) == 0 #lab 21 3, jezeli ilosc elementow na stosie to 0 to znaczy ze stos jest pusty/empty, inaczej zwraca FALSE

    def size(self):
        return len(self.__stack_list) #lab 21 3

    def top(self):
        return self.__stack_list[-1] #lab 21 3 zwracamy stack list -1

stack = Stack()
print("Jest pusty?", stack.empty())

stack.push("Ala")
stack.push("Tomek")
stack.push("Agata")

print("Jest pusty?", stack.empty())
print("Ile elementów?", stack.size())
print("Na samej górze:", stack.top())

print(stack.pop())
print(stack.pop())
print(stack.pop())