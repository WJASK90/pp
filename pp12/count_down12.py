

def count_down(wishes = True): #piszemy odliczanie do zyczen
    print("Trzy...")
    print("Dwa...")
    print("Jeden...")
    if not wishes:
        return
    print("Szczęśliwego Nowego Roku!")


count_down() #wyswietli sie wszystko lacznie z print

def count_down(wishes = True): #piszemy odliczanie do zyczen
    print("Trzy...")
    print("Dwa...")
    print("Jeden...")
    if not wishes:
        return
    print("Szczęśliwego Nowego Roku!")

count_down(False) #rowniez 0 jest tlumaczone jako False, ale teraz nie da nam ostatniego Print

def count_down(wishes = True): #piszemy odliczanie do zyczen
    print("Trzy...")
    print("Dwa...")
    print("Jeden...")
    if wishes == False:
        return
    print("Szczęśliwego Nowego Roku!")

count_down()