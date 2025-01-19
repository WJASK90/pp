class Car:
    def drive(self):
        print("Jedzie...")

class Boat:
    def sail(self):
        print("Płynie...")

class Amphibian(Car, Boat):
    pass

amphibian = Amphibian()
amphibian.drive()
amphibian.sail()
