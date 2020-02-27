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


# Eksempel på dekorator pattern: Bruk av komposisjon i stedet for arving for å utvide en klasse med ny
# funksjonalitet, i dette eksemplet fagbok som utvider bok
class Fagbok:
    def __init__(self, ISBN, tittel, forfattere, utgivelsesaar, fagfelt, utgave):
        self.bok = Bok(ISBN, tittel, forfattere, utgivelsesaar)         # Lager en instans av Bok og refererer til den
        self.fagfelt = fagfelt                                          # Lagrer egne egenskaper separat
        self.utgave = utgave

    # Viser fram bok-objektet sin ISBN
    @property
    def ISBN(self):
        return self.bok.ISBN

    # Viser fram bok-objektet sin tittel som om det var fagbokas egen. Kan ha tilsvarende for
    # forfatter og utgivelsesår.
    @property
    def tittel(self):
        return self.bok.tittel

    @tittel.setter
    def tittel(self, ny_tittel):
        self.bok.tittel = ny_tittel

    # Delegerer forfatterliste til bok-rederansen.
    def forfatterliste(self):
        return self.bok.forfatterliste()

    # Lager en egen __str__ metode
    def __str__(self):
        resultat = f"Fagbok: {self.bok.tittel}, {self.utgave}. utgave, av " + self.bok.forfatterliste()
        resultat += " i fagfelt " + self.fagfelt + " utgitt i " + str(self.bok.utgivelsesaar)
        resultat += " med ISBN " + self.bok.ISBN
        return resultat


# Forfatter som egen klasse, illustrerer at man kan ha referanser begge veier mellom to objekter,
# og at man trenger det for å kunne navigere begge veier. I dette tilfellet ønsker man at forfatteren
# skal kunne lage ei liste med bøker som vedkommende har skrevet. For å få til det, må forfatteren
# ha ei liste med bøker.
class Forfatter:
    def __init__(self, fornavn, etternavn):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.boker = []                 # Liste med bøker som forfatteren har skrevet

    # Kalles når forfatteren har registrert at vedkommende har skrevet ei bok. Denne sørger for at referansene
    # i både Bok og Forfatter er konsistente gjennom å sjekke om denne forfatteren (self) er med i boka sin liste
    # over forfattere, og setter inn forfatteren i boka sin liste hvis ikke.
    def har_skrevet_bok(self, boka: Bok):
        if self in boka.forfattere:
            self.boker.append(boka)
        else:
            boka.forfattere.append(self)
            self.boker.append(boka)
#            raise ValueError("Forfatteren må ha skrevet boka!")

    def bokliste(self):
        return self.boker


if __name__ == "__main__":
    bok = Bok("24-324-5345", "Hobbiten", ["JRR Tolkien"], 1946)
    fagbok = Fagbok("1-292-22575-0", "Starting out with Python", ["Tony Gaddis"], 2019, "Programmering", 4)
    print(bok)
    print(fagbok)
