from enkelt_kortspill.kort import *


# Spiller
class Spiller:
    def __init__(self, navn, kort):
        self.navn = navn
        self.kort = kort

    def __str__(self):
        return f"Spiller {self.navn} har kortet {self.kort}"

    def har_hoyere_verdi(self, verdi):
        if self.kort.verdi > verdi:
            return True
        else:
            return False

    def har_denne_verdien(self, verdi):
        return self.kort.verdi == verdi

    def verdi(self):
        return self.kort.verdi


# Kortspill
class Kortspill:
    def __init__(self):
        self.kortstokk = Kortstokk()
        self.kortstokk.lag_standard_kort()
        self.kortstokk.stokk()
        self.spillere = []

    def lag_spillere(self):
        antall_spillere = int(input("Hvor mange spillere skal det være?"))
        for i in range(antall_spillere):
            navn = input(f"Navnet til spiller {i}: ")
            kortet = self.kortstokk.trekk()
            spilleren = Spiller(navn, kortet)
            self.spillere.append(spilleren)

    def vinner(self):
        vinnere = []                # Kan ha flere som har høyeste kort! Derfor liste.
        hoyeste_verdi = 0
        for spiller in self.spillere:
            if spiller.har_hoyere_verdi(hoyeste_verdi):
                vinnere.clear()
                vinnere.append(spiller)
                hoyeste_verdi = spiller.verdi()
            elif spiller.har_denne_verdien(hoyeste_verdi):
                vinnere.append(spiller)
        return vinnere

    def skriv_ut_spillere(self):
        print("Spillere: ")
        for spiller in self.spillere:
            print(spiller)

    def spill_spillet(self):
        self.lag_spillere()
        print("Enkelt kortspill")
        self.skriv_ut_spillere()
        vinnere = self.vinner()
        while len(vinnere) > 1:
            print("\nUavgjort!")
            self.spillere = vinnere
            for spiller in self.spillere:
                spiller.kort = self.kortstokk.trekk()
            self.skriv_ut_spillere()
            vinnere = self.vinner()
        print(f"Og vinneren er: {vinnere[0]}")


if __name__ == "__main__":
    spillet = Kortspill()
    spillet.spill_spillet()
