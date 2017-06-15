"""
Codigo para generar los graficos del ejercicio 2
"""

import numpy as np
import matplotlib.pyplot as plt

# Valor de N
N = np.arange(1, 15)

# Numero de soluciones
sol = np.array([1	, 0,	 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596])

# Tiempos
ta = np.array([1.63e-4, 1.84e-4, 1.67e-4, 2.3e-4, 3.28e-4, 3.58e-4, 9.62e-4,
               2.313e-3, 9.159e-3, 2.8563e-2, 2.14e-2, 1.325, 7.445, 39.545])
tb = np.array([1.66e-4, 1.43e-4, 1.7e-4, 1.98e-4, 3.5e-4, 3.87e-4, 8.14e-4, 
               3.214e-3, 1.2868e-2, 2.8423e-2, 0.222, 1.319, 7.426, 39.857])
tc = np.array([2.24e-4, 1.67e-4, 1.57e-4, 2.49e-4, 5.3e-4, 6.33e-4,
               2.447e-3, 1.2612e-2, 7.3701e-2, 0.433, 2.578, 20.815, 164, 1472])
td = np.array([1.47e-4, 1.61e-4, 1.69e-4, 2.3e-4, 5.49e-4, 6.29e-4, 2.639e-2,
               0.011, 0.067, 0.401, 2.784, 21.385, 161, 1.43e3])

# Propagaciones
pa = np.array([0, 6, 13, 29, 102, 271, 839, 3034, 11827, 45027, 195128, 
               931501, 4761432, 25951470])
pb = np.array([0, 6, 13, 31, 100, 278, 848, 3092, 11903, 45115, 195510, 
               932526, 4767222, 25976821])
pc = np.array([0, 6, 19, 61, 266, 1048, 4868, 25401, 144712, 898123, 
               6065992, 44350624, 345100207, 25951470])
pd = np.array([0, 6, 16, 58, 253, 1019, 4760, 24875, 141160, 872785,
               5876335, 42869947, 332938520, 2870917241])

# Grafico soluciones
#plt.semilogy(N, sol, "*b")
#plt.title("N° de soluciones vs N")
#plt.ylabel("N° sol")
#plt.xlabel("N")
#plt.grid(True)
#plt.show()

# Grafico tiempos
#plt.semilogy(N, ta, "*-b", label="Estrategia 1")
#plt.semilogy(N, tb, "ro", label="Estrategia 2")
#plt.semilogy(N, tc, "gx", label="Estrategia 3")
#plt.semilogy(N, td, "kd", label="Estrategia 4")
#plt.title("Tiempo vs N")
#plt.ylabel("t [s]")
#plt.xlabel("N")
#plt.grid(True)
#plt.legend()
#plt.show()

# Grafico numero de propagaciones
plt.semilogy(N, pa, "*b", label="Estrategia 1")
plt.semilogy(N, pb, "ro", label="Estrategia 2")
plt.semilogy(N, pc, "gx", label="Estrategia 3")
plt.semilogy(N, pd, "kd", label="Estrategia 4")
plt.title("Propagaciones vs N")
plt.ylabel("N° de Propagaciones")
plt.xlabel("N")
plt.grid(True)
plt.legend()
plt.show()