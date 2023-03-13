import numpy as np

mat = np.diag(np.arange(3))
print(mat)
#selecionar um elemento
print(mat[1,1]) #linha 1, coluna 1
print(mat[1])#seleciona a primeira linha
print(mat[:,2])#todos elementos da coluna 2

arr1 = np.arange(10)
print(arr1)

#start, stop, step
print(arr1[1:9:2])

arr2 = np.array([1,2,3,4])
arr3= np.array([7,8,3,3])

#comparar item a item
print(arr2==arr3)

#comparar de forma global
print(np.array_equal(arr2,arr3))

#encontrar menor valor
print(arr3.min())

#encontrar maior valor
print(arr3.max())

#somar um valor a cada posição
print(arr3+10)

arr4 = np.array([1.2,1.5,1.7,2.6,2.9,3.4,4.9])

#arredondar valores
print(np.around(arr4))

arr5 = np.array([[1,2,3,4],[5,6,7,8]])

#matriz para array
print(arr5.flatten())

#repetir sequencia de um array
arr6 = np.arange(4)
print(arr6.repeat(3))
print(np.repeat(arr6,4))

print(np.tile(arr6, 3))

#cópia de um array
arr7 = np.copy(arr5)

print(arr7)
