from komposisjon_referanser.punkt import *


# Segmentlinje er ei linje som består av en serie med linjesegmenter. Dette
# kan representeres ved ei liste av punkter.
class Segmentlinje:
    def __init__(self, punktliste=None):
        if punktliste is None:
            self.punkter = []
        else:
            self.punkter = punktliste[:]

    # Delegerer det å legge til et punkt på slutten av segmentlinja til den indre lista
    def legg_til_punkt(self, punktet: Punkt):
        self.punkter.append(punktet)

    # Delegerer det å slette et punkt til den indre lista
    def slett_punkt(self, punktet: Punkt):
        self.punkter.remove(punktet)

    # For å få ut en strengrepresentasjon, spør den indre lista om elementene sine og spør deretter
    # elementene om koordinatpar-strengen deres.
    def __str__(self):
        resultat = "Segmentlinje: "
        for punkt in self.punkter:
            resultat += punkt.koordinatpar_streng() + ", "
        return resultat


if __name__ == "__main__":
    linje = Segmentlinje()
    linje.legg_til_punkt(Punkt(1, 1))
    linje.legg_til_punkt(Punkt(5, 4))
    linje.legg_til_punkt(Punkt(10, 4))
    linje.legg_til_punkt(Punkt(10, 1))
    print(linje)
