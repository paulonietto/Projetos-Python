import numpy as np
import matplotlib.pyplot as plt

with open("dataset.csv") as arquivo:
    arr1 = np.loadtxt(arquivo,delimiter=',', usecols = (0,1,2,3), skiprows= 1)
    arquivo.seek(0,0)
    arr2, arr3 = np.loadtxt(arquivo,delimiter=',', usecols = (0,1), skiprows= 1, unpack=True)
print(arr1)
print(arr2)
print(arr3)

plt.plot(arr2, arr3, 'o', markersize = 6, color = 'red')
plt.show()