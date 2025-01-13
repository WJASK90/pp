# Napisz funkcję, której zadaniem będzie wyświetlić na ekranie dowolny znak, dowolną
# ilość razy, w poziomie lub w pionie.

def creating_signs(sign="*", repeat=10, vertical=False):
    for i in range(repeat):
        if vertical:
            print(sign)
        else:
            print(sign + " ", end="")
    if not vertical:
        print()
    print()



creating_signs()
creating_signs(sign="?", repeat=5, vertical=False)
creating_signs(sign="!", repeat=8, vertical=True)
