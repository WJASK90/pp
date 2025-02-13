# Napisz program, zliczający wystąpienia danego słowa we wskazanym tekście, w tym celu:
# •analizowany tekst wczytaj z pliku tekstowego np. znachor.txt,
# •pobierz od użytkownika szukane słowo,
# •wyświetl liczbę wystąpień zliczanego słowa.

#UWAGA - miałem problem ze znalezieniem Znachora w formacie txt więc użyłem opowiadania "Czarny Kot" autorstwa Edgara Allana Poe'a

#użycie file_path znalazłem w internecie
file_path = r"\\DESKTOP-4QM08OI\\Users\\Wojtek-PC\\Desktop\\Czarny Kot Edgar Allan Poe\\Czarny Kot opowiadanie E A Poe.txt"

try:
    with open(file_path) as file: #open() podpatrzone w internecie
        text = file.read().lower()
        words = text.split() #dzielimy tekst na pojedyńcze słowa zapisane w liście

        user_word = input("Wpisz słowo, które chcesz znaleźć w pliku: ").lower()
        occurrences = words.count(user_word)

        print(f"To słowo występuje w tekście {occurrences} razy!")
except FileNotFoundError:
    print("Błąd: Plik nie został znaleziony.")