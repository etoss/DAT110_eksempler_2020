import tkinter
from tkinter import messagebox


# Eksempel på en egendefinert dialog
class Tekstdialog:
    def __init__(self, sporsmaal, forelder):
        # Lager dialogvinduet
        self.vindu = tkinter.Toplevel(forelder)

        # Lager komponentene i dialogvinduet
        self.sporsmaal_label = tkinter.Label(self.vindu, text=sporsmaal)
        self.sporsmaal_label.pack(side=tkinter.LEFT)
        self.tekstfelt = tkinter.Entry(self.vindu, width=20)
        self.tekstfelt.pack(side=tkinter.LEFT)
        self.ok_knapp = tkinter.Button(self.vindu, text="OK", command=self.ok_funksjon)
        self.ok_knapp.pack(side=tkinter.LEFT)
        self.cancel_knapp = tkinter.Button(self.vindu, text="Cancel", command=self.cancel_funksjon)
        self.cancel_knapp.pack(side=tkinter.LEFT)

        # Lager en variabel som skal inneholde resultatet når det er klart
        self.resultat = None

    # OK-knappen setter resultatet og lukker dialogen
    def ok_funksjon(self):
        self.resultat = self.tekstfelt.get()
        self.vindu.destroy()

    # Cancel knappen lukker dialogen men lar resultatet forbli None
    def cancel_funksjon(self):
        self.vindu.destroy()


# Funksjon som viser dialogen, med tilsvarende syntaks som messagebox-dialogene
def vis_tekstdialog(sporsmaal, forelder=None):
    dialogen = Tekstdialog(sporsmaal, forelder)

    # Venter på at vinduet blir lukket. Denne metoden fortsetter ikke før
    # vinduet er lukket
    dialogen.vindu.wait_window()

    # Vet her at vinduet er lukket og at resultat-variabelen er satt hvis brukeren
    # trykte OK.
    return dialogen.resultat


# Enkelt demo-GUI som viser bruken av den egendefinerte dialogen
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
