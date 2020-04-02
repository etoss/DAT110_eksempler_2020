import tkinter
from tkinter import messagebox


# Slider og spinbox demo
class Demo:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()

        # Spinbox er en måte å velge fra ei liste av muligheter som tar mindre
        # plass enn en Listbox
        self.meny = tkinter.Spinbox(self.hovedvindu,
                                    values=("En", "To", "Tre"), command=self.haandter_spinbox)
        self.meny.pack()

        # Scale er en slider hvor man kan trekke den for å indikerer hvilken verdi man ønsker,
        # fra from_ til to. Funksjonen som settes inn i command-paramteren skal ta en
        # parameter, verdien som Scale-en ble satt til.
        self.slider = tkinter.Scale(self.hovedvindu, from_=0, to=100,
                                    orient=tkinter.HORIZONTAL, command=self.haandter_slider)

        # Aktiver-knapp for spinbox-en for å kunne lese av verdier som brukeren
        # skriver inn, hvis det er ønskelig.
        self.aktiver_knapp = tkinter.Button(self.hovedvindu, text="Aktiver", command=self.haandter_spinbox)
        self.aktiver_knapp.pack()
        self.slider.pack()
        tkinter.mainloop()

    def haandter_spinbox(self):
        innhold = self.meny.get()
        messagebox.showinfo("Spinbox aktiv", f"Innhold: {innhold}")

    def haandter_slider(self, verdi):
        print(f"Slider aktivert med verdi {verdi}")


if __name__ == "__main__":
    gui = Demo()
