from komposisjon_referanser.punkt import Punkt
from komposisjon_referanser.linjesegment import Linjesegment
from polymorfisme.geometri import Sirkel, Punkt3D, Kvadrat

#Grensesnitt: Flyttbar
# flytt(delta_x: float, delta_y: float) -> None
#   Flytter objektet det angitte antall piksler i x- og y-retning

# Signatur til en metode: navn + parametre + returtype

# Polymorfisme: Man kan skrive kode som fungerer på objekter av mange ulike
# klasser så lenge klassen støtter grensesnittet man forventer.
# I dette tilfellet fungerer kallet til flytt-metoden på alle objekter av
# klasser som har en slik metode. At jeg skreiv Sirkel klassen etter å
# ha skrevet denne metoden gjør ingen ting.
def flytt_alle(liste_av_flyttbare):
    for objekt in liste_av_flyttbare:
        objekt.flytt(2, 2)


def total_areal(liste_av_omraade):
    total = 0.0
    for objekt in liste_av_omraade:
        total += objekt.areal()
    return total


# Lager ei liste som inneholder ulike objekter, men hvor alle er flyttbare
objekt_liste = []
objekt_liste.append(Punkt(5, 6))
#objekt_liste.append(Punkt(5, 2))   Kommentert ut for å gjøre debugger-demoen raskere
objekt_liste.append(Linjesegment(Punkt(1,1), Punkt(3, 3)))
objekt_liste.append(Sirkel(10, 10, 4))
objekt_liste.append(Kvadrat(5, 5, 5))
#objekt_liste.append(Punkt3D(7, 5, 3))      Kommentert ut siden denne genererer en exception siden Punkt3D har en flytt metode med feil signatur
objekt_liste.append(Punkt(9, 1))

# Skriver ut objektene før flytting
for objekt in objekt_liste:
    print(objekt)

# Flytter objektene
flytt_alle(objekt_liste)

# Skriver ut objektene etter flytting
print()
for objekt in objekt_liste:
    print(objekt)

# Lager ei liste med områder
omraade_liste = []
omraade_liste.append(Sirkel(10, 10, 4))
omraade_liste.append(Kvadrat(5, 5, 5))
#omraade_liste.append(Punkt3D(3, 3, 3))     Kommentert ut siden denne genererer en exception siden Punkt3D sin areal metode har feil returverdi (None)

# Regner ut arealet
print(total_areal(omraade_liste))
