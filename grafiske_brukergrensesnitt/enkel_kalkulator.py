import tkinter


# Et litt mer komplisert eksempel på et GUI: Enkel kalkulator
class EnkelKalkulator:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()

        # Ei ramme er en komponent som kan inneholde andre komponenter, og som brukes for å
        # organisere mer kompliserte grensesnitt
        self.knappramme = tkinter.Frame(self.hovedvindu)
        self.tallknapper = []
        for i in range(1, 10):
            # Knappene har ramma heller enn hovedvinduet som forelder
            self.tallknapper.append(tkinter.Button(self.knappramme, text=str(i)))
            # Grid layout manager plasserer komponenter i et rutenett, man oppgir column og row
            # for å vise hvilken rad og kolonne. Rader og kolonner får størrelse slik at den største
            # komponenten passer inn.
            self.tallknapper[-1].grid(column=(i-1)%3, row=2 - ((i-1)//3))
        self.tallknapper.append(tkinter.Button(self.knappramme, text="0"))
        # Kan bruke columnspan og rowspan parameter for å si at en komponent skal dekke flere kolonner og/eller rader
        # Kan bruke sticky parameteren for å få strukket en komponent slik at den fyller hele cellen. I dette tilfellet
        # strekkes komponenten i horisontal retning (vest - øst).
        self.tallknapper[-1].grid(column=0, row=3, columnspan=2, sticky=(tkinter.W, tkinter.E))
        self.tallknapper.append(tkinter.Button(self.knappramme, text="="))
        self.tallknapper[-1].grid(column=2, row=3)
        self.knappramme.grid(column=1, row=1)
        tkinter.mainloop()


if __name__ == "__main__":
    gui = EnkelKalkulator()
