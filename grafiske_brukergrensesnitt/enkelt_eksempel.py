import tkinter
from tkinter import font

# Enkelt eksempel på et GUI

# Lager en klasse for GUI-et slik at jeg vet hvor jeg har referanser til
# de ulike komponentene. Man trenger disse referansene når man skal
# håndtere hendelser (det brukeren gjør med grensesnittet)
class EnkeltGUI:

    # Setter opp GUI-et i konstruktøren til klassen
    def __init__(self):
        # Lager selve vinduet
        self.hovedvindu = tkinter.Tk()
        self.stor_tekstfont = font.Font(size=20)

        # Lager en etikett (Label) med parameter forelder / master component samt teksten
        self.tekstviser = tkinter.Label(self.hovedvindu, text="Skriv inn tekst:", font=self.stor_tekstfont)
        self.tekstviser.pack(side=tkinter.LEFT)
        # Bruker layout-håndteren Pack for å plassere tekstviseren i forelderen (hovedvinduet i dette tilfellet)

        # Lager en Entry, hvor brukeren kan skrive inn tekst. width parameteren er antall tegn brei den skal være
        self.ekkofelt = tkinter.Entry(self.hovedvindu, width=15, font=self.stor_tekstfont)
        self.ekkofelt.pack(side=tkinter.LEFT)

        # Lager en knapp. command-parameteren forteller hvilken funksjon (i dette tilfellet metode) som skal
        # kalles når brukeren trykker på knappen. Dette er en funksjonsreferanse og skal derfor IKKE
        # ha parenteser bak seg. Fraværet av parenteser er det som skiller en funksjonsreferanse fra
        # et funksjonskall. Funksjonen skal ikke kalles nå, den skal kalles seinere, når brukeren
        # trykker på knappen.
        self.knapp = tkinter.Button(self.hovedvindu, text="Kopier",
                                    font=self.stor_tekstfont, command=self.ekko)
        self.knapp.pack(side=tkinter.LEFT)

        # Lager en StringVar variabel. Dette er en tkinter streng som kan endres, og som sier fra til
        # gui-komponenten den legges til i når den blir endret slik at grensesnittet oppdateres
        self.teksten = tkinter.StringVar()
        self.teksten.set("Ingen tekst enda")

        # Bruker strengvariabelen i etiketten for å lage en etikett hvor man kan endre innholdet underveis.
        self.ekkoetikett = tkinter.Label(self.hovedvindu, textvariable=self.teksten, font=self.stor_tekstfont)
        self.ekkoetikett.pack(side=tkinter.LEFT)

        # Setter tittel til hovedvinduet
        self.hovedvindu.title("Ekko eksempel")

        # Starter hendelsesløkka slik at GUI-et kan reagere på det brukeren gjør, gjelder også ting som
        # tkinter håndterer selv slik som at brukeren flytter eller endrer størrelsen til vinduet.
        tkinter.mainloop()

        # print-setning etter mainloop for å illustrere at denne kjøres først etter at brukeren har
        # lukket vinduet.
        print("Etter mainloop")

    # Metoden som skal kalles når brukeren trykker på knappen
    def ekko(self):
        teksten = self.ekkofelt.get()       # Henter ut teksten fra tekstfeltet
        self.teksten.set(teksten)           # Endrer strengvariabelen


# Kode for å starte GUI-et
if __name__ == "__main__":
    gui = EnkeltGUI()
