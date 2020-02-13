# While demo

# Skriv inn flere linjer tekst, hvor brukeren avslutter med å skrive
# ei tom linje
print("Skriv inn en tekst. Avslutt med tom linje.")
linja = input("> ")
resultat = linja + "\n"
while linja != "":
    linja = input("> ")
    if linja == "":
        break
    resultat += linja + "\n"     #    resultat = resultat + linja + "\n"
print(resultat)
print("Linja etter")
