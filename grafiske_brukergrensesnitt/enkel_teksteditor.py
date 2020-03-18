import tkinter
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog

FONT_TIMES = 0
FONT_ARIAL = 1
FONT_COURIER = 2

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
        self.filmeny.add_command(label="Lagre", command=self.lagre_fil)
        self.filmeny.add_command(label="Lukk", command=self.lukk)

        self.knappramme = tkinter.Frame(self.hovedvindu)
        self.knappramme.grid(column=2, row=0)

        self.bold_var = tkinter.BooleanVar()
        self.bold = tkinter.Checkbutton(self.knappramme, text="Bold", variable=self.bold_var, command=self.endre_font)
        self.bold.pack()

        self.italic_var = tkinter.BooleanVar()
        self.italic = tkinter.Checkbutton(self.knappramme, text="Italic", variable=self.italic_var, command=self.endre_font)
        self.italic.pack()

        self.font_var = tkinter.IntVar(value=FONT_TIMES)
        self.times = tkinter.Radiobutton(self.knappramme, text="Times new roman",
                                         variable=self.font_var, value=FONT_TIMES, command=self.endre_font)
        self.times.pack()
        self.arial = tkinter.Radiobutton(self.knappramme, text="Arial",
                                         variable=self.font_var, value=FONT_ARIAL, command=self.endre_font)
        self.arial.pack()
        self.courier = tkinter.Radiobutton(self.knappramme, text="Courier New",
                                           variable=self.font_var, value=FONT_COURIER, command=self.endre_font)
        self.courier.pack()

        self.fontliste = tkinter.Listbox(self.hovedvindu, selectmode=tkinter.SINGLE)
        self.fontene = font.families()
        for fonten in self.fontene:
            self.fontliste.insert(tkinter.END, fonten)
        self.fontliste.grid(column=3, row=0, sticky=(tkinter.N, tkinter.S))

        self.fontscroller = tkinter.Scrollbar(self.hovedvindu, orient=tkinter.VERTICAL,
                                               command=self.fontliste.yview)

        self.fontliste.config(yscrollcommand=self.fontscroller.set)

        # Scrollbaren må strekkes vertikalt for å se bra ut.
        self.fontscroller.grid(column=4, row=0, sticky=(tkinter.N, tkinter.S))

        self.fontliste.bind("<Double-Button-1>", lambda e: self.endre_font_listbox())
        self.fontliste.bind("<Key-Return>", lambda e: self.endre_font_listbox())

        tkinter.mainloop()

    def aapne_fil(self):
        with filedialog.askopenfile() as fila:
            teksten = fila.read()
            self.teksten.delete(0.0, tkinter.END)
            self.teksten.insert(tkinter.END, teksten)

    def lagre_fil(self):
        with filedialog.asksaveasfile() as fila:
            tekst_i_omraadet = self.teksten.get(0.0, tkinter.END)
            fila.write(tekst_i_omraadet)

    def lukk(self):
        self.hovedvindu.destroy()

    def endre_font(self):
        if self.bold_var.get():
            bold_tekst = "bold"
        else:
            bold_tekst = "normal"
        if self.italic_var.get():
            italic_tekst = "italic"
        else:
            italic_tekst = "roman"
        if self.font_var.get() == FONT_TIMES:
            font_tekst = "Times New Roman"
        if self.font_var.get() == FONT_ARIAL:
            font_tekst = "Arial"
        if self.font_var.get() == FONT_COURIER:
            font_tekst = "Courier New"
        ny_font = font.Font(size=18, weight=bold_tekst, slant=italic_tekst, family=font_tekst)
        self.teksten.config(font=ny_font)

    def endre_font_listbox(self):
        if self.bold_var.get():
            bold_tekst = "bold"
        else:
            bold_tekst = "normal"
        if self.italic_var.get():
            italic_tekst = "italic"
        else:
            italic_tekst = "roman"
        valg_index = self.fontliste.curselection()
        ny_font = font.Font(size=18, weight=bold_tekst, slant=italic_tekst, family=self.fontene[valg_index[0]])
        self.teksten.config(font=ny_font)


if __name__ == "__main__":
    gui = Teksteditor()
