liste = [0, 1, 2, 3, 4, 5]  # Lager ei liste som inneholder elementene 0, 1, 2, 3, 4, 5
print("Utskrift av elementer i ei liste")
print(liste[0])             # Skriver ut det første elementet i lista. Python starter å telle på 0.
print(liste[3])             # Skriver ut det fjerde elementet i lista
print(liste[-1])            # Skriver ut det siste elementet i lista. Negative indekser teller bakfra.
print(liste[-3])            # Skriver ut det tredje siste elementet i lista.
liste.append(6)             # Legger til tallet 6 på slutten av lista.
print(liste[-1])

print("\n Lengden til lista: ")
print(len(liste))           # len funksjonen gir lengden til ei liste

print("\n Elementene i lista")
for element in liste:       # For hvert element i lista, utfør blokken (skriv ut elementet i dette tilfellet)
    print(element)
liste4 = [0,1]*5            # *-operatoren gjør repetisjoner av ei liste. liste4 blir ei liste med 5 repetisjoner av [0, 1]
liste5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("\n List slices")
liste_test = liste5[2:5]    # List slicing, lager ei ny liste fra liste5 som starter på index 2 og går til men ikke med index 5
for element in liste_test:
    print(element)
liste_test = liste5[:5]     # List slice som starter på starten og går til men ikke med element 5
liste_test = liste5[5:]     # List slice som starter på element 5 og går til slutten av lista
liste_test = liste5[1:14:2] # List slice som starter på index 2, går til index 14, og bare tar med hvert andre element.
                            # At index 14 er langt forbi slutten av lista spiller ingen rolle, den stopper
                            # automatisk når den når slutten av lista.

print("\n Lister av lister")
liste_av_lister = list()    # Lager ei tom liste
liste_av_lister.append([2, 3, 4, 5])       # Lister kan inneholde hva som helst, inkludert andre lister
liste_av_lister.append([6, 7, 8])
liste_av_lister.append([9, 10])
print(liste_av_lister[1][2])                # Henter ut det tredje elementet i det andre elementet i lista.

print("\n Enumerate funksjonen tar ut både index og verdi")
for teller, verdi in enumerate(liste5):     # Henter ut både index (teller) og verdi for hvert element i lista
    print(str(teller) + ": " + str(verdi))

print("\n referanser og kopiering av lister")
referanse_kopi = liste5     # referanse_kopi settes til å referere til samme liste som liste5
liste5[5] = 23              # Endrer liste5
print("Lista: " + str(liste5))
print("referansekopi: " + str(referanse_kopi))       # Endringen er synlig også gjennom referanse_kopi referansen

ekte_kopi = liste5[:]       # En måte å kopiere lister på, lager et list slice som inneholder hele lista
liste5[7] = 13
print("Lista: " + str(liste5))
print("Ekte kopi: " + str(ekte_kopi))            # Ekte kopi er ikke endret siden det er en annen liste
