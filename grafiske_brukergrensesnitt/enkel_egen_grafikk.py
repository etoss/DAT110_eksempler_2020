import tkinter


# Demo på hvordan å tegne egen grafikk
class EnkelEgenGrafikk:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()

        # Canvas brukes for å tegne. Må oppgi bredde og høyde i piksler
        self.tegner = tkinter.Canvas(self.hovedvindu, width=800, height=600)
        self.tegner.pack()

        # Lager linje. De fire tallene er x1, y1, x2, y2, x- og y-koordinatene for
        # start- og sluttpunktet. Fill gir fargen til linja
        self.tegner.create_line(50, 300, 300, 100, width=4, dash=(20, 10), fill="green")

        # Lager rektangel. De fire tallene er x1, y1, x2, y2, som er koordinatene
        # til to diagonalt motsatte hjørner i rektanglet.
        self.tegner.create_rectangle(400, 200, 600, 400, fill="blue", outline="red")

        # Lager oval (sirkel eller ellipse). De fire tallene er x1, y1, x2, y2, som er
        # koordinatene til et rektangel som inneholder ovalen.
        self.tegner.create_oval(100, 400, 250, 500)

        # Lager en bue, en del av en oval. Parametre som oval bortsett fra start og extent,
        # som begge er vinkler i grader, samt style som sier hvordan buen skal avsluttes.
        # ALternativer ARC (uten avslutning), CHORD (linje fra slutt til start) elle
        # PIESLICE (ser ut som et kakestykke)
        self.tegner.create_arc(400, 400, 550, 500, start=-90, extent=90, style=tkinter.PIESLICE)

        # Polygon. Tallene representerer koordinater med formen x1, y1, x2, y2, x3, y3, ...
        self.tegner.create_polygon(500, 50, 540, 25, 580, 50, 580, 100, 540, 125, 500, 100, fill="red")

        # Tegner en tekst. Koordinatene er senter for teksten.
        self.tegner.create_text(75, 15, text="Tester tekst i canvas")

        tkinter.mainloop()


if __name__ == "__main__":
    gui = EnkelEgenGrafikk()
