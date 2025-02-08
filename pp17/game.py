import sys

sys.path.append("\\\\DESKTOP-4QM08OI\\Users\\Wojtek-PC\\Desktop\\packages")

from games.lotto import get_user_numbers, check_user_numbers, draw_numbers



print("Witaj w grze LOTTO!")
user_numbers = get_user_numbers()
print("Pobrane liczby to:", user_numbers)

print("\nNaciśnij ENTER, aby dokonać losowania liczb!\n")
input()
lucky_numbers = draw_numbers()
print("Wylosowano liczby:", lucky_numbers)
print()

result = check_user_numbers(user_numbers, lucky_numbers)
if result == 6:
    print("GRATULACJE!", "Jesteś milionerem!")
elif result == 5:
    print("BRAWO!", "Trafiłeś piątkę!", "Zgarniesz sporą sumę!")
elif result == 4:
    print("Hurra!", "Trafiono czwórkę!", "To całkiem niezły wynik!")
elif result == 3:
    print("Trafiono trójkę!", "Przysługuję Ci minimalna wygrana!")
elif result == 2 or result == 1:
    print("Trafiono {} liczbę/y. Było bardzo blisko!".format(result))
else:
    print("To nie jest Twój dzień!")

