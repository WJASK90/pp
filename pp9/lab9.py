# Wyświetl tylko liczby podzielne przez 3, 5 lub 7, ze zbioru liczb z zakresu
# określonego przez użytkownika.

value_1 = int(input("Podaj początek zakresu liczb, sprawdzimy czy są podzielne przez 3, 5 lub 7: "))
value_2 = int(input("Podaj koniec zakresu liczb, sprawdzimy czy są podzielne przez 3, 5 lub 7: "))
for i in range(value_1,value_2):
    if i % 3 == 0:
        print(i)
    elif i % 5 == 0:
        print(i)
    elif i % 7 == 0:
        print(i)
    else:
        print(end="")



print("*" * 25)
# Udowodnij, że w zbiorze liczb z zakresu 1-100, jest 11 liczb, które są
# parzyste i jednocześnie większe od 90, a gdy są nieparzyste, to
# przynajmniej dzielą się przez 9.

for i in range(1,100):
    if i % 2 == 0:
        print("Parzysta")
    elif i % 2 == 0 and  i >= 90:
        print("Parzysta i większa od 90")





print("*" * 25)
# Napisz program wyznaczający wartość n-tego bitu dla dowolnej liczby
# całkowitej. Bity liczymy od 0, od najmniej znaczącego bitu.






print("*" * 25)

