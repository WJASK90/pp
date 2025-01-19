# 3. Zaprojektuj klasę produktu sklepu internetowego wg wytycznych:
# • stwórz klasę o nazwie Product,
# • dodaj (prywatne) właściwości jak nazwa, kategoria, cena, rabat w procentach,
# • dodaj metodę obliczającą cenę uwzględniającą rabat,
# • dodaj metodę sprawdzającą przynależność produktu do danej kategorii,
# • dodaj metodę reprezentującą obiekt klasy jako ciąg znaków.
# Dodatkowo stwórz grupę produktów z kilku kategorii, ustaw rabat dla produktów z jednej
# kategorii i wyświetl listę produktów.


class Product:

    def __init__(self, name, category, price):
        self.__name = name
        self.__category = category
        self.__price = price
        self.__discount_in_percent = 0

    def set_discount_in_percent(self, percent):
        self.__discount_in_percent = percent

    def get_current_price(self):
        result = self.__price * (1 - self.__discount_in_percent / 100) #pomniejszamy wartosc produktu
        return round(result, 2)

    def is_category(self, category):
        return self.__category == category

    def __str__(self):
        return f'{self.__name} ({self.__category}) - {self.get_current_price()} zł'

def show_products(products):
        for product in products:
            print(product)

def special_offer(products, category, discount_in_percent): #lista produktow, kategoria, ile obnizamy
        for product in products:
            if product.is_category(category):
                product.set_discount_in_percent(discount_in_percent)

products = []
products.append(Product(name="mleko", category="spożywcze", price=3.99))
products.append(Product(name="masło", category="spożywcze", price=9.78))
products.append(Product(name="jogurt", category="spożywcze", price=2.15))
products.append(Product(name="płyn do naczyń", category="chemia", price=4.50))

show_products(products)
special_offer(products, category="chemia", discount_in_percent=10)
show_products(products)




