# 1. Rozbuduj klasę Employee o mechanizm zwiększania wynagrodzeń:
# • dodaj metodę rise_salary(),
# • metoda powinna zwiększać zarobki o podaną wartość procentową,
# • domyślnie metoda powinną zwiększać zarobki o 10% (* 0.1)

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

    def rise_salary(self): #lab 22 1
        return self.__salary * 0.1 + self.__salary
