stack = [] #czyli "stos"

def push(val):
    stack.append(val) #bierzemy liste i dodajemy element

def pop(): #funkcja pop sciaga liczbe ze stosu i ja zwraca
    val = stack[-1] #wez ostatni element na liscie stack
    del stack[-1]
    return val
    # return stack.pop()

push(3)
push(2)
push(1)

#mozna w stackach uzywac wyrazow
print(pop("Ala"))
print(pop("ma"))
print(pop("kota"))


# STOS WYGLADA TAK:
# zaczynam sciaganie od gory
# 1 -->
# 2 --> 2 -->
# 3 --> 3 --> 3