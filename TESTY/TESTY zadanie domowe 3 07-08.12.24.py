# Napisz grę polegającą na zapamiętywaniu kolejnych słów. Wylosowany
# gracz podaje pierwsze słowo a kolejny powtarza słowo i dodaje swoje.
# Następny w kolejce gracz musi podać wszystkie wcześniejsze słowa w tej
# samej kolejności i także dodać swoje. Rozgrywka kończy się gdy, któryś z
# graczy popełni błąd. Na ekranie komputera przy każdej turze należy
# wymazać ekran np. przez wyświetlenie 100 pustych wierszy.

import os
import random
import time


# Funkcja do czyszczenia ekranu przez wyświetlenie pustych linii
def clear_screen():
    # Wyświetlamy 100 pustych linii, aby "wyczyścić" ekran
    print("\n" * 100)


# Funkcja do rozgrywki
def memory_game():
    # Lista słów do wyboru
    words = ['apple', 'banana', 'cherry', 'dog', 'elephant', 'flower', 'grape', 'house', 'ice', 'jungle']

    # Losowanie pierwszego słowa
    game_words = [random.choice(words)]
    current_player = 1

    print("Gra w pamięć. Powtarzaj słowa w tej samej kolejności!")
    print("Pierwsze słowo:", game_words[0])

    while True:
        clear_screen()  # Czyszczenie ekranu - wyświetlanie pustych linii
        print(f"Runda {len(game_words)} - Gracz {current_player}")

        # Gracz musi powtórzyć słowa i dodać swoje
        player_input = input(f"Gracz {current_player}, podaj słowa: ").strip().lower()

        # Sprawdzanie, czy gracz podał poprawnie wszystkie słowa
        if player_input == ' '.join(game_words):
            print("Dobrze! Teraz dodaj swoje słowo.")
            new_word = input(f"Gracz {current_player}, podaj nowe słowo: ").strip().lower()
            game_words.append(new_word)  # Dodajemy nowe słowo do listy
            current_player = 2 if current_player == 1 else 1  # Zmieniamy gracza
        else:
            # Gracz popełnił błąd, kończymy grę
            print("Błąd! Gra kończy się.")
            break

        time.sleep(1)  # Krótkie opóźnienie przed kolejną rundą


# Rozpoczęcie gry
memory_game()
