# Eksempel på grensesnitt fra Python rammeverket: Iterator.
#
# Objekter av en klasse som implementerer Iterator grensesnittet kan brukes i en for-løkke for å behandle alle
# elementene i den.
#
# Eksempel: En klasse som representerer en geometrisk rekke. tall_nummer_n = start*base^n
class Rekke:
    def __init__(self, start, base, antall):
        self.start = start
        self.base = base
        self.antall = antall
        self.k = 0

    # Implementerer metode fra Iterator grensesnittet. Denne skal lage og returnere en iterator over rekka.
    def __iter__(self):
        return RekkeIterator(self)


# Iterator klasse for rekke. Tar inn en referanse til rekka den skal iterere over i konstruktøren
class RekkeIterator:
    def __init__(self, rekke):
        self.rekke = rekke
        self.k = 0

    # Implementerer metode fra Iterator grensesnittet. For iteratoren skal denne alltid returnere objektet selv.
    def __iter__(self):
        return self

    # Implementerer metode fra Iterator grensesnittet. Denne skal returnere neste element, eller lage
    #   StopIteration exception når det ikke er flere elementer igjen.
    def __next__(self):
        if self.k >= self.rekke.antall:
            raise StopIteration
        verdi = self.rekke.start*(self.rekke.base**self.k)
        self.k += 1
        return verdi


# Demonstrerer bruken av rekka og iteratoren.
if __name__ == "__main__":
    rekka = Rekke(1, 0.5, 15)
    for tall in rekka:
        print(tall)
    for tall in rekka:
        print(tall)
