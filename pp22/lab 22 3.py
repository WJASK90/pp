# 3. Napisz klasę reprezentującą obiekty typu książka, w tym celu:
# • stwórz klasę Book z odpowiednimi właściwościami i metodami,
# • stwórz kilka przykładowych egzemplarzy tej klasy,
# • zademonstruj działanie wybranych metod na przykładowych egzemplarzach.

class Book:
    def __init__(self, title, author, publisher, year):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__year = year

    def show_short_info(self):
        print(f"tytuł {self.__title} autor: {self.__author}") #piszemy z f-string czyli f""

    def show_full_info(self):
        print(f"tytuł {self.__title} autor: {self.__author} wydawca: {self.__publisher} rok wydania: {self.__year}")

books = []
books.append(Book("Dzieci z Bullerbyn", author="Astrid Lindgren", publisher="Nasza Księgarnia", year=2014))
books.append(Book("Moby Dick", author="Herman Marville", publisher="Amercon", year=2009))
books.append(Book("Python. Wprowadzenie", author="Mark Lutz", publisher="Helion", year=2022))
#wymusza wszystkie pola ALE jak dasz wartosc domyslne (jak w funkcjach) to mozesz to obejsc :)
for book in books:
    book.show_full_info()

