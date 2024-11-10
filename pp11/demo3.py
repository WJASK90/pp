row = [1, 2]
matrix = [row[:], row[:]] #dawaj wycinki !!!
print(matrix)

matrix[0][0] = 99
print(matrix)

#wygeneruj plansze do szachownicy, czyli plansze 8 * 8 (64 pola)