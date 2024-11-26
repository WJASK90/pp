# Napisz program sumujący pobrane liczby od użytkownika wg wytycznych:
# • program powinien pobierać od użytkownika liczby całkowite,
# • niepodanie liczby powinno zakończyć wprowadzanie danych,
# • program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych.


#czyli musze zrobic tak: musze pytac uzytkownika o liczby calkowite i jak juz bedzie chcial przestac to niech wpisze STOP
#albo nic, po czym program musi podac sume liczb parzystych podanych przez uzytkownika jak i nieparzystych,

#musze przemycic stringi do tego wszystkiego, polaczyc to z petla ktora, kiedy zostanie zatrzymana, policzy ile wyszlo liczby parzystych a ile nieparzystych

#wiec nalezy zrobic petle i warunki if (liczba parzysta to) elif (liczba nieparzysta) else (nie liczba to stop) + zrobic integer (INT)
# to wtedy bede mial tylko liczby calkowite + czyli pracuje glownie na petli typu ELSE (patrz plik TESTY --> Testy PETLE 1)


# Pętla do pobierania liczb
# for i in range(liczba):
#     liczba = int(input(f"Podaj liczbę: "))
#     if (i == i(int)):
#         continue
#     print(f"Podana liczba {i+1} to: {liczba}")
#         else
#     print("To nie jest liczba całkowita!")

#  POMOC CHATGPT liczba = 4
#
# for i in range(liczba):
#     user_input = input(f"Podaj liczbę całkowitą: ")
#     liczba = int(user_input)
#     print(f"Podana liczba {i+1} to: {liczba}")

# liczba = 4
#
# for i in range(liczba):
#     liczba = int(input(f"Podaj liczbę: "))
#     if (i == int(liczba)):
#         print("To jest liczba całkowita")
#     else:
#         print("To nie jest liczba całkowita")

#zmienna do sumowania liczb
s = 0

# Pętla do wprowadzania liczb
while True:
    # Pobranie liczby od użytkownika
    liczba = input("Podaj liczbę całkowitą (lub naciśnij Enter, aby zakończyć): ")
    # Jeśli użytkownik nie podał liczby, zakończ pętlę
    if int(liczba) == "":
        print("Koniec pobierania liczb")
        break
    try:
        # Próba konwersji wprowadzonego ciągu na liczbę całkowitą
        liczba = int(liczba)
        s += liczba
        print("Suma podanych liczb to: " + str(s))
    except ValueError:
        # Jeśli nie udało się przekonwertować, informujemy użytkownika
        print("To nie jest liczba całkowita, spróbuj ponownie.")


# liczba = int(input("Podaj liczbę całkowitą (lub naciśnij Enter, aby zakończyć): "))
# print(str(liczba))
# print(int(liczba) + 10)



# if s % 2 == 0:
#    print("To jest liczba parzysta")
# else:
#     print("To jest liczba nieparzysta")







