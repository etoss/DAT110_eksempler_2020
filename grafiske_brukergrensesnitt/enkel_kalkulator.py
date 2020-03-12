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
            # For å kunne lage lytterfunksjoner (call-backs) for de enkelte knappene, trenger man et objekt
            # som lagrer verdien av variabelen "i" i det knappen lagres.
            knapplytter = TallKnappLytter(str(i), self)

            # Knappene har ramma heller enn hovedvinduet som forelder. Command-parameteren er et kall til en funksjon
            # i objektet som lagrer verdien av variabelen i.
            self.tallknapper.append(tkinter.Button(self.knappramme, text=str(i),
                                                   command=knapplytter.sett_inn_tall))
            # Grid layout manager plasserer komponenter i et rutenett, man oppgir column og row
            # for å vise hvilken rad og kolonne. Rader og kolonner får størrelse slik at den største
            # komponenten passer inn.
            self.tallknapper[-1].grid(column=(i-1)%3, row=2 - ((i-1)//3))

        # Lambda-uttrykk: Lager en anonym funksjon til bruk som call-back / lytter.
        # syntakt: lambda <parameterliste>: <Python kommando>. I dette tilfellet forventer Button en funksjon
        # uten parametre, så parameterlista er tom. lambda-uttrykk kan ikke være mer enn en enkel Python kommando.
        self.tallknapper.append(tkinter.Button(self.knappramme, text="0",
                                               command=lambda: self.sett_inn_tall("0")))

        # Kan bruke columnspan og rowspan parameter for å si at en komponent skal dekke flere kolonner og/eller rader
        # Kan bruke sticky parameteren for å få strukket en komponent slik at den fyller hele cellen. I dette tilfellet
        # strekkes komponenten i horisontal retning (vest - øst).
        self.tallknapper[-1].grid(column=0, row=3, columnspan=2, sticky=(tkinter.W, tkinter.E))
        self.tallknapper.append(tkinter.Button(self.knappramme, text="="))
        self.tallknapper[-1].grid(column=2, row=3)
        self.knappramme.grid(column=1, row=1, padx=10, pady=10)

        self.operasjonsramme = tkinter.Frame(self.hovedvindu)
        self.pluss = tkinter.Button(self.operasjonsramme, text="+")
        self.minus = tkinter.Button(self.operasjonsramme, text="-")
        self.gange = tkinter.Button(self.operasjonsramme, text="*")
        self.dele = tkinter.Button(self.operasjonsramme, text="/")
        self.pluss.grid(column=0, row=0)
        self.minus.grid(column=0, row=1)
        self.gange.grid(column=0, row=2)
        self.dele.grid(column=0, row=3)
        self.operasjonsramme.grid(column=2, row=1)

        self.minneramme = tkinter.Frame(self.hovedvindu)
        self.clear = tkinter.Button(self.minneramme, text="C")
        self.memory = tkinter.Button(self.minneramme, text="M")
        self.clear.grid(column=0, row=0)
        self.memory.grid(column=0, row=1)
        self.minneramme.grid(column=0, row=1)

        self.tallviser = tkinter.Entry(self.hovedvindu, width=10)
        self.tallviser.grid(column=0, row=0, columnspan=3, sticky=(tkinter.W, tkinter.E))

        tkinter.mainloop()

    # Metode for å sette inn et tall på slutten av en Entry.
    def sett_inn_tall(self, tallet_streng):
        self.tallviser.insert(tkinter.END, tallet_streng)


# Klassen for objektene som lagrer tallverdien til den enkelte knappen.
class TallKnappLytter:
    def __init__(self, tall_streng, gui):
        self.tall_streng = tall_streng
        self.gui = gui

    def sett_inn_tall(self):
        self.gui.sett_inn_tall(self.tall_streng)


if __name__ == "__main__":
    gui = EnkelKalkulator()
