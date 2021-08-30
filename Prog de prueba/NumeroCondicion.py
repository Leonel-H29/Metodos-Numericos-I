import numpy as np
import matplotlib.pyplot as plt
from math import pi, fabs , sqrt, log
import random
from sympy import *

#Funcion bool que me indica si la matriz es identidad
def esMatrizIdentidad(matriz):
	Resultado = True
	for i in range(0,matriz.shape[0]):
		for j in range(0,matriz.shape[0]):
			##Reviso si los elementos de la diagonal principal son distintos de 1
			if j==i and matriz[i].item(i)!=1:
				Resultado = False
				break
			##Reviso si los demas elementos son distintos de 0
			elif j!=i and matriz[i].item(j)!=0:
				Resultado = False
				break
	return Resultado

def ResultadoMatrices(matriz1,matriz2):
	if esMatrizIdentidad(matriz1) is True and esMatrizIdentidad(matriz2) is True:
		print("--El producto entre las matrices da la matriz identidad")
	else: print("--El producto entre las matrices no da la matriz identidad")


## Norma Matricial: ||A|| 
def norma(matriz):
	suma=0
	lista=[]
	for i in range(0,matriz.shape[0]):
		for j in range(0,matriz.shape[0]):
			#Sumo en valor absoluto a todos los elementos de cada fila
			suma+=np.abs(matriz[i].item(j))
		lista.append(suma) #Agrego la suma a la lista
		"""
		Vuelvo a poner la suma en cero para que en la proxima iteracion haga la suma de la
		de la sgte fila, y asi hasta que no halla mas filas que sumar 
		"""
		suma=0 
	#print(lista)
	return np.max(lista) #Devuelvo el valor mas alto de la lista

## Numero de condicion: k(A) = ||A|| * ||A^-1|| 
def numCondicion(norma1, norma2):
	return norma1*norma2

"""
-- Cumple que:
κ(A) ≥ 1, y si κ(A) es un numero proximo a 1 se dice que A es
una matriz bien condicionada; y si es mucho mayor que 1, que es
mal condicionada.
"""
def condicionamiento(num):
	if num <=1:
		print("Rta: Matriz bien condicionada")
	else:
		print("Rta: Matriz mal condicionada")
#-------------------------------------------------------------------------------------------------------------------
print("---Matriz A")
a=np.array([[1,2,3],[0,0,2],[0,1,1]])
print(a)
print("---Matriz A^-1")
print(np.linalg.inv(a)) #matriz inversa de a
#### a @ np.linalg.inv(a)  ##Producto entre matrices

"""
--- Veo si el producto entre las matrices da como resultado la matriz identidad
Paso como parametros el producto de las matrices ((A*A^-1) ^ (A^-1*A)) convertidas a int, ya que el 
producto me dara una matriz float 
"""
ResultadoMatrices(np.matrix(a @ np.linalg.inv(a), dtype=int),np.matrix(np.linalg.inv(a) @ a, dtype=int))

#print("--||A|| :" ,norma(a))
print(f"--||A|| : {np.linalg.norm(a,np.inf)}") #Otra forma de calcular la norma infinita 
#print("--||A^-1|| :" ,norma(np.linalg.inv(a)))
print(f"--||A^-1|| :{np.linalg.norm(np.linalg.inv(a),np.inf)}")
#print("--k(A): ",numCondicion(norma(a),norma(np.linalg.inv(a))))
print("--k(A): ",numCondicion(np.linalg.norm(a,np.inf),np.linalg.norm(np.linalg.inv(a),np.inf)))
#condicionamiento(numCondicion(norma(a),norma(np.linalg.inv(a))))
condicionamiento(numCondicion(np.linalg.norm(a,np.inf),np.linalg.norm(np.linalg.inv(a),np.inf)))
#-------------------------------------------------------------------------------------------------------------------
print("---Matriz B")
b=np.array([[2,1],[2,1.01]])
print(b)
print("---Matriz B^-1")
print(np.linalg.inv(b)) #matriz inversa de b

#print(np.linalg.det(b)*np.linalg.det(np.linalg.inv(b)))
ResultadoMatrices(np.matrix(b @ np.linalg.inv(b), dtype=int),np.matrix(np.linalg.inv(b) @ b, dtype=int))

print("--||B|| :" ,norma(b))
print("--||B^-1|| :" ,norma(np.linalg.inv(b)))
print("--k(B): ",numCondicion(norma(b),norma(np.linalg.inv(b))))
condicionamiento(numCondicion(norma(b),norma(np.linalg.inv(b))))
