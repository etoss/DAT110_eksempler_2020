import math

# Første eksempel på en egendefinert klasse: Punkt
#
# Denne versjonen har to egenskaper, r og theta, som ikke er lagret i instansvariabler men i stedet blir
# regnet ut fra instansvariablene. I denne versjonen er det settere for r og theta som viser hvordan du kan
# sette slike beregnete egenskaper gjennom å sette de egenskapene som punktet faktisk lagrer, x og y.
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

    # Getter for egenskapen r
    @property
    def r(self):
        return math.sqrt(self.x**2 + self.y**2)

    # Setter for egenskapen r. Denne setter variablene x og y slik at punktet for den nye r men beholder
    # theta slik den var fra før.
    @r.setter
    def r(self, ny_r):
        min_theta = self.theta
        self.x = ny_r*math.cos(min_theta)
        self.y = ny_r*math.sin(min_theta)

    # Getter for egenskapen theta
    @property
    def theta(self):
        return math.acos(self.x/self.r)

    @theta.setter
    def theta(self, ny_theta):
        min_r = self.r
        self.x = min_r*math.cos(ny_theta)
        self.y = min_r*math.sin(ny_theta)

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
    print(punkt1.r)
    print(punkt1.theta)
    punkt1.r = 18
    print(punkt1)
    punkt1.theta = math.pi*0.33
    print(punkt1)
