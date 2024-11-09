#Załóżmy, że na pierwsze pole szachownicy kładziemy 1 ziarno zboża, na
# drugie 2 ziarna, na trzecie 4 ziarna i na każde następne pole dwa razy
# więcej ziaren niż na pole poprzednie. Napisz program, który zasymuluje
# taką sytuację i zliczy sumę wszystkich ziaren na szachownicy.

# 0 1 2 3 4 5... for i in range(64) da nam rezultaty od 0 do 63, ale to i tak są "64 pola" na szachownicy
# 1 2 4 8 16 32... ziarna zboza. Kolejne wartosci to sa potegi 2! Dochodzimy do 64


s = 0
for i in range(64):
    s += 2 ** i #dodaj do sumy za kazdym raze 2 do potegi i

print("Suma wszystkich ziaren zboża na szachownicy to " + str(s))


# założenia: waga 1 ziarna to 0,4mg -> 0,0004g

# 1kg = 1000g
# 1000 kg = 1t

tons = int(s * 0.0004 / 1000 / 1000)
print("ton: ", tons)

# roczna produkcja pszenicy na świecie to 782 mln ton
years = int(tons / 782_000_000)
print("lata: ", years)