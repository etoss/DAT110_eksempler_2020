import math

def areal_trekant(lengde, bredde, vinkel_grader):
    vinkel_radianer = math.radians(vinkel_grader)
    areal = 0.5*lengde*bredde*math.sin(vinkel_radianer)
    return areal        # Ny kodelinje


print("Areal av trekant")
lengde = input("Lengde: ")
lengde = float(lengde)
bredde = input("Bredde: ")
bredde = float(bredde)
vinkel_grader = input("Vinkel i grader: ")
vinkel_grader = float(vinkel_grader)
areal = areal_trekant(lengde, bredde, vinkel_grader) # Endret kodelinje
print("Arealet er: ")
print(str(areal))
