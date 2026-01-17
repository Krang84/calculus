import pandas as pd
import matplotlib.pyplot as plt

population = pd.Series(
    [1650, 1750, 1860, 2070, 2300, 2560, 3040, 3710, 4450, 5280, 6080, 6870],
    index=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
)

plt.figure()
plt.plot(population.index, population.values, marker='o')
plt.xlabel("Années (depuis l'origine)")
plt.ylabel("Population (millions)")
plt.title("Évolution de la population")
plt.grid(True)
plt.tight_layout()
plt.show()
