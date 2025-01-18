# tworzymy modul do symulacji gry w lotto

# def draw_numbers():
#     pass #dajemy pass po to aby sobie funkcja czekala na dokonczenie, sobie szkicujemy wszystko po czym piszemy poprawna implementacje

from random import sample #SAMPLE daje nam mozliwosc losowania kilku liczb ze zbioru NUMBERS bez powtorzen


def draw_numbers():  # losuje liczby
    numbers = [i for i in range (1, 50)] #lista od 1 do 49, jak do 50 to powinnismy miec 51 lub +1
    lucky_numbers = sample(numbers, k=6)
    lucky_numbers.sort()
    return lucky_numbers
    # return sample(range(1, 50), 6)


def get_user_numbers():  # bierze liczby od gracza
    n = 6 #stala, chodzi o losowanie 6 liczb
    counter = 1 #licznik czy mam 6 liczb, zaczynam od 1
    user_numbers = []
    while counter <= n: #sprawdzamy czy counter jest rowny lub mniejszy od liczb pobranych przez uzytkownika
        try: #zabezpieczamy sie przed bledem
            number = int(input("Podaj {} liczbę (1-49): ".format(counter))) #input konwertuje na INT bo to sa liczby calkowite
            if number in user_numbers: #jesli jest w liscie to...
                print("Powtórzona liczba!") #zmuszamy aby znowy wybral
                continue
            if number < 1 or number > 49: #czy liczba jest z poza przedzialu od 1 do 49
                print("Należy podać liczbę z przedziału 1-49!")
                continue
        except:
            print("To nie jest liczba!")
            continue
        user_numbers.append(number) #dodajemy liczbe do listy
        counter += 1
    user_numbers.sort() #domyslnie sortuje rosnaca
    return user_numbers


def check_user_numbers(user_numbers, lucky_numbers):  # sprawdza liczby
    counter = 0 #licznik na zero
    for number in user_numbers: #przechodzimy po wytypowanych liczbach w liscie
        if number in lucky_numbers: #jesli trafiony jest numer, to zwiekszamy counter
            counter += 1
    return counter


if __name__ == '__main__':
    user_numbers = get_user_numbers()
    lucky_numbers = draw_numbers()
    result = check_user_numbers(user_numbers, lucky_numbers) #wykladowca mial puste nawiasy i dzialalo, ja musialem dodac
    print(user_numbers)
    print(lucky_numbers)
    print(result)

#!!!!!!!! UZYWAMY TEGO W LOTTO_GAME.PY !!!!!!!!!!!!!!