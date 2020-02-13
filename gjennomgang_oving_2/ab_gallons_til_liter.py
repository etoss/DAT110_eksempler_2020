LITER_I_EN_GALLON = 3.785411784


# Oppgave a)
def gallons_til_liter(gallons):
    liter = gallons*LITER_I_EN_GALLON
    return liter


# Oppgave b)
if __name__ == "__main__":
    gallons = float(input("Skriv inn antall gallons: "))
    liter = gallons_til_liter(gallons)
    print(f"Antall liter: {liter:6.2f}")
