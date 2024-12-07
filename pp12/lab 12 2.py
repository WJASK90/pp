# 2. Napisz skrypt obliczający obwód, pole powierzchni i długość przekątnej dla
# prostokątów o następujących długościach boków:
# • 4 i 5,
# • 2678 i 5678,
# • 344555 i 788998.

#stworzymy trzy funkcje - jedna do obwodu, inna do pola i inna do dlugosci przekatnej

def perimeter(a, b): #obwod
    return 2 * a + 2 * b

def surface_area(a, b): #pole powierzchni
    return a * b

def diagonal_lenght(a, b): #dlugosc przekatnej
    return (a ** 2 + b ** 2) ** 0.5 #Pitagoras

def show_result(a, b):
    print("Prostokąt o bokach {} i {}:".format(a, b))
    print("Obwód:", perimeter(a, b))
    print("Pole powierzchni: ", surface_area(a, b))
    print("Długość przekątnej: ", diagonal_lenght(a, b))
    print()

show_result(4, 5)
show_result(2678, 5678)
show_result(344555, 788998)