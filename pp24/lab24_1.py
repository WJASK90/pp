# 1. Zamodeluj strukturę klas figur geometrycznych, w tym celu:
# • stwórz ogólną klasę Shape,
# • stwórz podklasy: Rectangle, Triangle, Circle,
# • utwórz kilka figur i wyświetl ich typy.

class Shape:
    pass

class Rectangle(Shape):
    pass

class Circle(Shape):
    pass

class Triangle(Shape):
    pass

figures = [Rectangle(), Circle(), Triangle()]

for figure in figures:
    print(type(figure))


