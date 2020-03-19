import tkinter
from tkinter import messagebox


class HendelsesDemo:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.tegner = tkinter.Canvas(self.hovedvindu, width=600, height=500)
        self.rektanglet = self.tegner.create_rectangle(0,0,600,500, fill="blue")
        self.tegner.pack()

        self.tegner.bind("<Enter>", self.mus_inni)
        self.tegner.bind("<Leave>", self.mus_utenfor)
        self.tegner.bind("<Button>", self.museklikk)
        self.hovedvindu.bind("<Key>", self.tastetrykk)

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
        messagebox.showinfo("Tastetrykk", f"Tegn {tegn}. Tastesymbol {tastesymbol}. Tastekode {tastekode}.")


if __name__ == "__main__":
    gui = HendelsesDemo()
