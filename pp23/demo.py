class A:
    pass

class B:
    pass

class C(A, B):
    pass

print(C.__bases__) #wynik (<class '__main__.A'>, <class '__main__.B'>) lista nadklas