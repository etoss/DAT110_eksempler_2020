import unittest
from testing.student_eksempel import *


# Tester en enkel klasse
class TestStudent(unittest.TestCase):

    # Tester egenskapen "navn"
    def test_navn(self):
        studenten = Student("Arne Arnesen", "Data", 2)
        self.assertEquals(studenten.navn, "Arne Arnesen")
        student2 = Student("Ida Iversen", "Data", 1)
        self.assertEquals(student2.navn, "Ida Iversen")
        studenten.navn = "Arne Andre Arnesen"
        self.assertEquals(studenten.navn, "Arne Andre Arnesen")
        self.assertEquals(student2.navn, "Ida Iversen")


    def test_studieretning(self):
        studenten = Student("Arne Arnesen", "Data", 2)
        self.assertEquals(studenten.studieretning, "Data")
        student2 = Student("Ida Iversen", "Elektro", 1)
        self.assertEquals(student2.studieretning, "Elektro")
        studenten.studieretning = "Maskin"
        self.assertEquals(studenten.studieretning, "Maskin")
        self.assertEquals(student2.studieretning, "Elektro")


    # Tester egenskapen "aarskurs", inkludert testing av exceptions.
    def test_aarskurs(self):
        studenten = Student("Arne Arnesen", "Data", 2)
        self.assertEquals(studenten.aarskurs, 2)
        studenten.aarskurs = 4
        self.assertEquals(studenten.aarskurs, 4)
        with self.assertRaises(ValueError):     # Test feiler hvis det *ikke* blir en ValueError her.
            studenten.aarskurs = 6
        with self.assertRaises(ValueError):
            studenten.aarskurs = 0


if __name__ == "__main__":
    unittest.main()
