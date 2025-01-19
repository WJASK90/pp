class MyClass:
    counter = 0 #zmienna klasy

    def __init__(self, x=1):
        self.__x = x # zmienna instancji
        MyClass.counter += 1 #tu MUSI byc nazwa klasy, zmienna klasowa w konstruktorze musi byc tak ustawiona

obj1 = MyClass(0)
obj2 = MyClass(2)
obj3 = MyClass(3)

print(MyClass.counter) #wywolujac wlasciwosci MYCLASS.COUNTER to otrzymamy wartosc 3
print(obj1.counter) #mozna sie odwolac tez w taki sposob