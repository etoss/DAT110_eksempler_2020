class Student:
    def __init__(self, navn, studieretning, aarskurs):
        self.navn = navn
        self.studieretning = studieretning
        self.aarskurs = aarskurs

    def get_aarskurs(self):
        return self.__aarskurs

    def set_aarskurs(self, nytt_aarskurs):
        if nytt_aarskurs < 1:
            raise ValueError("Kan ikke ha årskurs under 1!")
        if nytt_aarskurs > 5:
            raise ValueError("Kan ikke ha årskurs høyere enn 5!")
        self.__aarskurs = nytt_aarskurs

    @property
    def aarskurs(self):
        return self.__aarskurs

    @aarskurs.setter
    def aarskurs(self, nytt_aarskurs):
        if nytt_aarskurs < 1:
            raise ValueError("Kan ikke ha årskurs under 1!")
        if nytt_aarskurs > 5:
            raise ValueError("Kan ikke ha årskurs høyere enn 5!")
        self.__aarskurs = nytt_aarskurs


if __name__ == "__main__":
    test = Student("Arne Andresen", "Data", 7)
    test.aarskurs = 1
    test.aarskurs = 0

