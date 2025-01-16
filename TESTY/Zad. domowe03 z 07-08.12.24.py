# Napisz grę polegającą na zapamiętywaniu kolejnych słów. Wylosowany
# gracz podaje pierwsze słowo a kolejny powtarza słowo i dodaje swoje.
# Następny w kolejce gracz musi podać wszystkie wcześniejsze słowa w tej
# samej kolejności i także dodać swoje. Rozgrywka kończy się gdy, któryś z
# graczy popełni błąd. Na ekranie komputera przy każdej turze należy
# wymazać ekran np. przez wyświetlenie 100 pustych wierszy.

import random


# Funkcja do czyszczenia ekranu
def clear_screen():
    # Wyświetlamy 100 pustych linii
    print("\n" * 100)


# Funkcja do gry
def memory_game():
    # Lista słów
    words = ['czereśnia', 'banan', 'truskawka', 'pies', 'kot', 'pomarańcza', 'motyl', 'koń', 'słoń', 'lew']

    # Losowanie pierwszego słowa
    game_words = [random.choice(words)]
    current_player = 1

    print("Gra w pamięć. Musisz pisać słowa w tej samej kolejności!")
    print("Pierwsze słowo:", game_words[0])

    while True:
        clear_screen()  # Czyszczenie ekranu czyli wyświetlanie pustych linii
        print("Runda " + str(len(game_words)) + " - Gracz " + str(current_player))

        # Gracz musi powtórzyć słowa, po czym dodaje swoje
        player_input = input("Gracz " + str(current_player) + ", napisz słowa: ").strip().lower()

        # Sprawdzanie słowa są poprawne i w dobrej kolejności
        if player_input == ' '.join(game_words):
            print("Dobrze pamiętasz! Teraz napisz swoje słowo.")
            new_word = input("Gracz " + str(current_player) + ", napisz nowe słowo: ").strip().lower()
            game_words.append(new_word)  # nowe słowo do listy
            current_player = 2 if current_player == 1 else 1  # Zmiana gracza
        else:
            # Błąd czyli koniec gry
            print("Popełniłeś błąd, koniec gry.")
            break


# Start gry
memory_game()
