import tkinter


# Prinsipp for å lage animasjoner: Lag en metode som oppdaterer animasjonen, og legg inn
# denne metoden som en call-back som systemet skal kalle etter et oppgitt antall millisekunder

# Eksempel: Ei kule som flyr horisontalt over vinduet fem ganger.
class EnkelAnimasjon:
    def __init__(self):
        self.hovedvindu = tkinter.Tk()
        self.tegner = tkinter.Canvas(self.hovedvindu, width=600, height=400)
        self.tegner.pack()
        self.x_posisjon = 10
        self.antall_ganger = 0
        self.kula = self.tegner.create_oval(self.x_posisjon, 50, self.x_posisjon+40, 90, fill="red")

        # Denne metoden i hovedvinduet registrerer at den skal kalle metoden "self.flytt_kula"
        # etter 20 millisekunder. Parameterne er (tid i millisekunder, funksjon). Dette kallet
        # starter animasjonen. 20 millisekunder gir en "frame-rate" på 50 oppdateringer
        # i sekundet.
        self.hovedvindu.after(20, self.flytt_kula)

        tkinter.mainloop()

    # Metoden som gjør animasjonen
    def flytt_kula(self):
        self.x_posisjon += 10

        # Kommer kula til enden av skjermen (som er 600 brei, og kula er 40 brei.
        if self.x_posisjon >= 560:
            self.x_posisjon = 10
            self.antall_ganger += 1

        # Flytter kula gjennom å gi den nye koordinater
        self.tegner.coords(self.kula, self.x_posisjon, 50, self.x_posisjon+40, 90)

        # Legger inn en ny after for å få den til å gjøre neste oppdatering på animasjonen.
        if self.antall_ganger < 5:
            self.hovedvindu.after(20, self.flytt_kula)


if __name__ == "__main__":
    gui = EnkelAnimasjon()
