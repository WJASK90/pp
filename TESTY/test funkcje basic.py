def powitanie(imie="Jan"):
    print("Cześć, {}!".format(imie))

powitanie("Wojtek")

def introduce(first_name, last_name="Jaskot"): #napis USAGE z liczba nad def oznacza ile razy funkcja jest uzywana w kodzie
    print("Cześć, jestem", first_name, last_name + ".")

introduce(first_name="Magdalena")