import unittest
from testing.bokstavkarakter import *


# Enhetstest av funksjonen "bokstavkarakter".
#
# Tester alle veier gjennom metoden, det vil si ulike tall som representerer hver
#   av de fem karakterene A til F.
#
# Tester grensetilfeller, slik at for eksempel 90 skal gi A mans 89 skal gi B.
#
# Testeklassen arver fra unittest.Testcase. assertEquals (og andre assert metoder)
# arver man derfra.
class TestBokstavkarakter(unittest.TestCase):
    def test_bokstavkarakter(self):
        self.assertEquals(karakter_fra_prosent(98), "A")
        self.assertEquals(karakter_fra_prosent(90), "A")
        self.assertEquals(karakter_fra_prosent(89), "B")
        self.assertEquals(karakter_fra_prosent(84), "B")
        self.assertEquals(karakter_fra_prosent(80), "B")
        self.assertEquals(karakter_fra_prosent(79), "C")
        self.assertEquals(karakter_fra_prosent(74), "C")
        self.assertEquals(karakter_fra_prosent(60), "C")
        self.assertEquals(karakter_fra_prosent(59), "D")
        self.assertEquals(karakter_fra_prosent(58), "D")
        self.assertEquals(karakter_fra_prosent(50), "D")
        self.assertEquals(karakter_fra_prosent(49), "E")
        self.assertEquals(karakter_fra_prosent(40), "E")
        self.assertEquals(karakter_fra_prosent(39), "F")
        self.assertEquals(karakter_fra_prosent(10), "F")


# Kjører testene.
if __name__ == "__main__":
    unittest.main()
