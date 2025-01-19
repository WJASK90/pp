class MyClass:
    def __init__(self, x=1):
        self.__x = x #zmienna INSTANCJI a nie KLASY bo sie definiuje w konstruktorze i jej porzedzona specjalna zmienna self

    def sety(self, y):
        self.__y = y

obj = MyClass(99) #dziala jak w funkcji, tak jakbysmy wywolali KONSTRUKTOR omijac parametr self
obj.sety(77)

print(obj.x, obj.y) #jak instancja ma __ to aby sie do niej odwolac

obj2 = MyClass(0)
obj2.sety(0)

print(obj2.x, obj2.y)

obj3 = MyClass()
obj3.z = 1

print(obj3.x, obj3.z)

print(obj.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)

print(obj3.__z) #to zadziala mimo zabezpieczenia w formie __