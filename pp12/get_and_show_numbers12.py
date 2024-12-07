# pobranie 3 liczb od użytkownika i wyświetlenie ich na ekranie

# print("Podaj liczbę: ")
# a = int(input())
# print("Podaj liczbę: ")
# b = int(input())
# print("Podaj liczbę: ")
# c = int(input())
#
# print("Pobrano liczby:", a, b, c)

#pracodawca chce aby komunikat byl Prosze podaj liczbe --> zmienimy wszystko dzieki funkcji! zdefiniujmy jak jako show_message()


# def show_message():
#     print("Prosze podaj liczbę:")
#
# show_message()
# a = int(input())
# show_message()
# b = int(input())
# show_message()
# c = int(input())
#
# print("Pobrano liczby:", a, b, c)

#uwaga, tak jak robilisym w asterisks12, bierzemy stamtad przyklad --> dajemy w nawiasie number_no
def show_message(number_no):
    print("Prosze podaj {} liczbę:".format(number_no))

show_message(1)
a = int(input())
show_message(2)
b = int(input())
show_message(3)
c = int(input())

print("Pobrano liczby:", a, b, c)