import unittest
from testing.fakultet import *


class FakultetTest(unittest.TestCase):
    def test_fakultet(self):
        self.assertEquals(fakultet(0), 1)
        self.assertEquals(fakultet(1), 1)
        self.assertEquals(fakultet(2), 2)
        self.assertEquals(fakultet(3), 6)
        self.assertEquals(fakultet(5), 120)
        self.assertEquals(fakultet(8), 40320)

    # Bruk assertAlmostEqual for flyttall siden flyttallsmatematikk av og til er litt upresis på grunn av
    # avrundingsfeil.
    def test_volum_rom(self):
        self.assertEquals(volum_rom(2, 3, 4), 24)
        self.assertAlmostEquals(volum_rom(2.5, 3.4, 4.3), 36.55, places=6)


if __name__ == "__main__":
    unittest.main()
