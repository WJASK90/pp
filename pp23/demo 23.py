class MyClass:
    def my_method(self, x):
        print("To jest moja metoda!", x)

obj = MyClass()
obj.my_method(1)
obj.my_method("A")

obj = MyClass()
obj.my_method(1)
obj.my_method("A")

class MyClass:

    def __init__(self, y=23):
        self.x = 1
    def __init__(self, y):
        self.x = 1
        self.y = y


class MyClass:
    y = 99
    def my_method(self, x):
        print("To jest moja metoda!", x, self.y)

obj.my_method(1)




