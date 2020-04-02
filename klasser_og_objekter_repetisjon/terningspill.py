import random


# En klasse for terninger. En terning har et antall sider (ikke nødvendigvis 6, terninger med
# 4, 6, 8, 10, 12 og 20 sider ble vist i forelesningen) og en verdi. Verdien er tallet som ble
# kastet sist.
class Terning:
    def __init__(self, antall_sider):
        self.antall_sider = antall_sider
        self.verdi = 1

    def kast(self):
        self.verdi = random.randint(1, self.antall_sider)
        print(f"Kaster terningen med {self.antall_sider} sider og får {self.verdi}")


# Klasse for en spiller. Denne lagrer navn og poengsum men har ingen egen oppførsel
# (ingen egne metoder)
class Spiller:
    def __init__(self, navn):
        self.navn = navn
        self.poengsum = 0


# Funksjon for å lage spillerne
def lag_spillere():
    antall_spillere = int(input("Antall spillere: "))
    spillerliste = list()
    for i in range(antall_spillere):
        navn = input(f"Navn til spiller {i}: ")
        spilleren = Spiller(navn)
        spillerliste.append(spilleren)
    return spillerliste


# Spiller spillet
def spill_spillet():
    # Lager en 6-sidet og en 10-sidet terning
    terning1 = Terning(6)
    terning2 = Terning(10)

    # Lager spillerne
    spillerliste = lag_spillere()

    # Går gjennom lista med spillere for å kaste terningene for dem
    for spiller in spillerliste:
        terning1.kast()         # Kaster den 6-sidete terningen
        terning2.kast()         # Kaster den 10-sidete terningen
        tallsum = terning1.verdi + terning2.verdi       # Henter ut verdiene til de to terningene og summerer dem
        spiller.poengsum = tallsum                      # Lagrer summen i spilleren sin poengsum egenskap
        print(f"Spiller {spiller.navn} har {spiller.poengsum} poeng")   # Skriver ut poengsummen

    # Finner vinneren. Starter med første spiller
    vinner = spillerliste[0]
    vinner_poeng = vinner.poengsum

    # Går gjennom lista med spillere. Har denne spilleren høyere poengsum enn foreløpig vinner,
    # sett vinner lik denne spilleren og vinner-poengsummen til denne spilleren sine poeng
    for spiller in spillerliste:
        if spiller.poengsum > vinner_poeng:
            vinner = spiller
            vinner_poeng = vinner.poengsum

    # Skriv ut vinneren
    print(f"Vinneren er {vinner.navn} med {vinner.poengsum} poeng")


# Sett i gang spilet hvis dette scriptet er det som blir kjørt. Blir det i stedet
# importert, ikke gjør noe.
if __name__ == "__main__":
    spill_spillet()
