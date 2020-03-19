import tkinter
from tkinter import messagebox


# Start på slider og spinbox demo
class Demo:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.meny = tkinter.Spinbox(self.hovedvindu,
                                    values=("En", "To", "Tre"), command=self.haandter_spinbox)
        self.meny.pack()
        self.slider = tkinter.Scale(self.hovedvindu, from_=0, to=100,
                                    orient=tkinter.HORIZONTAL, command=self.haandter_slider)

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
