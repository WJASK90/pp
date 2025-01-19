# class MyClass:
#
#     def my_method(self, x):
#         self.other_method()
#         print("To jest moja metoda!", x, self.y)
#     def other_method(self):
#         print("To jest moja metoda!", self.y)
#
# obj = MyClass
# obj.my_method(1)

class MyClass:
    def __init__(self, name):
        print("Inicjalizuję obiekt...")
        self.__name = name

    def get_name(self):
        return self.__name

# MyClass() #tworzenie instancji klasy MyClass z automatu inicjalizuje konstruktora
obj = MyClass("Marcin")
print(obj.get_name())

class MyClass:
    def __my_private_method(self):
        print("To jest metoda niepubliczna...")

obj = MyClass()
print(MyClass.__dict__)

obj._MyClass__my_private_method()
# obj.__my_private_method()