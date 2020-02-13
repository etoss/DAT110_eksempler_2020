import math

# Kan bruke strenger som lister
streng = "Dette er en streng."
print(len(streng))
print(streng[3])
print(streng[0])
print(streng[2:10])

# Splitting av strenger: Splitetr basert på whitespace
ordliste = streng.split()

# Fjerner whitespace fra endene av strengen
# bruk lstrip() og rstrip() for å fjerne fra bare én ende
print(streng.strip())
print(streng.strip(".,:;"))        # Fjerner punktum, komma, kolon og semikolon fra endene av strengen

smaa_bokstaver = streng.lower()     # Konverterer til bare små bokstaver
print(smaa_bokstaver)

# Formatering av strenger
tall = 1.2
tall -= 1.0
print(tall)
0.19999999999999996
pris = 129
formatert_streng = "Total pris: %d" % pris
print(formatert_streng)

formatert_streng = "Total pris: %6d" % pris             # %-formatering, eldste type
formatert_streng = "Total pris: " + format(pris, "6d")  # format-funksjonen, fra tidlig i Pythons historie
formatert_streng = f"Total pris: {pris}"                # f-streng, fra og med Python 3.6

formatert_streng = "Testetallet: %8.5f" % tall
formatert_streng = "Testetallet: " + format(tall, "8.5f")
formatert_streng = f"Testetallet: {tall:8.5f}"

lengde = 4.0
bredde = 3.0
vinkel = math.pi/2.0
areal = 0.5*lengde*bredde*math.sin(vinkel)
formatert_streng = "Arealet til en trekant med lengde %7.2f og bredde %7.2f og vinkel %6.2f er %8.2f" % (lengde, bredde, vinkel, areal)
formatert_streng = "Arealet til en trekant med lengde %5.2f og bredde %5.2f og vinkel %5.2f er %6.2f" % (lengde, bredde, vinkel, areal)
formatert_streng = f"Arealet til trekant lengde {lengde:5.2f}, bredde {bredde:5.2f} og vinkel {vinkel:5.2f} er: {areal:6.2f}"
