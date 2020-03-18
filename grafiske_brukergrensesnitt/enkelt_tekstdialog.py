import tkinter
from tkinter import messagebox


class Tekstdialog:
    def __init__(self, sporsmaal, forelder):
        self.vindu = tkinter.Toplevel(forelder)
        self.sporsmaal_label = tkinter.Label(self.vindu, text=sporsmaal)
        self.sporsmaal_label.pack(side=tkinter.LEFT)
        self.tekstfelt = tkinter.Entry(self.vindu, width=20)
        self.tekstfelt.pack(side=tkinter.LEFT)
        self.ok_knapp = tkinter.Button(self.vindu, text="OK", command=self.ok_funksjon)
        self.ok_knapp.pack(side=tkinter.LEFT)
        self.cancel_knapp = tkinter.Button(self.vindu, text="Cancel", command=self.cancel_funksjon)
        self.cancel_knapp.pack(side=tkinter.LEFT)
        self.resultat = None

    def ok_funksjon(self):
        self.resultat = self.tekstfelt.get()
        self.vindu.destroy()

    def cancel_funksjon(self):
        self.vindu.destroy()


def vis_tekstdialog(sporsmaal, forelder=None):
    dialogen = Tekstdialog(sporsmaal, forelder)
    dialogen.vindu.wait_window()
    return dialogen.resultat


class DemoGUI:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.viseknapp = tkinter.Button(self.hovedvindu, text="Vis dialog", command=self.viseknapp_funksjon)
        self.viseknapp.pack()
        tkinter.mainloop()

    def viseknapp_funksjon(self):
        teksten = vis_tekstdialog("Skriv inn tekst")
        messagebox.showinfo("Resultat", f"Du skreiv: {teksten}")


if __name__ == "__main__":
    gui = DemoGUI()
