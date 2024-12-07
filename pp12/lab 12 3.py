# 3. Napisz program obliczającej wskaźnik BMI (Body Mass Index), w tym celu:
# • zapytaj użytkownika o wzrost i wagę,
# • stwórz funkcję obliczającą wskaźnik BMI na podstawie podanych przez użytkownika danych,
# • stwórz funkcję wyznaczającą odpowiednią kategorię (niedowaga, waga prawidłowa, nadwaga,
# otyłość) na podstawie wskaźnika BMI,
# • zaprezentuj wyniki korzystając z wcześniej przygotowanych funkcji.

print("Obliczenie wskaźnika BMI!")

def get_data(): #pobieramy dane ktore wyglada jak odwrotnosc PRINT, zwraca dane do nas
    weight_in_kg = float(input("Podaj swoją wagę w kg: "))
    hight_in_cm =  float(input("Podaj swój wzrost w cm: "))
    return [weight_in_kg, hight_in_cm] #robimy z tego liste
def calculate_bmi(weight_in_kg, hight_in_m): #jakie dane pobiera? dwie liczby typu FLOAT, zwraca BMI
    return weight_in_kg / hight_in_m ** 2 #** 2 czyli podniesione do kwadratu, nie potrzeba nawiasow bo potega ma wyzszy priorytet

def determine_bmi_category(bmi): #pobiera jedna liczbe FLOAT (bmi) a zwraca STR
    if bmi < 18.5:
        return "Niedowaga"
    elif bmi < 25:
        return "Waga prawidłowa"
    elif bmi < 30:
        return "Nadwaga"
    else:
        return "Otyłość"


weight_in_kg, hight_in_cm = get_data()
bmi = calculate_bmi(weight_in_kg, hight_in_cm * .01)
category = determine_bmi_category(bmi)

print("Wskaźnik BMI: ", round(bmi, 2))
print("Kategoria:", category)