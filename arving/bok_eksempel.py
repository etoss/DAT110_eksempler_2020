#Baseklasse Bok, for generelle bøker
class Bok:
    def __init__(self, ISBN, tittel, forfattere, utgivelsesaar):
        self.__ISBN = ISBN
        self.tittel = tittel
        self.forfattere = forfattere
        self.utgivelsesaar = utgivelsesaar

    # ISBN er read-only
    @property
    def ISBN(self):
        return self.__ISBN

    # Metode for å få ut en liste av forfattere som en streng
    def forfatterliste(self):
        resultat = ""
        for forfatter in self.forfattere:
            resultat += forfatter + ", "
        return resultat

    # String-metoden, sørger for at man kan lage en streng av boka
    def __str__(self):
        resultat = "Bok: " + self.tittel + " av " + self.forfatterliste()
        resultat += " utgitt i " + str(self.utgivelsesaar)
        return resultat


# Subklasse av Bok for fagbøker. Du arver:
#
# Alle egenskaper
# Alle metoder
class Fagbok(Bok):
    # Egen konstruktør, overstyrer (override) konstruktøren til Bok
    def __init__(self, ISBN, tittel, forfattere, utgivelsesaar, fagfelt, utgave):
        # Kaller superklassen (Bok) sin konstruktør. Dette må alltid gjøres først!
        super().__init__(ISBN, tittel, forfattere, utgivelsesaar)

        # Lager egne egenskaper for fagbøker
        self.fagfelt = fagfelt
        self.utgave = utgave

    def __str__(self):
        resultat = f"Fagbok: {self.tittel}, {self.utgave}. utgave, av " + self.forfatterliste()
        resultat += " i fagfelt " + self.fagfelt + " utgitt i " + str(self.utgivelsesaar)
        resultat += " med ISBN " + self.ISBN
        return resultat


# Man kan fint ha flere subklasser av samme superklasse
class Fiksjonsbok(Bok):
    def __init__(self, ISBN, tittel, forfattere, utgivelsesaar, sjanger):
        super().__init__(ISBN, tittel, forfattere, utgivelsesaar)
        self.sjanger = sjanger


# En klasse som arver fra Fagbok og derfor også arver indirekte fra Bok.
class Artikkelsamling(Fagbok):
    def __init__(self, ISBN, tittel, forfattere, utgivelsesaar, fagfelt, utgave):
        super().__init__(ISBN, tittel, forfattere, utgivelsesaar, fagfelt, utgave)
        self.artikler = []

    def legg_til_artikkel(self, artikkel):
        self.artikler.append(artikkel)

    def legg_til_artikler(self, artikler):
        for artikkel in artikler:
            self.legg_til_artikkel(artikkel)

    def artikkelliste_streng(self):
        resultat = ""
        for indeks, artikkel in enumerate(self.artikler):
            resultat += f"{indeks}: {artikkel} \n"
        return resultat


# Artikkelsamling med teller, eksempel på "fragile base class" problemet.
#
# En endring i implementasjonen av legg_til_artikler metoden fra klassen
# Artikkelsamling fører til at man også må endre denne metoden i
# ArtikkelsamlingMedTeller.
class ArtikkelsamlingMedTeller(Artikkelsamling):
    def __init__(self, ISBN, tittel, forfattere, utgivelsesaar, fagfelt, utgave):
        super().__init__(ISBN, tittel, forfattere, utgivelsesaar, fagfelt, utgave)
        self.teller = 0

    def legg_til_artikkel(self, artikkel):
        super().legg_til_artikkel(artikkel)
        self.teller += 1

    def legg_til_artikler(self, artikler):
        super().legg_til_artikler(artikler)
        self.teller += len(artikler)


# Testekode
if __name__ == "__main__":
    boka = Fagbok("1-292-22575-0", "Starting out with Python", ["Tony Gaddis"], 2019, "Programmering", 4)
    print(boka)
    bok2 = Fiksjonsbok("3456-234-2", "Hobbiten", ["JRR Tolkien"], 1946, "Fantasy")
    print(bok2)
    samlingen = ArtikkelsamlingMedTeller("1234-453-2345", "Advanced Database Systems", ["Michael Stonebraker", "Tony Sellis"], 2014, "Databaser", 2)
    samlingen.legg_til_artikkel("Test1")
    samlingen.legg_til_artikler(["Test2", "En artikkel", "Navn"])
    print(samlingen.artikkelliste_streng())
    print(samlingen.teller)
