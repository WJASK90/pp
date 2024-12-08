from random import choice, sample

lst = [i for i in range (1,11)]

print(choice(lst)) #wybiera jedną liczbę ze zbioru
print(sample(lst,5)) #wybiera 5 liczb ze zbioru - bez powtorzen
print(sample(lst,10)) #wybiera 10 liczb ze zbioru - bez powtorzen