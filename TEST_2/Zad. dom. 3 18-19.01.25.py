# Napisz kolejną wersję programu do gry w lotto uwzględniając:
# •zasady programowania zorientowanego obiektowo,
# •możliwość podawania typowanych przez użytkownika liczb jako lista,
# •możliwość grania systemem (6-12 liczb).


from random import sample
#tworzenie klasy
class LottoGame:
    def __init__(self):
        self.user_numbers = []
        self.lucky_numbers = []
#losowanie
    def draw_numbers(self):
        if not self.lucky_numbers:
            self.lucky_numbers = sorted(sample(range(1, 50), 6))
        return self.lucky_numbers
#wprowadzanie danych do gry
    def get_game_system(self):
        while True:
            try:
                number = int(input("Podaj liczby z przediału 6-12: "))
                if number < 6 or number > 12:
                    print("Uwaga! Musisz podać liczbę z przedziału 6-12!")
                    continue
                return number
            except ValueError:
                print("Niestety, to nie jest liczba! :(")
                continue
#pobieramy liczby (z zabezpieczeniami)
    def get_user_numbers(self):
        n = self.get_game_system()

        while True:
            user_input = input(f"Podaj {n} liczb oddzielając je przecinkami: ")
            try:
                numbers = [int(_.strip()) for _ in user_input.split(',')]
            except ValueError:
                print("Uwaga! Upewnij się, że wpisujesz liczby oddzielone przecinkami.")
                continue

            if len(numbers) != n:
                print(f"Uwaga! Musisz podać dokładnie {n} liczb.")
                continue
            if len(set(numbers)) != len(numbers):
                print("Uwaga! Nie możesz podawać powtórzonych liczby!")
                continue
            if any(num < 1 or num > 49 for num in numbers):
                print("Uwaga! Wszystkie liczby muszą być z przedziału 1-49!")
                continue

            self.user_numbers = sorted(numbers)
            return self.user_numbers
#sprawdzamy trafienia
    def check_user_numbers(self):
        hits = [num for num in self.user_numbers if num in self.lucky_numbers]
        return len(hits), hits
#gra w lotto
    def play(self):
        print("Witaj w grze Lotto! Oby fart ci sprzyjał!")
        self.get_user_numbers()
        self.draw_numbers()
        hit_count, hit_numbers = self.check_user_numbers()
        print("\nTwoje liczby:", self.user_numbers)
        print("Liczby losowania:", self.lucky_numbers)
        print("Liczba trafień:", hit_count)
        if hit_count > 0:
            print("Trafione liczby: ", hit_numbers)


game = LottoGame()
game.play()