name = "jan kowalski"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "jan"
last_name = "kowalski"
full_name = f"{first_name} {last_name}"
print(f"Witaj, {full_name.title()}!")

first_name = "jan"
last_name = "kowalski"
full_name = f"{first_name} {last_name}"
message = f"Witaj, {full_name.title()}!"
print(message)

print("\tPython")
print("Języki programowania:\nPython\nC++\nJava")
print("Języki programowania:\n\tPython\n\tC++\n\tJava")

favorite_language = ' python '
favorite_language = favorite_language.rstrip()
favorite_language = favorite_language.lstrip()
favorite_language = favorite_language.strip()
print(favorite_language)

nostarch_url = 'https://nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)

message = "Dla programisty Johna O'Hary jedną z zalet Pythona jest jego wszechstronność i oddana mu społeczność"
print(message)  #:)