telefonkatalog = {}                             # Lager et tomt dictionary
telefonkatalog["Jan Johansen"] = 12345678       # Setter inn nøkkel "Jan Johansen" og tilhørende verdi 12345678
telefonkatalog["Berit Nilsen"] = 23456789
telefonkatalog["David Ås"] = 98765432
telefonkatalog["Jan Johansen"] = 13579753       # Overskriver verdien for "Jan Johansen"

# Generell syntaks dictionary[nøkkel] = verdi

# Måte å leite i en mengde uten å få exception ved skrivefeil
nokkel_sok = input("Navn på person: ")
if nokkel_sok in telefonkatalog:
    print(telefonkatalog[nokkel_sok])
else:
    print("Personen du leiter etter er ikke med")

# Syntaks for sok: verdi = dictionary[nøkkel]


# En for-loop på dictionaries går gjennom alle nøklene
for verdi in telefonkatalog:
    print(verdi)

# For å få ut verdiene, hent dem ut for hver iterasjon
for nokkel in telefonkatalog:
    print(str(nokkel) + ": " + str(telefonkatalog[nokkel]))

# Dictionary kontrollerer ikke typer, men tillater ikke lister som nøkler. Tupler går fint:
telefonkatalog[(5, 6)] = 34525325

# Sletter en verdi fra et dictionary
del telefonkatalog[(5, 6)]

# Dictionary konstant, nøkkel: verdi par skilt med komma
dict2 = {"test": 5, "t2": 9}
