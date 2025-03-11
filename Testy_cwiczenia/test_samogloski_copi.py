# Napisz funkcję o nazwie policz_samogloski, która przyjmuje jako argument łańcuch tekstu (string)
# i zwraca liczbę samogłosek w tym łańcuchu. Samogłoski to: a, e, i, o, u
# (możesz też dodać polskie znaki, takie jak ą, ę, jeśli chcesz!).
#
# Oto podpowiedź, od której możesz zacząć:
# def policz_samogloski(tekst):
#     samogloski = "aeiou"
#     licznik = 0
#     # Twoja logika tutaj
#     return licznik
#
# # Wywołaj funkcję na przykładzie:
# print(policz_samogloski("Witaj w świecie Pythona!"))
# Twoim zadaniem jest uzupełnienie logiki tak, aby funkcja poprawnie liczyła samogłoski.

# samogloski = ["a", "e", "i", "o", "u"]
# ile_samoglosek = []


def policz_samogloski(tekst):
    samogloski = "aeiou"
    licznik = 0
    for i in tekst:
        if i in samogloski:
            licznik = licznik + 1
    return licznik


print(policz_samogloski("Halo"))
print(policz_samogloski("Dobrze"))
print(policz_samogloski("Witaj w świecie Pythona!"))
print(policz_samogloski("DDD"))

# if samogloski in tekst:
#     ile_samoglosek.append(tekst)
#     print(ile_samoglosek)