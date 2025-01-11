#co zrobić kiedy wygenerujemy SYNTAX ERROR czyli błąd składni?

# print("Hello World")
# print("Hello World" #pycharm czerwonym podkreśleniem daje znać że coś jest nie tak
#kiedy jest SYNTAX ERROR to nie wyświetlają się linie dobrze napisane

# print(1 / 0) #składniowo jest OK ale będzie błąd ZeroDivisionError

#mozemy to ominąć składnią TRY:... EXCEPT...

try:
    print(1 / 0)
except:
    print("Coś poszło nie tak...")
