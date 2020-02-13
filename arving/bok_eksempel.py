class Bok:
    def __init__(self, ISBN, tittel, forfattere, utgivelsesaar):
        self.__ISBN = ISBN
        self.tittel = tittel
        self.forfattere = forfattere
        self.utgivelsesaar = utgivelsesaar

    @property
    def ISBN(self):
        return self.__ISBN

    def forfatterliste(self):
        resultat = ""
        for forfatter in self.forfattere:
            resultat += forfatter + ", "
        return resultat

    def __str__(self):
        resultat = "Bok: " + self.tittel + " av " + self.forfatterliste()
        resultat += " utgitt i " + str(self.utgivelsesaar)
        return resultat


class Fagbok(Bok):
    def __init__(self, ISBN, tittel, forfattere, utgivelsesaar, fagfelt, utgave):
        super().__init__(ISBN, tittel, forfattere, utgivelsesaar)
        self.fagfelt = fagfelt
        self.utgave = utgave

    def __str__(self):
        resultat = f"Fagbok: {self.tittel}, {self.utgave}. utgave, av " + self.forfatterliste()
        resultat += " i fagfelt " + self.fagfelt + " utgitt i " + str(self.utgivelsesaar)
        resultat += " med ISBN " + self.ISBN
        return resultat


class Fiksjonsbok(Bok):
    def __init__(self, ISBN, tittel, forfattere, utgivelsesaar, fagfelt, utgave, sjanger):
        super().__init__(ISBN, tittel, forfattere, utgivelsesaar)
        self.sjanger = sjanger


class Artikkelsamling(Fagbok):
    def __init__(self, ISBN, tittel, forfattere, utgivelsesaar, fagfelt, utgave):
        super().__init__(ISBN, tittel, forfattere, utgivelsesaar, fagfelt, utgave)
        self.artikler = []

    def legg_til_artikkel(self, artikkel):
        self.artikler.append(artikkel)

    def legg_til_artikler(self, artikler):
        for artikkel in artikler:
            self.artikler.append(artikkel)

    def artikkelliste_streng(self):
        resultat = ""
        for indeks, artikkel in enumerate(self.artikler):
            resultat += f"{indeks}: {artikkel} \n"
        return resultat

if __name__ == "__main__":
    boka = Fagbok("1-292-22575-0", "Starting out with Python", ["Tony Gaddis"], 2019, "Programmering", 4)
    print(boka)
    samlingen = Artikkelsamling("1234-453-2345", "Advanced Database Systems", ["Michael Stonebraker", "Tony Sellis"], 2014, "Databaser", 2)
    samlingen.legg_til_artikkel("Test1")
    samlingen.legg_til_artikler(["Test2", "En artikkel", "Navn"])
    print(samlingen.artikkelliste_streng())

