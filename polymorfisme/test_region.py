import unittest
from komposisjon_referanser.geometri_eksempler import Region
from komposisjon_referanser.punkt import Punkt


# Eksempel på et Mock Object: Segmentlinje til bruk for å teste Region klassen. Den må inneholde alle egenskapene
# fra Segmentlinje som Region trenger: en lengde-metode og ei liste med punkter.
class MockSegmentlinje:
    def __init__(self):
        self.punkter = []
        self.punkter.append(Punkt(3, 4))
        self.punkter.append(Punkt(6, 4))
        self.punkter.append(Punkt(6, 8))
        self.punkter.append(Punkt(3, 8))
        self.punkter.append(Punkt(3, 4))

    def lengde(self):
        return 5.0


# Enhetstester som bruker Mock Objekt
class TestRegion(unittest.TestCase):
    def test_omkrets(self):
        linja = MockSegmentlinje()
        region = Region(linja)
        self.assertAlmostEqual(region.omkrets(), 5.0, 5)

    def test_areal(self):
        linja = MockSegmentlinje()
        region = Region(linja)
        self.assertAlmostEqual(region.areal(), 12.0, 5)


if __name__ == "__main__":
    unittest.main()
