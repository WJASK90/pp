class MyClass:
    def __init__(self):
        self.x = 1

obj1 = MyClass()
obj2 = MyClass()
obj3 = obj1

print(obj1 is obj2)
print(obj2 is obj3)
print(obj1 is obj3) #TRUE poniewaz do obj3 podstawilismy referencje z obj1

obj3.x = 99

print(obj1.x) #99
print(obj1.x, obj2.x, obj3.x) #99 1 99