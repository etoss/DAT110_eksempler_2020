from komposisjon_referanser.punkt import *


# Refleksiv funksjon. Eksempel a+b = b+a
#
# For avstand: avstand(a, b) == avstand(b, a)
def avstand(punkt1: Punkt, punkt2: Punkt):
    x_diff = punkt1.x - punkt2.x
    y_diff = punkt1.y - punkt2.y
    return math.sqrt(x_diff ** 2 + y_diff ** 2)


# Segmentlinje er ei linje som består av en serie med linjesegmenter. Dette
# kan representeres ved ei liste av punkter.
class Segmentlinje:
    def __init__(self, punktliste=None):
        if punktliste is None:
            self.punkter = []
        else:
            self.punkter = punktliste[:]        # list slicing gir en grunn kopi av lista

    # Delegerer det å legge til et punkt på slutten av segmentlinja til den indre lista
    def legg_til_punkt(self, punktet: Punkt):
        self.punkter.append(punktet)

    # Delegerer det å slette et punkt til den indre lista
    def slett_punkt(self, punktet: Punkt):
        self.punkter.remove(punktet)

    def lengde(self):
        total_avstand = 0       # Akkumulator
        for i in range(1, len(self.punkter)):
            total_avstand += avstand(self.punkter[i-1], self.punkter[i])
        return total_avstand

    # For å få ut en strengrepresentasjon, spør den indre lista om elementene sine og spør deretter
    # elementene om koordinatpar-strengen deres.
    def __str__(self):
        resultat = "Segmentlinje: "
        for punkt in self.punkter:
            resultat += punkt.koordinatpar_streng() + ", "
        return resultat


# En region representerer man ofte med grenselinja, som kan være ei segmentlinje. Eksempel på komposisjon siden
# regionen har en grenselinje.
#
# Kan lage nye objekter igjen basert på regionen, eksempel en skog som har en region og i tillegg for eksempel
# et dominerende treslag og en eier.
class Region:
    def __init__(self, grenselinje: Segmentlinje):
        self.grenselinje = grenselinje

    def grense(self):
        return self.grenselinje

    # Delegerer. Omkrets av en region er lengden til grenselinja
    def omkrets(self):
        return self.grenselinje.lengde()

    # Må regne ut selv siden segmentlinje ikke har et areal
    def areal(self):
        total_areal = 0.0
        for i in range(1, len(self.grenselinje.punkter)):
            total_areal += areal_trapes(self.grenselinje.punkter[i-1], self.grenselinje.punkter[i])
        return abs(total_areal)     # Hvis negativ, bytt fortegn. Blir negativ eller positiv anhengig av retningen til grenselinja.


def areal_trapes(start: Punkt, slutt: Punkt):
    x_avstand = slutt.x - start.x
    y_hoyde = min(start.y, slutt.y)
    areal_rektangel = x_avstand*y_hoyde
    y_differanse = max(start.y, slutt.y) - y_hoyde
    areal_trekant = 0.5*x_avstand*y_differanse
    return areal_trekant + areal_rektangel


if __name__ == "__main__":
    linje = Segmentlinje()
    linje.legg_til_punkt(Punkt(1, 1))
    linje.legg_til_punkt(Punkt(5, 4))
    linje.legg_til_punkt(Punkt(10, 4))
    linje.legg_til_punkt(Punkt(10, 1))
    linje.legg_til_punkt(Punkt(1, 1))       # Lukker linja slik at den fungerer som region
    print(linje)
    print(linje.lengde())
    region = Region(linje)
    print(f"Region omkrets: {region.omkrets()}")
    print(f"Regionens areal: {region.areal()}")
