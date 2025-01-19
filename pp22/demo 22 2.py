class MyClass:
    counter = 0 #zmienna klasy, tez moze byc nie publiczna

    def __init__(self, x=1):
        self.__x = x # zmienna instancji
        MyClass.counter += 1 #tu MUSI byc nazwa klasy, zmienna klasowa w konstruktorze musi byc tak ustawiona

obj1 = MyClass(0)
obj2 = MyClass(2)
obj3 = MyClass(3)

print(MyClass.counter) #wywolujac wlasciwosci MYCLASS.COUNTER to otrzymamy wartosc 3
print(obj1.counter) #mozna sie odwolac tez w taki sposob

print(obj1.__dict__, obj1.counter) # wynik {'_MyClass__x': 0} 3 ten numer na koncu, czyli 3, dlatego bo mamy 3 instancje
print(obj2.__dict__, obj2.counter) # {'_MyClass__x': 2} 3
print(obj3.__dict__, obj3.counter) # {'_MyClass__x': 3} 3