import numpy as np
import matplotlib.pyplot as plt

e = np.arange(1, 5)
p1 = np.array([896, 915, 832, 804])
p2 = np.array([180, 176, 180, 176])
p3 = np.array([394, 396, 396, 398])

fig, ax = plt.subplots()
plt.plot(e, p3, 'b-o')
ax.set_xticks([1, 2, 3, 4])
plt.title("N° de propagaciones ejemplo 3")
plt.xlabel("Estrategia")
plt.ylabel("Propagaciones")
plt.grid(True)
plt.show()
