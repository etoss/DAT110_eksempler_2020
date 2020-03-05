import math

from komposisjon_referanser.geometri_eksempler import avstand
from komposisjon_referanser.punkt import Punkt

# Grensesnitt: Område
#   areal() -> float
#   omkrets() -> float
#   overlapper(overlapper_med: område) -> boolean

# Eksempel på klasse som støtter Flyttbar og Område grensesnittene
class Sirkel:
    def __init__(self, senter_x, senter_y, radius):
        self.senter_x = senter_x
        self.senter_y = senter_y
        self.radius = radius

    def __str__(self):
        return f"Sirkel med senter ({self.senter_x}, {self.senter_y}) og radius {self.radius}"

    # Implementerer "flyttbar" grensesnittet
    def flytt(self, delta_x, delta_y):
        self.senter_x += delta_x
        self.senter_y += delta_y

    # Implementerer "område" grensesnittet
    def areal(self):
        return math.pi*self.radius*self.radius

    # Implementerer "område" grensesnittet
    def omkrets(self):
        return 2.0*math.pi*self.radius


# Eksempel på klasse som støtter Flyttbar og Område grensesnittene
class Kvadrat:
    def __init__(self, start_x, start_y, storrelse):
        self.start_x = start_x
        self.start_y = start_y
        self.storrelse = storrelse

    # Implementerer "flyttbar" grensesnittet
    def flytt(self, delta_x, delta_y):
        self.start_x += delta_x
        self.start_y += delta_y

    # Implementerer "område" grensesnittet
    def areal(self):
        return self.storrelse*self.storrelse

    # Implementerer "område" grensesnittet
    def omkrets(self):
        return self.storrelse*4.0


# Eksempel på klasse som har metoder fra område og flyttbar grensesnittene, men med feil signatur
class Punkt3D:
    def __init__(self, start_x, start_y, start_z):
        self.x = start_x
        self.y = start_y
        self.z = start_z

    # Flytt metode med en parameter for mye
    def flytt(self, delta_x, delta_y, delta_z):
        self.x += delta_x
        self.y += delta_y
        self.z += delta_z

    # Areal metode med feil returverdi. Siden den ikke har en return-setning, returnerer den None.
    def areal(self):
        print("Areal til et 3D punkt fins ikke")


# Eksempel på grensesnitt lagd basert på en eksisterende klasse: Linje

# Grensesnitt: Linje
#   egenskap: start: Punkt
#   egenskap: slutt: Punkt
#   lengde() -> float
#   flytt(delta_x: float, delta_y: float) -> None
class Linjesegment:
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


# Versjon av Segmentlinje som implementerer Linje grensesnittet
class Segmentlinje:
    def __init__(self, punktliste=None):
        if punktliste is None:
            self.punkter = []
        else:
            self.punkter = punktliste[:]        # list slicing gir en grunn kopi av lista

    # Lager egenskapene start og slutt som properties som leser ut start og slutt fra punktlista
    @property
    def start(self):
        return self.punkter[0]

    @property
    def slutt(self):
        return self.punkter[-1]

    def legg_til_punkt(self, punktet: Punkt):
        self.punkter.append(punktet)

    def slett_punkt(self, punktet: Punkt):
        self.punkter.remove(punktet)

    # Implementerer lengde() metoden fra Linje grensesnittet
    def lengde(self):
        total_avstand = 0       # Akkumulator
        for i in range(1, len(self.punkter)):
            total_avstand += avstand(self.punkter[i-1], self.punkter[i])
        return total_avstand

    # Implementerer flytt() metoden fra Linje grensesnittet
    def flytt(self, delta_x, delta_y):
        for punkt in self.punkter:
            punkt.flytt(delta_x, delta_y)

    # For å få ut en strengrepresentasjon, spør den indre lista om elementene sine og spør deretter
    # elementene om koordinatpar-strengen deres.
    def __str__(self):
        resultat = "Segmentlinje: "
        for punkt in self.punkter:
            resultat += punkt.koordinatpar_streng() + ", "
        return resultat
