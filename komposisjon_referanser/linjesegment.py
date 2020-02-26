from komposisjon_referanser.punkt import *
import math

# Klassen "linjesegment" er et eksempel på komposisjon. Et linjesegment har to punkter, start og slutt
class Linjesegment:
    # start og slutt skal være Punkt objekter. Bruker type hints slik at PyCharm gir advarsler hvis
    # den brukes feil. Et type hint ser ut som <parameternavn>: <navn på type>. Så
    # start: Punkt definerer parameteren ved navn "start" og sier at jeg forventer et Punkt objekt her.
    def __init__(self, start: Punkt, slutt: Punkt):
        self.start = start
        self.slutt = slutt

    def __str__(self):
        return f"Linje, start {self.start}, slutt {self.slutt}"

    # Regner ut lengden på linja ved å spørre start- og sluttpunktene om koordinatene
    # deres og deretter regne ut lengden.
    def lengde(self):
        x_diff = self.start.x - self.slutt.x
        y_diff = self.start.y - self.slutt.y
        return math.sqrt(x_diff**2 + y_diff**2)

    # Flytter linja gjennom å flytte start- og sluttpunktet
    def flytt(self, delta_x, delta_y):
        self.start.flytt(delta_x, delta_y)
        self.slutt.flytt(delta_x, delta_y)


if __name__ == "__main__":
    punkt1 = Punkt(1, 1)
    punkt2 = Punkt(6, 5)
    linje1 = Linjesegment(punkt1, punkt2)
    print(linje1)
    punkt3 = Punkt(3, 9)
    linje2 = Linjesegment(punkt2, punkt3)
    print(linje2)
    print(linje1.lengde())
    print(linje2.lengde())

    # Flytter linje1, noe som flytter denne linja sine start- og sluttpunkter, punktene som
    # varablene punkt1 og punkt2 refererer til
    linje1.flytt(0, 2)
    print("Etter å ha flyttet linje 1 to enheter i y-retning")
    print(linje1)

    # Siden linje2 starter i samme punkt som linje1 slutter i, er også starten til linje2 flyttet siden jeg
    # flyttet linje1. Når man bygger linjer må man tenke på om dette er oppførsel man ønsker eller ikke. Hvis
    # man ikke ønsker dette, må man lage et separat punktobjekt for starten til linje2.
    print(linje2)

