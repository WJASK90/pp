# Elektroniczny dziennik z ocenami studentów
# - wprowadzanie ocen
# - wyswietlanie ocen wraz z wprowadzoną średnią

#NAJLEPIEJ UZYC SLOWNIK GDZIE BEDZIEMY MIEC SPIS STUDENTOW, nie krotka lub lista bo trudno sie do tego odwołać

# students = {"Tomek": [2, 3, 4, 2], "Agata": [5, 5, 5, 5]} # w strukturze beda wartosci ktore beda LISTAMI

def average(marks):
    return sum(marks) / len(marks)
def get_data(): #funkcja do pobierania danych
    students = {}
    while True: #pytamy dopoki ktos nie uzna ze koniec wprowadzania
        student = input("Podaj imię studenta: ")
        if student == "": #jak nie ma imienia
            break
        mark = float(input("Podaj ocenę: ")) #dajemy float bo moze ktos wpisze 3.5
        if mark < 2 or mark > 5: #jak beda dziwne oceny
            break

        if student in students: #jezeli student jest to aktualizujmy jego oceny, odwolajmy sie do slownika students po kluczu students
            marks = students[student] #jezeli byl, to aktualizujemy
            marks.append(mark)
        else:
            marks = [mark]

        students.update({student: marks}) #jak go nie bylo, to go dodajemy

    return students

def print_summary(students): #podsumowanie
    counter = 1
    for student in sorted(students.keys()): #posortujemy dane
        marks = students[student]
        print(counter, student, "oceny:", marks, "średnia:", average(marks))
        counter += 1

print_summary(get_data()) #pobierz podsumowanie pobranych danych od uzytkownika
