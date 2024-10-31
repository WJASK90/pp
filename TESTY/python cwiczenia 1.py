#cwiczenie 1

imie_a = "Magda"

print("Cześć " + str(imie_a) + "!, Czy chcesz dzisiaj poznawać Pythona?")

imie_b = "cymbała"

print(imie_b.lower())
print(imie_b.upper())
print(imie_b.title())

print('Alber Einstein powiedział kiedyś: "Osoba, która nigdy nie popełniła błedu, jest kimś, kto nigdy nie próbował czegoś nowego"')

famous_person = "Albert Einstein"
message = ' powiedział kiedyś: "Osoba, która nigdy nie popełniła błedu, jest kimś, kto nigdy nie próbował czegoś nowego"'
famous_message = f"{famous_person}{message}"
print(famous_message)

print("\tZygmunt")
print("Zygmunt\t")

print("Zygmunt\t\nIrena\t\n")

irena_1 = " Irena"
irena_2 = "Irena "
irena_3 = " Irena "
print(irena_1)
print(irena_1.lstrip())
print(irena_2)
print(irena_2.rstrip())
print(irena_3)
print(irena_3.strip())

filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))