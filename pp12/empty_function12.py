#pusta funkcja ktora nic nie robi
def empty_function():
    #pass
    #print("nic")
    2 + 2 #zniknie  bo nie jest przepisane do zadnej zmiennej ani do niczego

print(empty_function())

if empty_function() is None: #is None, to jest to samo co None. is None == None, is not None, != None
    print("Funkcja nic nie zwróciła!")