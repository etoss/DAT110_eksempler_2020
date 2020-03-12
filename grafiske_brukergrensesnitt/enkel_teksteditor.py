import tkinter
from tkinter import font
from tkinter import messagebox


# Eksempel på GUI objekter som snakker med hverandre: Et tekstområde og en scrollbar for dette området.
# De må koordinere for at scrollingen skal virke
class Teksteditor:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.fonten = font.Font(size=18)

        # tkinter.Text er komponenten for en lengre tekst over flere linjer. width og height er begge
        # i antall tegn. Siden denne bruker en større enn vanlig font blir hele komponenten også
        # større enn vanlig.
        self.teksten = tkinter.Text(self.hovedvindu, width=40, height=20, font=self.fonten)
        self.teksten.grid(column=0, row=0)

        # Lager en vertikal scrollbar og bruker command parameteren for å koble den til teksten
        self.tekstscroller = tkinter.Scrollbar(self.hovedvindu, orient=tkinter.VERTICAL,
                                               command=self.teksten.yview)

        # Sørger for at tekst-komponenten også vet om scrollbaren, slik at de kan snakke sammen
        # begge veier.
        self.teksten.config(yscrollcommand=self.tekstscroller.set)

        # Scrollbaren må strekkes vertikalt for å se bra ut.
        self.tekstscroller.grid(column=1, row=0, sticky=(tkinter.N, tkinter.S))

        # Lager en menylinje
        self.hovedmeny = tkinter.Menu(self.hovedvindu)
        self.hovedvindu.config(menu=self.hovedmeny)
        self.hovedvindu.option_add("*tearOff", False)

        # Lager en meny "Fil" og legger den til i hovedmenyen
        self.filmeny = tkinter.Menu(self.hovedvindu)
        self.hovedmeny.add_cascade(menu=self.filmeny, label="Fil")

        # Legger til menyvalgene åpne, lagre og lukk. command-parameteren for menyvalg fungerer på samme
        # måte som for knapper
        self.filmeny.add_command(label="Åpne", command=self.aapne_fil)
        self.filmeny.add_command(label="Lagre")
        self.filmeny.add_command(label="Lukk")

        tkinter.mainloop()

    def aapne_fil(self):
        # messagebox kan brukes for å lage enkle standarddialoger.
        messagebox.showinfo("Melding", "Du trykket på 'Åpne'")


if __name__ == "__main__":
    gui = Teksteditor()
