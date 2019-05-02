import os
import numpy as np
import matplotlib.pyplot as plt


a = os.system("g++ DanielaBarrios_Ejercicio28.cpp -o DanielaBarrios_Ejercicio28.x")
a = os.system("./DanielaBarrios_Ejercicio28.x > DanielaBarrios_Ejercicio28.dat")

plt.figure()
data = np.loadtxt("DanielaBarrios_Ejercicio28.dat")
plt.plot(data[:,0], data[:,1])
plt.axis('square')
plt.xlim([-25, 25])
plt.ylim([-25, 25])
plt.xlabel('Indice x')
plt.ylabel('Indice T')
plt.savefig("imagen1.png")
