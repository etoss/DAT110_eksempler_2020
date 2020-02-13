import numpy as np


array = np.arange(7)        # numpy array av heltall, tallene fra og med 0, til men ikke med 7
print(array)
array2 = np.zeros(6)        # numpy array av flyttall, 6 elementer som alle er 0.0
array2[2] = 14.7
print(array2[2])
print(array2[-2])
array = array * 5           # Matematiske operasjoner på numpy arrays gjøres på alle elementene
print(array)
array3 = np.array([2, 3, 2, 3, 2, 3, 2])    # Lager en array fra ei Python liste
print(array3)
array = array * array3                      # Siden operasjonen gjøres element for element må de to array-ene være like lange
print(array)
matrise1 = np.array([[1, 2, 3], [4, 5, 6]])     # Lager en 3x2 matrise fra ei liste av lister
print(matrise1)
matrise2 = np.array([[4, 3], [5, 4], [6, 5]])   # Lager en 2x3 matrise
matrise3 = matrise1 @ matrise2                  # @ operatoren gir matrisemultiplikasjon (* operatoren gjør element-for-element multiplikasjon)
print(matrise2)
print(matrise3)
matrise4 = matrise2 @ matrise1
print(matrise4)

print("\n Eksempler fra timen 29. januar: ")
matrise1 = np.zeros((3, 4))         # Lager en matrise med 3 rader og 4 kolonner, fylt med nuller
matrise1[1, 2] = 5.0                # Setter elementet på rad 1 og kolonne 2 lik 5.0
variabel = matrise1[2, 3]           # Henter ut elementet på ran 2 og kolonne 3
liste = [1, 2, 3, 4]
liste2 = [5, 6, 7, 8]
liste3 = [9, 10, 11, 12]
liste_lister = []
liste_lister.append(liste)
liste_lister.append(liste2)
liste_lister.append(liste3)
matrise2 = np.array(liste_lister)   # Lager en matrise fra ei liste av lister
print(matrise2)
print(matrise2[0:2, 0:2])           # Bruk list slicing for å hente ut en delmatrise,
                                    # i dette tilfellet radene fra og med 0 til men
                                    # ikke med 2, og kolonnene fra og med 0, til men
                                    # ikke med 2.
print(matrise2[:, 2:4])             # Alle radene, kolonne 2-4
print(matrise2[:, 1])               # 1-dimensjonal array, alle radene, kolonne 1
print(matrise2[1, :])               # 1-dimensjonal array, alle kolonnene, rad 1
