import unittest
from testing.bokstavkarakter import *


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


if __name__ == "__main__":
    unittest.main()
