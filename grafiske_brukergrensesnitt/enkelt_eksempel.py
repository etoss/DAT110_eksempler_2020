import tkinter

# Enkelt eksempel på et GUI

# Lager en klasse for GUI-et slik at jeg vet hvor jeg har referanser til
# de ulike komponentene. Man trenger disse referansene når man skal
# håndtere hendelser (det brukeren gjør med grensesnittet)
class EnkeltGUI:

    # Setter opp GUI-et i konstruktøren til klassen
    def __init__(self):
        # Lager selve vinduet
        self.hovedvindu = tkinter.Tk()

        # Lager en etikett (Label) med parameter forelder / master component samt teksten
        self.tekstviser = tkinter.Label(self.hovedvindu, text="Skriv inn tekst:")
        # Bruker layout-håndteren Pack for å plassere tekstviseren i forelderen (hovedvinduet i dette tilfellet)
        self.tekstviser.pack(side=tkinter.LEFT)

        # Lager en Entry, hvor brukeren kan skrive inn tekst. width parameteren er antall tegn brei den skal være
        self.ekkofelt = tkinter.Entry(self.hovedvindu, width=15)
        self.ekkofelt.pack(side=tkinter.LEFT)

        # Lager en knapp
        self.knapp = tkinter.Button(self.hovedvindu, text="Kopier")
        self.knapp.pack(side=tkinter.LEFT)
        self.ekkoetikett = tkinter.Label(self.hovedvindu, text="Ingen tekst enda")
        self.ekkoetikett.pack(side=tkinter.LEFT)

        # Setter tittel til hovedvinduet
        self.hovedvindu.title("Ekko eksempel")

        # Starter hendelsesløkka slik at GUI-et kan reagere på det brukeren gjør, gjelder også ting som
        # tkinter håndterer selv slik som at brukeren flytter eller endrer størrelsen til vinduet.
        tkinter.mainloop()

        # print-setning etter mainloop for å illustrere at denne kjøres først etter at brukeren har
        # lukket vinduet.
        print("Etter mainloop")


# Kode for å starte GUI-et
if __name__ == "__main__":
    gui = EnkeltGUI()
