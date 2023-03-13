import numpy as np

arr1 = np.array([10,20,32,65,98])

#media
print(np.mean(arr1))

#desvio padrao  - o quanto os valores estão afastados da média
print(np.std(arr1))

#variancia
print(np.var(arr1))

arr2 = np.arange(1, 10)
print(arr2)
#soma dos elementos
print(np.sum(arr2))

#produto dos elementos
print(np.prod(arr2))

#soma acumulada
print(np.cumsum(arr2))

#produto acumulado
print(np.cumprod(arr2))

arr3 = np.array([3,2,1])
arr4 = np.array([1,2,3])

#somar dois arrays
arr5 = np.add(arr3, arr4)
print(arr5)

#multiplicar matrizes - número colunas 1 matriz deve ser igual ao numero de colunas da 2 matriz
arr6 = np.array([[1,2],[3,4]])
arr7 = np.array([[5,6],[7,8]])

arr8 = np.dot(arr6,arr7)
print(arr8)

arr9 = arr6 @ arr7
print(arr9)