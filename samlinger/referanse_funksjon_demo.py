# Demo på funksjonskall og referanser. Når du kaller en funksjon så blir det overført en kopi av referansen.
# Hvis funksjonen gjør en endring på ei liste så er denne endringen fortsatt der etter at funksjonen er
# ferdig siden den opprinnelige variabelen og parameteren til funksjonen begge refererer til samme liste.
def funksjon(v1, v2):
    v1 = v1 + v2
    print(v1)


def listetest(liste1):
    liste1[3] = 6
    print("6")


tall = 5
tall2 = 7
funksjon(tall, tall2)
print(tall)
print(tall2)
liste = [0, 1, 2, 3, 4, 5, 6]
listetest(liste)
for element in liste:
    print(element)
