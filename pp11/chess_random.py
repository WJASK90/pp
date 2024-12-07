import random

BLANK_SQUARE = "--"
pieces = ["WP", "BP", "BP", "BT", "WQ"] #wp white pawn, bp black pawn, bt black tower, wq white queen

chessboard = [[BLANK_SQUARE for _ in range(8)] for _ in range(8)] #jak nie uzywasz i to uzyj _

counter = 0 #dajemy counter bo potrzebujemy petle WHILE, WHILE poniewaz mamy te 5 elementow,
#petla sie obraca dopoki counter bedzie mniejsze od 5 - czyli trzeba dokonac 5 rozstawien

counter = 0
while counter < 5:
    row = random.randint(0, 7) #linie, mamy 8 pol, indeks zaczyna sie od 0, wiec od 0 do 7
    col = random.randint(0, 7) #kolumny
    if chessboard[row][col] == BLANK_SQUARE: #jezeli jest puste pole, to wstawiaj
        chessboard[row][col] = pieces[counter] #counter sie podnosi dopoki nie bedzie trafiac na puste pole
        counter += 1

#wyswietlamy liste listy, czyli petla w petli
for row in range(len(chessboard)): #sprawdzamy ile ma elementow szachownica/lista chessboard
    if row == 0:
        print( " ","A","B","C","D","E","F","G","H", sep="  ") #aby uzyskac pozycje graficzna pionkow na szachownicy
        print(row + 1, end=" ") #aby uzyskac pozycje graficzna pionkow na szachownicy
    for col in range(len(chessboard[row])): #sprawdzamy ile elementow ma konkretny wiersz
        print(chessboard[row][col], end=" ") #end=" " bo wtedy wyswietlamy po kolei pola
    print() #konczymy

