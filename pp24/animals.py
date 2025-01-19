from pp24.demo24 import Cat


class Animal:
    def introduce(self):
        print(f"Jestem typem {self.type} mam na imię {self.name} i jest nas wszystkich {self.counter}!")


class Dog(Animal):
    type = "pies"
    counter = 0

    def __init__(self, name):
        self.name = name
        Dog.counter += 1


class Cat(Animal):
    type = "kot"
    counter = 0

    def __init__(self, name):
        self.name = name
        Cat.counter += 1

animals = [
    Dog("Pluto"),
    Cat("Filemon"),
    Dog("Azor"),
    Dog("As"),
    Dog("As"),
    Cat("Sylwester")
    ]

for animal in animals:
    animal.introduce()