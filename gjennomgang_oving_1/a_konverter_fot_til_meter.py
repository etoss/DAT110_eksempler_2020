# Lager en konstant for forholdet mellom meter og fot
METER_PR_FOT = 0.3048

print("Konverterer fra amerikanske for til meter")
fot_streng = input("Skriv inn antall fot: ")
fot_flyttall = float(fot_streng)
meter_flyttall = fot_flyttall*METER_PR_FOT
print("Det blir " + format(meter_flyttall, "10.4f") + " meter")
