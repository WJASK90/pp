temp = 12
is_sun_shining = False

# jeżeli będzie dodatnia temperatura i będzie słonecznie to...
# pójdziemy na spacer a jeżeli nie to zostaniemy w domu
if temp > 0 and is_sun_shining:
    print("Idziemy na spacer")
else:
    print("Zostajemy w domu")

print("-" * 20)

# jeżeli będzie ujemna temperatura lub będzie pochmurnie to...
# zostaniemy w domu a jeżeli nie to pójdziemy na spacer

if not (temp < 0 or not is_sun_shining):
    print("Idziemy na spacer")
else:
    print("Zostajemy w domu")

print("-" * 20)
 # operatory logiczne
 # and - koniunkcja - czytamy jako i
 # or - alternatywa - czytamy jako lub
 # not - negacja - czytamy jak nie

 # iterujemy od 0-9 (10 iteracji)
 # wyświetlamy cyfrę chyba, że...
 # będzie to liczba parzysta lub liczba większa od 6 to wyświetl *

for i in range(10):
    if i % 2 == 0 or i > 6:
        print("*")
    else:
        print(i)

print("-" * 20)

a, b, c = 2, 3, 4

if a < b and b < c:
    print("!!!")