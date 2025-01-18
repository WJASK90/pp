# 1. Wyświetl polski alfabet (tylko małe litery, także litery ze znakami diakrytycznymi)
# wraz z punktami kodowymi dla każdej litery.

# Polski alfabet (małe litery z diakrytycznymi znakami)
polski_alfabet = [aąbcćdeęfghijklłmnoópqrsśtuvwxyzźżz]

for litera in polski_alfabet:
    print(litera, ord(litera))
