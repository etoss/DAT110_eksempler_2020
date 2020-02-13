# Dette er en kommentar
lengde_streng = input("Lengden til rommet: ")
lengde_tall = float(lengde_streng)
bredde_streng = input("Bredden til rommet: ")
bredde_tall = float(bredde_streng)
areal = lengde_tall*bredde_tall
print("Arealet er: ", end="")
print(format(areal, "10.6f"))
# Evalueres innenfra og ut. format kjører først, og
# så sendes resultatet av format til print
