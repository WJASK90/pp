# 2. Dokonaj modyfikacji programu ze zwierzętami (animals.py):
# • dodaj 2 kolejne dowolne zwierzęta,
# • dodaj metody symulujące wydawanie dźwięków przez zwierzęta np. wyświetlając napis "miau",
# • dodaj właściwość pozwalającą zliczać wszystkie zwierzęta,
# • uwzględnij sumę wszystkich zwierząt oraz wydawane przez zwierzę dźwięki w metodzie introduce().

from pp24.demo24 import Cat #!


class Animal:
    all_counter = 0

    def __init__(self, name):
        super().__init__()
        Animal.all_counter += 1
        self.name = name

    def introduce(self):
        print(
            f"Jestem typem {self.type}, mam na imię {self.name}, jest nas {self.__class__.counter}, a wszystkich zwierząt {self.all_counter}, {self.make_sound()} !")


class Dog(Animal):
    type = "pies"
    counter = 0

    def __init__(self, name):
        super().__init__(name)
        Dog.counter += 1

    def make_sound(self):
        return "hau hau"


class Cat(Animal):
    type = "kot"
    counter = 0

    def __init__(self, name):
        super().__init__(name)
        Cat.counter += 1

    def make_sound(self):
        return "miau miau"


class Pig(Animal):
    type = "świnka"
    counter = 0

    def __init__(self, name):
        super().__init__(name)
        Pig.counter += 1

    def make_sound(self):
        return "chrum chrum"


class Horse(Animal):
    type = "koń"
    counter = 0

    def __init__(self, name):
        super().__init__(name)
        Horse.counter += 1

    def make_sound(self):
        return "ihaaa"



animals = [
    Dog("Pluto"),
    Cat("Filemon"),
    Dog("Azor"),
    Dog("As"),
    Dog("As"),
    Cat("Sylwester"),
    Pig("Piggy"),
    Horse("Karino")
]

for animal in animals:
    animal.introduce()
