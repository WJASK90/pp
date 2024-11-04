motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ktm')
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

colours = []
colours.append('red')
colours.append('green')
colours.append('blue')
print(colours)

colours.insert(0, 'yellow')
print(colours)

motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop() #metoda .pop zaczyna usuwanie od konca listy (pomysl ze to stos danych, honda jest u podstawy a suzuki na czubku)
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
last_owned = motorcycles.pop()
first_owned = motorcycles.pop(0)
print("Moim ostatnim, posiadanym motocyklem był model " + str(last_owned) + "!")
print("Moim pierwszym, posiadanym motocyklem był model " + str(first_owned.title()) + "!")

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('honda')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print("Motocykle marki " + str(too_expensive.title()) + " są za drogie!")

#cwiczenie 3.4 + 3.5
lista_gosci = ['magda', 'wojtek', 'reksio']
print(lista_gosci)
nieobecny_0 = 'magda'
obecny_1 = 'wojtek'
obecny_2 = 'reksio'
lista_gosci.remove('magda')
print(lista_gosci)
print("Gość o imieniu " + str(nieobecny_0.title()) + " nie może przyjść, co za smutek!")
print("Zapraszam osobę o imieniu " + str(obecny_1.title()) + " na obiad!")
print("Zapraszam osobę o imieniu " + str(obecny_2.title()) + " na obiad!")

#cwiczenie 3.6
lista_gosci = ['magda', 'wojtek', 'reksio']
print(lista_gosci)
lista_gosci.remove('magda')
print("Mamy większy stół, więc mogę zaprosić dodatkowych gości!")
lista_gosci.insert(0, 'arnold schwarzenegger')
lista_gosci.insert(2, 'boyd')
lista_gosci.append('donald trump')
nowy_gosc_1 = 'arnold schwarzenegger'
nowy_gosc_2 = 'boyd'
nowy_gosc_3 = 'donald trump'
print(lista_gosci)
print("Mamy większy stół, więc mogę zaprosić dodatkowych gości! Zapraszam pana " + str(nowy_gosc_1.title()) + " na obiad!")
print("Mamy większy stół, więc mogę zaprosić dodatkowych gości! Zapraszam pana " + str(nowy_gosc_2.title()) + " na obiad!")
print("Mamy większy stół, więc mogę zaprosić dodatkowych gości! Zapraszam pana " + str(nowy_gosc_3.title()) + " na obiad!")

#cwiczenie 3.7
lista_gosci = ['magda', 'wojtek', 'reksio']
print(lista_gosci)
lista_gosci.remove('magda')
print("Mamy większy stół, więc mogę zaprosić dodatkowych gości!")
lista_gosci.insert(0, 'arnold schwarzenegger')
lista_gosci.insert(2, 'boyd')
lista_gosci.append('donald trump')
nowy_gosc_1 = 'arnold schwarzenegger'
nowy_gosc_2 = 'boyd'
nowy_gosc_3 = 'donald trump'
print(lista_gosci)
print("Mamy większy stół, więc mogę zaprosić dodatkowych gości! Zapraszam pana " + str(nowy_gosc_1.title()) + " na obiad!")
print("Mamy większy stół, więc mogę zaprosić dodatkowych gości! Zapraszam pana " + str(nowy_gosc_2.title()) + " na obiad!")
print("Mamy większy stół, więc mogę zaprosić dodatkowych gości! Zapraszam pana " + str(nowy_gosc_3.title()) + " na obiad!")

print("O nie! Mogę zaprosić tylko dwie osoby! Co za tragikomedia!")

lista_gosci = ['arnold schwarzenegger', 'wojtek', 'boyd', 'reksio', 'donald trump']
print(lista_gosci)
popped_lista_gosci_1 = lista_gosci.pop()
popped_lista_gosci_2 = lista_gosci.pop()
popped_lista_gosci_3 = lista_gosci.pop()
print(lista_gosci)
obecny_gosc_1 = 'wojtek'
obecny_gosc_2 = 'arnold schwarzenegger'
print(popped_lista_gosci_1)
print("Wybacz że nie mogę Ciebie zaprosić " + str(popped_lista_gosci_1.title()) + " na obiad! To przez restauracje, jeszcze za to zapłacą!")
print("Wybacz że nie mogę Ciebie zaprosić " + str(popped_lista_gosci_2.title()) + " na obiad! To przez restauracje, jeszcze za to zapłacą!")
print("Wybacz że nie mogę Ciebie zaprosić " + str(popped_lista_gosci_3.title()) + " na obiad! To przez restauracje, jeszcze za to zapłacą!")
print("Cześć! Masz szczęście, dla Ciebie są miejsca " + str(obecny_gosc_1.title()) + " na obiad!")
print("Cześć! Masz szczęście, dla Ciebie są miejsca " + str(obecny_gosc_2.title()) + " na obiad!")
print(lista_gosci)
del lista_gosci[0]
print(lista_gosci)
del lista_gosci[0]
print(lista_gosci)