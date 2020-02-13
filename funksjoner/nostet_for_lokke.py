# Definisjon av en funksjon:
# def funksjonsnavn(parameterliste): blokk
# Denne definisjonen har default verdier for alle tre parametre
def skriv_ut_firkant(hoyde=3, bredde=3, tegn="*"):
    for y in range(hoyde):
        for x in range(bredde):
            print(tegn, end="")
        print()


# Siden funksjonen har default verdier for alle parametrene, kan man
# kalle den uten parametre. MErk at det fortsatt er parenteser etter.
# Slik skiller Python funksjoner fra variabler.
skriv_ut_firkant()

# Kaller funksjonen med parametre oppgitt basert på navn
skriv_ut_firkant(tegn="-", bredde=5)
hoyde = int(input("Høyde: "))
bredde = int(input("Bredde: "))

# Kaller funksjonen med parametre oppgitt basert på rekkefølge
skriv_ut_firkant(hoyde, bredde, "#")
