from gjennomgang_oving_6.kort import *

START_HAANDSTORRELSE = 5


# Oppgave b)
class Spiller:
    def __init__(self, navn):
        self.navn = navn
        self.haand = []

    def __str__(self):
        resultat = "Spiller: " + self.navn + "\nHånd:\n"
        for index, kort in enumerate(self.haand):
            resultat += str(index) + ": " + str(kort) + "\n"
        return resultat


# Oppgave c, d
class Spillet:
    def __init__(self):
        self.spillerne = []
        self.stokken = Kortstokk()
        self.stokken.lag_standard_kort()
        self.stokken.stokk()
        self.bunken = Kortstokk()
        kortet = self.stokken.trekk()
        self.bunken.legg(kortet)
        self.tur = 0        # Indeks inn i lista over spillere
        self.spillet_i_gang = True

    # Oppgave e
    def lag_spillerne(self):
        antall_spillere = int(input("Antall spillere: "))
        for i in range(antall_spillere):
            navn = input(f"Navnet til spiller {i}: ")
            spilleren = Spiller(navn)
            self.spillerne.append(spilleren)
            for k in range(START_HAANDSTORRELSE):
                kortet = self.stokken.trekk()
                spilleren.haand.append(kortet)

    # Oppgave f
    def lovlig_trekk(self, kortet):
        if kortet.verdi == 8:
            return True
        overste_kort = self.bunken.overste_kort()
        if kortet.har_samme_type(overste_kort):
            return True
        if kortet.har_samme_verdi(overste_kort):
            return True
        return False

    # Oppgave f
    def legg_aatter(self, nv_spiller):
        print(nv_spiller)
        kort_nr = int(input("\n Du la en åtter og kan legge et kort til. hvilket?"))
        kortet = nv_spiller.haand[kort_nr]
        self.bunken.legg(kortet)
        del nv_spiller.haand[kort_nr]
        if len(nv_spiller.haand) == 0:
            print("Gratulerer! Du har vunnet!")
            exit()

    # Oppgave f
    def tom_kortstokk(self):
        self.stokken = self.bunken
        self.bunken = Kortstokk()
        self.bunken.legg(self.stokken.trekk())
        self.stokken.stokk()

    # Oppgave f
    def spill_tur(self):
        nv_spiller = self.spillerne[self.tur]
        print(nv_spiller)
        print(f"\nØverste kort i bunken: {self.bunken.overste_kort()}")
        print()
        kort_nr = int(input("Hvilket kort ønsker du å legge? " +
                           "Et ugyldig kort vil gjøre at du " +
                           "trekker kort i stedet. "))
        kortet = nv_spiller.haand[kort_nr]
        if self.lovlig_trekk(kortet):
            self.bunken.legg(kortet)
            del nv_spiller.haand[kort_nr]
            if len(nv_spiller.haand) == 0:
                print("Gratulerer! Du har vunnet!")
                exit()
            if kortet.verdi == 8:
                self.legg_aatter(nv_spiller)
        else:
            nv_spiller.haand.append(self.stokken.trekk())
            if self.stokken.er_tom():
                self.tom_kortstokk()

    # Oppgave f
    def spill_spillet(self):
        while self.spillet_i_gang:
            self.spill_tur()
            self.tur += 1
            if self.tur >= len(self.spillerne):
                self.tur = 0


# Oppgave g
if __name__ == "__main__":
    spillet = Spillet()
    spillet.lag_spillerne()
    spillet.spill_spillet()
