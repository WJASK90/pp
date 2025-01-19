class Animal:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f"Jestem zwierzęciem, mam na imię {self.__name}"

class Dog(Animal): #klasa DOG rozszerza ANIMAL
    def __init__(self, name): #KONSTRUKTOR
        Animal.__init__(self, name) #KONSTRUKTOR wywoluje z ANIMAL

dog = Dog("Pluto") #mam obiekt klasy DOG
print(dog)