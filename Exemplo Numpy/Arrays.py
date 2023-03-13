import numpy as np

#array numpy
arr1 = np.array([10,20,32,65,98,45,31,46,28])
print(arr1)

print(type(arr1))

print(arr1.shape)

print(arr1.dtype)

#indexando
print(arr1[4])

print(arr1[1:4])

print(arr1[1:4+1])

indices = [2,4,1,8]

print(arr1[indices])

#criar uma mascara para os valores
mascara = (arr1%2==0)
print(mascara)
print(arr1[mascara])

#alterar valor do array
arr1[1] = 21
print(arr1)

#arrays numpy são de tipo único
try:
    arr1[1] = "Teste"
except:
    print("Um array é de tipo único")

#funções numpy
arr2 = np.array([1,2,3,4,5])

#soma acumulada
print(arr2.cumsum())

#produto acumulado
print(arr2.cumprod())

print(np)

#criar um array com uma progressão star, stop, step
arr3 = np.arange(0,50)
print(arr3)

arr4  = np.arange(0,50,5)
print(arr4)

print(arr4.dtype)

#criar array com zeros
arr5 = np.zeros(10)
print(arr5)

#Cria matriz identidade
arr6 = np.eye(3)
print(arr6)

#cria matriz diagonal
arr7 = np.diag(np.array([1,2,3,4]))
print(arr7)

#Array booleano
arr8 = np.array([True, False, False, True])
print(arr8)

#Array de strings
arr9 = np.array(["Linguagem Python", "Linguagem R", "Linguagem Julia"])
print(arr9)

#retorna um array espaçado dado um intervalo
arr10  = np.linspace(0,10)
print(arr10)

arr11  = np.linspace(0,10, 15) #15 elementos em um intervalo entre 0 e 10
print(arr11)

#geomspace similar ao anterior mas cria números em progressão geometrica
# logspace similar aos anteriores mas com progressão logaritma