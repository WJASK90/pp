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

    def raise_salary(self, percent=10): #lab 22 1
        self.__salary *= (1 + percent / 100)


    # def raise_salary(self, percent=10): #lab 22 1
    #     return self.__salary * 0.1 + self.__salary

#KOD ZMODYFIKOWANY EMPLOYEES

from employee import Employee #nacisnij kontrol i najedz na Employee to bedziesz mogl tam przeskoczyc

employees = []
employees.append(Employee(firstname="Jan", lastname="Kowalski", age=25, salary=4500))
employees.append(Employee(firstname="Edmund", lastname="Kaczmarczyk", age=45, salary=7000))
employees.append(Employee(firstname="Ewa", lastname="Nowak", age=60, salary=15200))

print("Lista płac")
print("-" * 30)
for employee in employees:
    print(employee.get_fullname(),
          "wiek:", employee.get_age(),
          "lat, pensja:", employee.get_salary(),
          "zł", "podwyżka 10%:", employee.raise_salary())

#WYNIK:
# Jan Kowalski wiek: 25 lat, pensja: 4500 zł podwyżka 10%: 4950.0
# Edmund Kaczmarczyk wiek: 45 lat, pensja: 7000 zł podwyżka 10%: 7700.0
# Ewa Nowak wiek: 60 lat, pensja: 15200 zł podwyżka 10%: 16720.0
