from komposisjon_referanser.punkt import Punkt
from komposisjon_referanser.linjesegment import Linjesegment
from polymorfisme.geometri import Sirkel

#Grensesnitt: FLyttbar
# flytt(delta_x: float, delta_y: float) -> None
#   Flytter objektet det angitte antall punkter i x- og y-retning


# Polymorfisme: Man kan srive kode som fungerer på objekter av mange ulike klasser så lenge
# klassen støtter grensesnittet man forventer. I dette tilfellet fungerer kallet til flytt-metoden
# på alle objekter av klasser som har en slik metode. At jeg skreiv Sirkel klassen etter å
# ha skrevet denne metoden gjør ingen ting.
def flytt_alle(liste_av_flyttbare):
    for objekt in liste_av_flyttbare:
        objekt.flytt(2, 2)


# Lager ei liste som inneholder ulike objekter, men hvor alle er flyttbare
objekt_liste = []
objekt_liste.append(Punkt(5, 6))
objekt_liste.append(Punkt(5, 2))
objekt_liste.append(Linjesegment(Punkt(1,1), Punkt(3, 3)))
objekt_liste.append(Sirkel(10, 10, 4))
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
