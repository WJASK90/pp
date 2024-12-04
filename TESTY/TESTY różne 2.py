print("Magda")
print("Wojtek")
print("dom")
message = "Witaj w świecie Pythona!"
print(message)

message = 'Witaj, świecie książki "Python. Instrukcje dla programisty"!'
print(message)

for i in range(3):
    print(i < 3)

for i in range(3):
    print("First")
    print("Second")

password = "SecretWord"
guess1 = "1234"
print(guess1 != password)

password = "SecretWord"
guess = input()
while guess != password:
    guess = input()
print("Access Granted")

