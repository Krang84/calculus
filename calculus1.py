import matplotlib.pyplot as plt
import numpy as np

# valeurs de x
x = np.linspace(0, 120, 100)

y = (1.43653* 10**9) * (1.01395 ** x)

# tracé
plt.plot(x, y)
plt.axhline(0)  # axe des x
plt.axvline(0)  # axe des y
plt.grid(True)

plt.show()
