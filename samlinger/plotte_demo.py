import matplotlib.pyplot as plt
import numpy as np

# Vanlig Python
# x_koordinater = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# y_koordinater = []
# for verdi in x_koordinater:
#     y_koordinater.append(verdi**2)


# List comprehension, kortere syntaks for å lage lister med enkle matematiske
# operasjoner som ikke krever numpy
x_koordinater = range(10)
y_koordinater = [x**2 for x in x_koordinater]   # for hver x i x-koordinater, lag et element som er x**2
y_2 = [x*5 for x in x_koordinater]

# numpy
# x_koordinater = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# y_koordinater = x_koordinater**2
# y_2 = x_koordinater*5

plt.plot(x_koordinater, y_koordinater)
plt.plot(x_koordinater, y_2)
plt.show()
