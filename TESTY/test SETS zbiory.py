#zbiory (sets) nie mogą mieć duplikatów, są ZMIENNE więc działają funkcje add() oraz remove()

friends = {"Anna", "Mery", "Mery", "Jonathan"}

print(friends)

guests = {"Anna", "Mery", "Jonathan"}

guests.add("Robert")

print(guests)

#union() łączy dwa sety bez duplikatów

set1 = {"apple", "banana"}
set2 = {"banana", "cherry"}
combined_set = set1.union(set2)
print(combined_set)

#difference() daje nam zbiór (set) z elementami z pierwszego seta ale nie z drugiego, czyli tez usuwa duplikat

set3 = {"apple", "banana", "cherry"}
set4 = {"banana", "orange"}
unique = set3.difference(set4)
print(unique)
