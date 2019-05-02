import os
import numpy as np
import matplotlib.pyplot as plt


a = os.system("g++ DanielaBarrios_Ejercicio28.cpp -o DanielaBarrios_Ejercicio28.x")
a = os.system("./DanielaBarrios_Ejercicio28.x > DanielaBarrios_Ejercicio28.dat")

plt.figure()
data = np.loadtxt("DanielaBarrios_Ejercicio28.dat")

plt.subplot(3,3,1)
plt.plot(data[:,0], data[:,1])
plt.axis('square')
plt.xlim([-25, 25])
plt.ylim([-25, 25])
plt.xlabel('Indice x')
plt.ylabel('Indice T')
plt.savefig("imagen1.png")

plt.subplot(3,3,2)
plt.plot(data[:,0], data[:,1])
plt.axis('square')
plt.xlim([-25, 25])
plt.ylim([-25, 25])
plt.xlabel('Indice x')
plt.ylabel('Temperatura')
plt.savefig("imagen2.png")
