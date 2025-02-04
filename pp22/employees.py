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


