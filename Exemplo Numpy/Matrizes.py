import numpy as np

#criar matriz
arr1 = np.array([[1,2,3],[4,5,6]])
print(arr1)

print(type(arr1))
print(arr1.shape)

#criar uma lista de 2 x 3 com valores 1
arr2 = np.ones((2,3))
print(arr2)

#criar matriz a partir de listas de listas
lista = [[13,98,14],[34,56,12],[93,71,25]]
arr3 = np.matrix(lista)
print(arr3)
print(type(arr3))
print(arr3.size)
print(arr3.dtype)

#indexação de arrays
print(arr3[1,2]) #linha 1 coluna 2
print(arr3[:,2]) #Todas linhas coluna 2
print(arr3[0:2,2]) #linhas 0 e 1 e coluna 2
print(arr3[1,]) #todas as colunas da linha 1

#alterar elemento
arr3[2,0] = 100
print(arr3)

#Forçar tipo de dado em um array
arr4 = np.matrix([[1,2,3],[4,5,6],[7,8,9]], dtype= np.float64)
print(arr4)
print(arr4.dtype)

#tamanho em bytes de cada elemnto do array
print(arr4.itemsize)

#soma do tamanho em bytes de cada elemnto do array
print(arr4.nbytes)

#numero de dimensões do array
print(arr4.ndim)