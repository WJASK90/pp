# 2. Korzystając z napisanej wcześniej klasy Stack:
# • utwórz 3 stosy (3 obiekty klasy Stack),
# • połóż na pierwszym stosie kolejno liczby od 1 do 100,
# • ściągaj kolejne elementy (liczby) z pierwszego stosu i umieszczaj na drugim,
# • ściągaj kolejne elementy z drugiego stosu i umieszczaj na trzecim,
# • ściągaj i wyświetlaj w tej samej linii elementy z trzeciego stosu.

from stack_oop import Stack #importujemy

s1 = Stack()
s2 = Stack()
s3 = Stack()

for i in range(1, 101):
    s1.push(i) #kazda liczbe kladziemy na stosie, robimy tak 100 razy

for _ in range(100):
    s2.push(s1.pop()) #poloz na stosie s2 element ktory sciagniesz ze stosu s1

for _ in range(100):
    s3.push(s2.pop())

for _ in range(100):
    print(s3.pop(), end=" ")