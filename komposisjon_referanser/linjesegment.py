from komposisjon_referanser.punkt import *
import math

class Linjesegment:
    # start og slutt skal være Punkt objekter
    def __init__(self, start: Punkt, slutt: Punkt):
        self.start = start
        self.slutt = slutt

    def __str__(self):
        return f"Linje, start {self.start}, slutt {self.slutt}"

    def lengde(self):
        x_diff = self.start.x - self.slutt.x
        y_diff = self.start.y - self.slutt.y
        return math.sqrt(x_diff**2 + y_diff**2)

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
    linje1.flytt(0, 2)
    print("Etter å ha flyttet linje 1 to enheter i y-retning")
    print(linje1)
    print(linje2)

