import math

class Punkt:
    def __init__(self, start_x=0, start_y=0):
        self.x = start_x
        self.y = start_y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, ny_x):
        if ny_x > 0.0:
            self.__x = ny_x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, ny_y):
        if ny_y > 0.0:
            self.__y = ny_y

    @property
    def r(self):
        return math.sqrt(self.x**2 + self.y**2)

    @r.setter
    def r(self, ny_r):
        min_theta = self.theta
        self.x = ny_r*math.cos(min_theta)
        self.y = ny_r*math.sin(min_theta)

    @property
    def theta(self):
        return math.acos(self.x/self.r)

    @theta.setter
    def theta(self, ny_theta):
        min_r = self.r
        self.x = min_r*math.cos(ny_theta)
        self.y = min_r*math.sin(ny_theta)

    def flytt(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def __str__(self):
        return "Punkt: " + self.koordinatpar_streng()

    # Overstyrer likhets-operatoren for punkter. To punkter er like hvis koordinatene er like.
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    # Lager en egen metode som returnerer strenger "(x, y)", siden den kan være nyttig andre steder som trenger
    # en kortere strengrepresentasjon enn __str__ gir.
    def koordinatpar_streng(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


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
