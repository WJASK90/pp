# Napisz program, zliczający wystąpienia danego słowa we wskazanym tekście, w tym celu:
# •analizowany tekst wczytaj z pliku tekstowego np. znachor.txt,
# •pobierz od użytkownika szukane słowo,
# •wyświetl liczbę wystąpień zliczanego słowa.

# #tworzymy klasę
# class WordCounter:
#     def __init__(self, file_path):
#         self.file_path = file_path
#
#     def count_word_occurrences(self, word):
#         try:
#             with open(self.file_path, 'r') as file:  # Otwieranie pliku
#                 text = file.read().lower()  # Zamiana na małe litery
#                 words = text.split()  # Podział na listę słów
#                 return words.count(word.lower())  # Licznik słowa
#         except FileNotFoundError:
#             print("Błąd: Plik nie został znaleziony.")
#             return None  #Możliwość nowej próby bez zamykania programu
#
# # Ścieżka do pliku
# file_path = r"\\DESKTOP-4QM08OI\\Users\\Wojtek-PC\\Desktop\\Czarny Kot Edgar Allan Poe\\Czarny Kot opowiadanie E A Poe.txt"  # Tutaj wpisz swoją ścieżkę do pliku
#
# # Tworzenie obiektu
# counter = WordCounter(file_path)
#
# # Pobieranie słowa od użytkownika
# user_word = input("Wpisz słowo, które chcesz znaleźć w pliku: ")
#
# # Liczenie wystąpień
# occurrences = counter.count_word_occurrences(user_word)
#
# # Wyświetlanie wyniku
# if occurrences is not None:
#     print(f"To słowo występuje w tekście {occurrences} razy!")


#ŁATWA WERSJA

file_path = r"\\DESKTOP-4QM08OI\\Users\\Wojtek-PC\\Desktop\\Czarny Kot Edgar Allan Poe\\Czarny Kot opowiadanie E A Poe.txt"

try:
    with open(file_path, 'r') as file:
        text = file.read().lower()
        words = text.split()

        user_word = input("Wpisz słowo, które chcesz znaleźć w pliku: ").lower()
        occurrences = words.count(user_word)

        print(f"To słowo występuje w tekście {occurrences} razy!")
except FileNotFoundError:
    print("Błąd: Plik nie został znaleziony.")






# -----------------------------------------
# class WordCounter:
#     def __init__(self, file_path):
#         self.file_path = file_path
#         self.text = self.read_file()
#
#     def read_file(self):
#         #pobieram słowo z tekstu
#         try:
#             with open(self.file_path, 'r', encoding='utf-8') as file:
#                 text = file.read()
#             return text
#         except FileNotFoundError: #w wypadku braku wpisanego słowa, zabezpieczamy
#             print(f"Błąd: Plik {self.file_path} nie został znaleziony.")
#             sys.exit()
#
#     def count_word_occurrences(self, word):
#         #liczym, ile razy dane słowo występuje w tekście
#         words = self.text.lower().split()  # dzieli tekst na słowa i ignoruje wielkość liter
#         return words.count(word.lower())  # zlicza wystąpienia słowa
#
# # Wczytanie pliku
# file_path = r"\\DESKTOP-4QM08OI\\Users\\Wojtek-PC\\Desktop\\Czarny Kot Edgar Allan Poe\\Czarny Kot opowiadanie E A Poe.txt"  # Ścieżka do pliku
# counter = WordCounter(file_path)
#
# # Pobieranie słowa od użytkownika
# user_word = input("Wpisz słowo, które chcesz znaleźć w pliku: ")
#
# # Liczenie wystąpień
# occurrences = counter.count_word_occurrences(user_word)
#
# # Wyświetlanie wyniku
# print(f"To słowo występuje w tekście {occurrences} razy!")

#-------------------------------------------------------------------------------
# file_path = C:\Users\Wojtek-PC\Desktop\Czarny Kot Edgar Allan Poe
#
# print(input("Wpisz słowo - sprawdzimy, ile razy występuje w pliku tekstowym: "))
#
# def count_words(word):
#     words_list = []
#     for i in word:
#         words_list.append(i)



# 2. Zaimplementuj funkcję, która przyjmuje jako argument ciąg znaków i zwraca
# liczbę wystąpień każdego znaku w ciągu.
# Na przykład dla ciągu "abracadabra" funkcja powinna zwrócić słownik { 'a': 5, 'b':
# 2, 'r': 2, 'c': 1, 'd': 1 }.

# txt = """W Pacanowie kozy kują
#     więc Koziołek, mądra głowa,
#     błąka się po całym świecie,
#     aby dojść do Pacanowa."""
#
# def count_letters(string):
#     stats = {}
#     for letter in string:
#         stats[letter] = stats.get(letter, 0) + 1
#     return stats
#
# print(count_letters('abc'))
# print(count_letters('Ala ma kota.'))
# print(count_letters(txt))