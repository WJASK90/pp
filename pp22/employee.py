class Employee:
    def __init__(self, firstname, lastname, age, salary):
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def get_fullname(self): #metoda zwraca imie i nazwisko
        return '{} {}'.format(self.__firstname, self.__lastname)

    def get_age(self):
        return self.__age

    def raise_salary(self): #lab 22 1
        return self.__salary * 0.1 + self.__salary
