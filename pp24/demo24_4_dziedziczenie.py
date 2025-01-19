class Animal:
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f"Jestem zwierzęciem, mam na imię {self.__name}"

    def get_name(self):
        return self.__name

class Dog(Animal): #klasa DOG rozszerza ANIMAL
    def __init__(self, name): #KONSTRUKTOR
        super().__init__(name) #KONSTRUKTOR wywoluje z klasy ANIMAL / super() wywoluje z NADKLASY Animal ale bez self w ()

    def __str(self):
    return f"Jestem psem, mam na imię {self.get_name()}"

dog = Dog("Pluto") #mam obiekt klasy DOG
print(dog)