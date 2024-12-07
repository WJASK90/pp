# 3. Napisz skrypt symulujący rozgrywkę gry w szachy, w tym celu:
# • stwórz wirtualną szachownicę,
# • na wirtualnej szachownicy rozmieść losowo 2. dowolne figury szachowe i 3. piony,
# • zaprezentuj użytkownikowi stan wirtualnej szachownicy.

row = [1, 2]
matrix = [row[:], row[:]] #dawaj wycinki !!!
print(matrix)

matrix[0][0] = 99
print(matrix)

print("*" * 25)
#wygeneruj plansze do szachownicy, czyli plansze 8 * 8 (64 pola)

# tworzymy planszę do gry w szachy, czyli szachownice (OMG)

# chess_row = ["--", "--", "--", "--", "--", "--", "--", "--"]
# chess_row = ["--" for _ in range(8)]
# chessboard = [chess_row[:] for _ in range(8)]

chessboard = [["--" for _ in range(8)] for _ in range (8)]

WHITE_PAWN = "BP"
BLACK_PAWN = "CP"

chessboard[3][4] = WHITE_PAWN
chessboard[2][7] = BLACK_PAWN

for chess_row in chessboard:
    for chess_square in chess_row:
        print(chess_square, end=" ")
    print()