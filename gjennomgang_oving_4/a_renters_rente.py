import matplotlib.pyplot as plt


# Oppgave a deloppgave a
def verdi_laan(startverdi, rente, antall_aar):
    okningstall = 1.0 + (rente/100.0)
    verdi = startverdi*(okningstall**antall_aar)
    return verdi


if __name__ == "__main__":
    aarstall = range(20)                        # oppgave a deloppgave b
    verdier = []
    for aar in aarstall:                        # oppgave a deloppgave c
        verdi = verdi_laan(100000, 2.89, aar)
        verdier.append(verdi)
    plt.plot(aarstall, verdier)                 # Oppgave a deloppgave d
    plt.show()

