import matplotlib.pyplot as plt
import numpy as np
import math

# valeurs de x
x = np.linspace(0.001, 10, 100)

# équation y = 2x - 1
y = math.pi * x**2

# tracé
plt.plot(x, y)
plt.axhline(0)  # axe des x
plt.axvline(0)  # axe des y
plt.xlabel("x")
plt.ylabel("y")
plt.title("cercle")
plt.grid(True)

plt.show()
