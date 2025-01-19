class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

# print(issubclass(Dog, Animal)) #czy DOG jest podklasa ANIMAL? TRUE
# print(issubclass(Animal, Dog)) #czy ANIMAL jest podklasa DOG? FALSE
# print(issubclass(Cat, Dog)) #czy CAT jest podklasa DOG? FALSE
# print(issubclass(Dog, Dog)) #czy DOG jest podklasa DOG? TRUE - dziwne ale prawdziwe :O

dog = Dog()
cat = Cat()

print(isinstance(dog, Dog)) #TRUE
print(isinstance(cat, Dog)) #FALSE
print(isinstance(cat, Animal)) #TRUE