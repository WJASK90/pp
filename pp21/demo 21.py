class MyClass: #nie ma wlasciwosci ani zachowan, przy ZDEFINIOWANIU nie potrzeba nawiasu w porownaniu do FUNKCJI
    pass

my_obj = MyClass() #nazywamy obiekt, troche dopodbne do wylowywania funkcji, podejscie do programowania zorientowanego obiektowo
my_obj.x = 5

print(my_obj.x) #wez obiekt i powiedz ile wynosi x dla tego obiektu, wynik --> 5
print(type(my_obj)) #wynik --> <class '__main__.MyClass'> czyli twór klasy MyClass, ale po co to? Stworzylismy Klase, a Klasa jest po to aby moc stworzyc
# dowolna ilosc takich obiektow

obj2 = MyClass()
obj2.x = 99 # B - TERAZ dodane i bedzie wynik czyli 99
print(obj2.x) # A - wynik AttributeError: 'MyClass' object has no attribute 'x', obj2 nie ma atrybutu

obj99 = MyClass()





