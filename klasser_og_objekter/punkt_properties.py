import math

# Første eksempel på en egendefinert klasse: Punkt
#
# Denne versjonen bruker properties for å sørge for at koordinatene ikke kan være negative. En property kan
# brukes som om den var en instansvariabel (variabel definert i __init__)
class Punkt:
    # Konstruktør, denne skal lage objektet. self er objektet som blir
    # lagd. De andre parameterne er som for en funksjon
    def __init__(self, start_x=0, start_y=0):
        self.x = start_x
        self.y = start_y

    # Getter for egenskapen x. En getter er en metode som henter ut verdien til en egenskap
    @property
    def x(self):
        return self.__x

    # Setter for egenskapen x. Denne sjekker at x ikke kan være negativ . En setter er en metode som setter verdien
    # til en egenskap.
    @x.setter
    def x(self, ny_x):
        if ny_x > 0.0:
            self.__x = ny_x

    # Getter for egenskapen y
    @property
    def y(self):
        return self.__y

    # Setter for egenskapen y
    @y.setter
    def y(self, ny_y):
        if ny_y > 0.0:
            self.__y = ny_y

    # Metode for klassen Punkt.
    def flytt(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def __str__(self):
        return "Punkt: (" + str(self.x) + ", " + str(self.y) + ")"


def flytt_til_midten(punkt1, punkt2):
    midt_x = (punkt1.x + punkt2.x)/2
    midt_y = (punkt1.y + punkt2.y)/2
    punkt1.x = midt_x
    punkt1.y = midt_y


if __name__ == "__main__":
    punkt1 = Punkt(3, 4)
    print(str(punkt1))
    print(punkt1.x)
    punkt1.flytt(-2, 0)
    punkt2 = Punkt(12, 23)
    print(punkt2)
    punkt2.flytt(1, 1)
    print(punkt2)
    print(punkt1)
    flytt_til_midten(punkt1, punkt2)
    print(punkt1)
    punkt2.x = 3
    print(punkt2)
    punkt2.x = -3
    print(punkt2)


