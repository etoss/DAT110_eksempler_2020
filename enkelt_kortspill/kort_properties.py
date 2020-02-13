import random


# Klasse som representerer et vanlig spillkort.
class Kort:
    KNEKT = 11              # Konstant definert i en klasse, til bruk for objekter i den klassen.
    DAME = 12               # Bruk Kort.DAME for å referere til denne.
    KONGE = 13

    def __init__(self, korttype, verdi):
        self.__korttype = korttype          # Lager privat instansvariabel. Private variabler starter med to underscores
        self.__verdi = verdi

    @property
    def verdi(self):
        return self.__verdi

    @property
    def korttype(self):                     # Property korttype
        return self.__korttype

    def har_samme_type(self, kortet):
        if self.korttype == kortet.korttype:
            return True
        else:
            return False

    def har_samme_verdi(self, kortet):
        return self.verdi == kortet.verdi

    def __str__(self):
        resultat = self.korttype + " "
        if self.verdi == 1:
            resultat += "ess"
        elif self.verdi <= 10:
            resultat += str(self.verdi)
        elif self.verdi == Kort.KNEKT:
            resultat += "knekt"
        elif self.verdi == Kort.DAME:
            resultat += "dame"
        elif self.verdi == Kort.KONGE:
            resultat += "konge"
        else:
            resultat += "ugyldig"
        return resultat


# Kortstokk
class Kortstokk:
    def __init__(self):
        self.kortene = []

    def lag_standard_kort(self):
        for verdi in range(1, 14):
            self.kortene.append(Kort("Spar", verdi))
            self.kortene.append(Kort("Kløver", verdi))
            self.kortene.append(Kort("Hjerter", verdi))
            self.kortene.append(Kort("Ruter", verdi))

    def stokk(self):
        random.shuffle(self.kortene)

    def trekk(self):
        kortet = self.kortene[-1]
        del self.kortene[-1]
        return kortet

    def legg(self, kortet):
        self.kortene.append(kortet)

    def overste_kort(self):
        return self.kortene[-1]

    def __str__(self):
        resultat = "kortstokk: \n"
        for kort in self.kortene:
            resultat += str(kort) + "\n"
        return resultat


if __name__ == "__main__":
    stokken = Kortstokk()
    stokken.lag_standard_kort()
    stokken.stokk()
    overste_kort = stokken.overste_kort()
    print(overste_kort)
    overste_kort = stokken.trekk()
    print(overste_kort)
    overste_kort = stokken.trekk()
    print(overste_kort)
    print(stokken)
    bunken = Kortstokk()
    bunken.legg(overste_kort)
    print(bunken)

