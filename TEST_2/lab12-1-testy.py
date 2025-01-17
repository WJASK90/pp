# Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
# ilość razy, w poziomie lub w pionie.


def create_char(symbol="@", repeat=10, vertical=False):
    for i in range(repeat):
        if vertical:
            print(symbol)
        else:
            print(symbol + "", end="") #będzie pionowy!
    if not vertical:
        print()
    print()


create_char()
create_char(symbol="!", repeat=8, vertical=True)
create_char(symbol="?", repeat=5, vertical=False)
