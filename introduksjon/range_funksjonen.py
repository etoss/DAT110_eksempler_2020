#For demo

# Skriver ut tallene i lista
# Range med en parameter: range(til) gir rekka 0, 1, 2, ..., til-1
for tall in range(7):
    if tall == 3:
        continue
    print(str(tall))

tall = int(input("Tallet jeg skal ta fakultet av: "))
# Vanlig måte å teste brukerinput for feil og gi bruker
# sjansen til å prøve på nytt hvis input er feil
while tall < 0:
    print("Kan ikke ta fakultet av negative tall.")
    tall = int(input("Tallet jeg skal ta fakultet av: "))
else:
    resultat = 1
# Range med to parametre: range(fra, til) gir rekka fra, fra+1, fra+2, ..., til-1
    for i in range(1, tall+1):
        resultat = resultat * i
    print(resultat)

# Range med tre parametre: range(fra, til, steg)
print("range 1, 10, 2")
for i in range(1, 10, 2):
    print(i)
print("range 10, 1, -1")
for i in range(10, 1, -1):
    print(i)
