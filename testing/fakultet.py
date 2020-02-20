def fakultet(tall):
    resultat = 1
    for i in range(1, tall+1):
        resultat *= i
    return resultat


def volum_rom(lengde, bredde, hoyde):
    return lengde*bredde*hoyde
