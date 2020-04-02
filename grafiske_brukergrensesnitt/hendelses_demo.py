import tkinter
from tkinter import messagebox


# Demo på bind-kommandoen for å håndtere hendelser: Et canvas som
# skifter farge avhengig av om muspekeren er inni eller utenfor, samt
# håndtering av museklikk og tastetrykk for å illustrere hvordan å hente
# informasjon ut av hendelsesobjektene
class HendelsesDemo:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.tegner = tkinter.Canvas(self.hovedvindu, width=600, height=500)

        # create-metodene til et Canvas returnerer en verdi, som man kan
        # bruke til å modifisere en figur seinere om man ønsker det. Her lagres
        # denne verdien i variabelen self.rektanglet
        self.rektanglet = self.tegner.create_rectangle(0,0,600,500, fill="blue")
        self.tegner.pack()

        self.tegner.bind("<Enter>", self.mus_inni)      # <Enter>: Muspekeren går inn i komponenten
        self.tegner.bind("<Leave>", self.mus_utenfor)   # <Leave>: Muspekeren forlater komponenten
        self.tegner.bind("<Button>", self.museklikk)    # <Button>: Brukeren klikker på en musknapp inne i komponenten
        self.hovedvindu.bind("<Key>", self.tastetrykk)  # <Key>: Brukeren trykker på en tast på tastaturet.

        tkinter.mainloop()

    def mus_inni(self, event):
        self.tegner.itemconfig(self.rektanglet, fill="green")

    def mus_utenfor(self, event):
        self.tegner.itemconfig(self.rektanglet, fill="blue")

    def museklikk(self, mus_hendelse):
        hvilken_knapp = mus_hendelse.num
        x_koordinat = mus_hendelse.x
        y_koordinat = mus_hendelse.y
        messagebox.showinfo("Museklikk", f"Du trykket på knapp {hvilken_knapp} på "
                                         f"koordinatene ({x_koordinat}, {y_koordinat})")

    def tastetrykk(self, tastehendelse):
        tegn = tastehendelse.char
        tastesymbol = tastehendelse.keysym
        tastekode = tastehendelse.keycode
        messagebox.showinfo("Tastetrykk", f"Tegn {tegn}. Tastesymbol {tastesymbol}. "
                                          f"Tastekode {tastekode}.")


if __name__ == "__main__":
    gui = HendelsesDemo()
