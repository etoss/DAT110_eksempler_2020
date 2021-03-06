# Eksempel på bruk av properties for å teste for lovlige verdier:
# student-klasse hvor "årskurs" egenskapen må være mellom 1 og 5.
#
# Python-metoden for å lage egenskaper til objekter:
# - start med at alle egenskapene til instansene av klassen er offentlige instansvariabler
# - konverter dem til properties ved behov, typisk:
#   - Du ønsker noe som kan leses men ikke skrives
#   - Du ønsker å sjekke for lovlige verdier
#   - Du ønsker å beregne egenskapen i stedet for å lagre den direkte
#
# get_X metoder og set_X metoder er gammeldags
class Student:
    def __init__(self, navn, studieretning, aarskurs):
        self.navn = navn
        self.studieretning = studieretning
        self.aarskurs = aarskurs

    # Eksempel på gammeldags getter
    def get_aarskurs(self):
        return self.__aarskurs          # Privat instansvariabel __arskurs, privat siden den starter med __

    # Eksempel på gammeldags setter
    def set_aarskurs(self, nytt_aarskurs):
        if nytt_aarskurs < 1:
            raise ValueError("Kan ikke ha årskurs under 1!")
        if nytt_aarskurs > 5:
            raise ValueError("Kan ikke ha årskurs høyere enn 5!")
        self.__aarskurs = nytt_aarskurs

    # Eksempel på property-getter
    @property
    def aarskurs(self):
        return self.__aarskurs

    # Eksempel på property-setter
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

