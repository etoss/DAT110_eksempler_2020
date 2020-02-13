import math

# Første eksempel på en egendefinert klasse: Punkt
#
# Denne versjonen er gjort så enkel som mulig, og tilsvarer versjonen jeg først demonstrerte
class Punkt:
    # Konstruktør, denne skal lage objektet. self er objektet som blir
    # lagd. De andre parameterne er som for en funksjon
    def __init__(self, start_x=0, start_y=0):
        self.x = start_x                        # Definerer at punkt-objekter skal ha variabelen x, og setter den lik start_x
        self.y = start_y

    # Metode for klassen Punkt. Self er objektet som metoden blir kalt på. Resten av parameterne er
    # som for en annen funksjon. Metoder er funksjoner bortsett fra at de er definert inne i en klasse
    # og derfor har denne spesielle self parameteren, som alltid skal stå først.
    def flytt(self, delta_x, delta_y):
        self.x += delta_x                       # Endrer objektet sin x-variabel
        self.y += delta_y

    # Python spesialmetode. Alle slike spesialmetoder har navn som både starter og slutter med to underscores (_ tegn)
    # Denne metoden brukes for å definere hvordan objektet skal konverteres til en streng, og brukes av str() og
    # print() funksjonene.
    def __str__(self):
        return "Punkt: (" + str(self.x) + ", " + str(self.y) + ")"


# Funksjon som opererer på punktobjekter, og som demonstrerer at hvis en funksjon gjør endringer på
# et objekt, så er endringen fortsatt synlig også etter at funksjonen er ferdig.
def flytt_til_midten(punkt1, punkt2):
    midt_x = (punkt1.x + punkt2.x)/2
    midt_y = (punkt1.y + punkt2.y)/2
    punkt1.x = midt_x
    punkt1.y = midt_y


# Demonstrasjonskode, kjør denne i debug-mode for å se hva som skjer.
if __name__ == "__main__":
    punkt1 = Punkt(3, 4)                # Lager en instans (objekt) av klassen Punkt med koordinatene 3, 4. Alle
                                        # objekter er instans av en klasse.
    print(str(punkt1))                  # Skriver ut punktet. __str__ til punkt-klasen blir kalt av denne
    print(punkt1.x)                     # Henter ut x-koordinaten til punktet
    punkt1.flytt(-2, 0)                 # kaller flytt metoden på punktet
    punkt2 = Punkt(12, 23)              # Lager et punkt til. Det er nå to punkt-objekter (instanser av klassen Punkt)
    print(punkt2)                       # Skriver ut punktet. __str__ til punkt-klasen blir kalt av denne
    punkt2.flytt(1, 1)                  # Kaller flytt metoden på punktet som punkt2 variabelen refererer til
    print(punkt2)
    print(punkt1)
    flytt_til_midten(punkt1, punkt2)    # Demonstrerer flytt_til_midten funksjonen
    print(punkt1)
    punkt2.x = 3                        # Setter x-koordinatet til 3 hos punktet som punkt2 variabelen refererer til
    print(punkt2)
