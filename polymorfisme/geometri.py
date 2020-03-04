# Eksempel på klasse som støtter Flyttbar grensesnittet
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
