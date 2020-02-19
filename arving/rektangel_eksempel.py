#Eksempel på brudd på Liskov Substitution Principle: Kvadrat som subklasse av Rektangel
class Rektangel:
    def __init__(self, start_x, start_y, bredde, hoyde):
        self.start_x = start_x
        self.start_y = start_y
        self.bredde = bredde
        self.hoyde = hoyde

    def areal(self):
        return self.bredde * self.hoyde

    # Strekker rektanglet horisintalt men slik at arealet forblir det samme
    def strekk(self, multiplikator):
        self.bredde *= multiplikator
        self.hoyde /= multiplikator

    def __str__(self):
        return f"Rektangel: fra ({self.start_x}, {self.start_y}) med bredde {self.bredde} og høyde {self.hoyde}"


# Kvadrat
class Kvadrat(Rektangel):
    def __init__(self, start_x, start_y, storrelse):
        super().__init__(start_x, start_y, storrelse, storrelse)

    # Redefinerer bredde og høyde som properties siden bdet som skiller et kvadrat
    # fra et rektangel er at bredde og høyde alltid er like.
    @property
    def bredde(self):
        return self.__bredde

    @bredde.setter
    def bredde(self, ny_bredde):
        self.__bredde = ny_bredde
        self.__hoyde = ny_bredde

    @property
    def hoyde(self):
        return self.__hoyde

    @hoyde.setter
    def hoyde(self, ny_hoyde):
        self.__bredde = ny_hoyde
        self.__hoyde = ny_hoyde


# Testekode. Bruker strekk metoden på både et rektangel og et kvadrat og viser at den ikke
# oppfører seg som forventet på kvadrater.
if __name__ == "__main__":
    rektangel = Rektangel(2, 1, 5, 4)
    print(rektangel)
    kvadrat = Kvadrat(10, 1, 6)
    print(kvadrat)
    liste = []
    liste.append(rektangel)
    liste.append(kvadrat)
    for rektangel in liste:
        rektangel.strekk(2)
    for rektangel in liste:
        print(rektangel)
