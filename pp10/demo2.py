# wyznaczanie długości listy

fruits = ['apple', 'banana', 'cherry']
print(len(fruits), fruits)

del fruits[0]

print(len(fruits), fruits)

#jak usunelismy liste i potem robimy print na nia, to da nam blad bo nie zrobi print nie istniejacego juz elementu

fruits = ['apple', 'banana', 'cherry']
print(len(fruits)) # len() to funkcja
fruits.append("plum") # append() to metoda, dodaje na koncu
fruits.insert(2, "orange") # insert() to metoda,dodaje gdzie chcemy

print(fruits)

