# 3. Zabezpiecz program zliczający punkty w grach (moduł 14, lab 3) przed
# wprowadzaniem błędnych danych przez użytkownika.

def fetch_and_validate_int(standard_msg, error_msg="To nie jest liczba całkowita."):
    while True:
        try:
            return int(input(standard_msg))
        except:
            print(error_msg)


def define_player(player_no):
    player_points = []
    player_name = input("Podaj imię {} gracza: ".format(player_no))
    return {player_name: player_points}

def define_players():
    players = {}
    players_total = fetch_and_validate_int("Podaj liczbę graczy od 1 do 8: ") #LAB15
    for i in range(players_total):
        #indeks powiekszony o 1 bo zaczynam od 0
        players.update(define_player(i + 1))
    return players

def define_win_points():
    return fetch_and_validate_int("Zdefiniuj liczbę punktów wygranej: ") #POD LAB15 NALEZY ZABEZPIECZYC

def is_winner(players, win_points): #wygral czy nie? potrzebujemy kluczy players i win_points
    for player in players.keys():
        if sum(players[player]) >= win_points:
            return True
    return False

def count_points(players, win_points): #zliczamy punkty graczom
    counter = 1
    while True: #petla konczy sie kiedy ktos wygra, counter zlicza punkty
        print("\nTura", counter) # \n zeby to sie ladnie wyswietlalo
        for player in players.keys(): #iterujemy po tych kluczach
            player_points = fetch_and_validate_int("Podaj punkty dla gracza: - {} ".format(player)) #podaj punkty dla gracza o nazwie player #LAB15
            players[player].append(player_points)
            if is_winner(players, win_points):
                return player
        counter += 1
    return "winner"

def show_results(players, winner):
    print("\nWygrał gracz o imieniu {}, brawo!".format(winner))
    print()
    print("Szczegółowa tabela wyników")
    for player, points in players.items():
        print(player, "->", points)

players = define_players()
win_points = define_win_points()
winner = count_points(players, win_points)
show_results(players, winner)
