from komposisjon_referanser.punkt import *


class Segmentlinje:
    def __init__(self, punktliste=[]):
        self.punkter = punktliste[:]

    # Delegerer det å legge til et punkt til den indre lista
    def legg_til_punkt(self, punktet: Punkt):
        self.punkter.append(punktet)

    def slett_punkt(self, punktet: Punkt):
        self.punkter.remove(punktet)

    def __str__(self):
        resultat = "Segmentlinje: "
        for punkt in self.punkter:
            resultat += punkt.koordinatpar_streng() + ", "
        return resultat
