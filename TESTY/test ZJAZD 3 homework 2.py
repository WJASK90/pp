# Chcemy ułożyć wieżę z puszek. Wieża składa się z poziomów, gdzie każdy
# wyższy poziom wymaga jednej puszki mniej niż poziom na którym go
# zbudowano. Korzystając z rekurencji napisz program, który pozwoli
# wyliczyć ilość potrzebnych puszek do wybudowania wieży o zadanym
# poziomie oraz ilość poziomów wieży jakie jesteśmy wstanie ułożyć z
# dostępnej liczby puszek. Przykład: jeżeli chcemy ułożyć 3 poziomową
# wieżę potrzebujemy 6 puszek a np. mając 10 puszek, ułożymy 4
# poziomową wieżę.


# Funkcja obliczająca liczbę puszek potrzebnych do zbudowania wieży o n poziomach
def needed_cans(n):
    if n == 0:
        return 0
    else:
        return n + needed_cans(n - 1)

# Funkcja obliczająca maksymalną liczbę poziomów, które można zbudować z dostępnych puszek
def max_levels(cans, current_level=0):
    if needed_cans(current_level + 1) <= cans:
        return max_levels(cans, current_level + 1)
    else:
        return current_level

# Funkcja budująca wieżę z symbolu
def build_tower(levels, symbol="@"):
    tower = []
    for level in range(1, levels + 1):
        tower.append(symbol * level)
    return tower

# Przykład użycia
levels = 3
cans_needed = needed_cans(levels)
print(f"Do zbudowania {levels}-poziomowej wieży potrzebujemy {cans_needed} puszek.")

# Obliczanie, ile poziomów można zbudować z dostępnych puszek
available_cans = 10
max_possible_levels = max_levels(available_cans)
print(f"Z {available_cans} puszek można zbudować wieżę o {max_possible_levels} poziomach.")

# Budowanie wieży
tower_levels = build_tower(max_possible_levels)
print("Wieża zbudowana z dostępnych puszek:")
for level in tower_levels:
    print(level)