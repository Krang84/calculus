import matplotlib.pyplot as plt
import numpy as np

# valeurs de x
x = np.linspace(-10, 10, 100)

# équation y = 2x - 1
y = 2*x - 1

# tracé
plt.plot(x, y)
plt.axhline(0)  # axe des x
plt.axvline(0)  # axe des y
plt.grid(True)

plt.show()
