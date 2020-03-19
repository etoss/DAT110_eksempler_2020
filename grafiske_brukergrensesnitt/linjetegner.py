import tkinter
from klasser_og_objekter.punkt_enkel import Punkt


class Linjetegner:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.tegner = tkinter.Canvas(self.hovedvindu, width=600, height=500)
        self.tegner.pack()
        self.punktliste = []
        self.tegner.bind("<Button>", self.museklikk_lytter)
        tkinter.mainloop()

    def museklikk_lytter(self, musehendelse):
        self.tegner.create_oval(musehendelse.x-2, musehendelse.y-2, musehendelse.x+2, musehendelse.y+2)
        if len(self.punktliste) > 0:
            forrige_punkt = self.punktliste[-1]
            self.tegner.create_line(forrige_punkt.x, forrige_punkt.y, musehendelse.x, musehendelse.y)
        self.punktliste.append(Punkt(musehendelse.x, musehendelse.y))


if __name__ == "__main__":
    gui = Linjetegner()
