class Left:
    x = "l"
    x_left = "ll"

    def foo(self):
        return "left"

class Right():
    x = "r"
    x_right = "rr"

    def foo(self):
        return "right"

class Subclass(Left, Right):
    pass

obj = Subclass()

print(obj.foo()) #wynik: LEFT, czemu? Bo jest PIERWSZĄ klasą która jest wspomniana
print(obj.x_left) #ll
print(obj.x_right) #rr
print(obj.x) #l