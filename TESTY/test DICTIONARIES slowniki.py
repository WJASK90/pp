#slowniki to kolekcje w parach key:value / klucz:wartosc

product = {
    "name": "pen",
    "color": "red",
    "price": 79
}

print(product)

#z funkcjami values() i keys() pobieramy wartosci i klucze ze Slownika

contact = {
    "name" : "John",
    "company" : "Google",
}

info_keys = contact.keys()
info_values = contact.values()

print(info_keys, info_values)