# Lager en tom mengde
mengde1 = set()
mengde1.add(1)      # Legger til et element
mengde1.add(2)
mengde1.add(3)
mengde1.add(4)
mengde1.add(5)
mengde1.add(6)
print(mengde1)

mengde1.add(3)      # Å legge til et element som allerede er i mengden gjør ingen ting, mengden blir ikke endret
print(mengde1)

mengde1.remove(4)   # Fjerner et element fra mengden
print(mengde1)

mengde2 = set([1, 3, 5, 7, 9, 11, 13])      # Lager en mengde fra ei liste

tall = 9
if tall in mengde2:                         # in-operatoren på mengder
    print(str(tall) + " er med i mengden")
else:
    print(str(tall) + " er med ikke i mengden")


for tall in mengde1:                        # for-loop på mengder
    print(tall)


# Mengdeoperasjoner:

# Snitt: Finn alle elementene som er med i begge mengdene:
print(mengde1.intersection(mengde2))

# Union: Finn alle elementene som er med i minst én av mengdene:
print(mengde1.union(mengde2))

# Minus: Finn alle elementene som er med i mengde1 men ikke mengde2:
print(mengde1 - mengde2)
