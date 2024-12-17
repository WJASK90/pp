# 3. Zabezpiecz program zliczający punkty w grach (moduł 14, lab 3) przed
# wprowadzaniem błędnych danych przez użytkownika.

def safe_int(arg):
    try:
        return int(arg)
    except: #jezeli wystapi jakis blad to ma zwrocic NONE