
# def scope_test():
#     x = 123
#     print(x)
#
# scope_test()
# print(x)

# def scope_test():
#     print("w środku funkcji:", x)
#
#
# x = 123 #zmienna globalna
# scope_test()
# print("poza funkcją", x)

def scope_test():
    global x #od tej pory traktuj zmienna global jako x
    x = 999 #zmienna lokalna ma priorytet, nadpisuje zmienna globalna!
    print("w środku funkcji:", x)


x = 123 #zmienna globalna
scope_test()
print("poza funkcją", x)