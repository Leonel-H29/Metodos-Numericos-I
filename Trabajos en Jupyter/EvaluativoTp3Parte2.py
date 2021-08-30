import numpy as np
import matplotlib.pyplot as plt
from math import pi, fabs , sqrt, log
import random
from sys import exit
from sympy import *

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
"""
def gaussseidel(a,b,x):
    n=len(x)
    for i in range(n):
        s=0
        for j in range(n):
            if i!=j:
                s=s+a[i,j]*x[j]
        x[i]=(b[i]-s)/a[i,i]
    return x

def gaussseidelm(a,b,x,e,m):
    n=len(x)
    t=x.copy()
    for k in range(m):
        x=gaussseidel(a,b,x)
        #d=np.max(np.abs(x-t))
        d=np.linalg.norm(x-t,np.inf)
        if d<e:
            return [x,k]
        else:
            t=x.copy()
    return [[],m]
"""
def gaussSeidel(A, b, prec):
	"""Metodo que calcula la solucion Ax = b, usando tecnicas iterativas"""

	n = len(A)
	Xk = [0.0]*n
	sumation = 0.0
	for i in range(n):
		if A[i][i] == 0:
			exit('Los elementos A[i][i] deben ser diferentes de 0')
	Xk1 = [b[i]/float(A[i][i]) for i in range(n)]
	minus = lambda x, y: [x[i]-y[i] for i in range(n)]

	for j in range(n):
		dominancia = 0.0
		for i in range(j+1, n):
			if j != i:
				dominancia += fabs(A[i][j])
		if A[i][i] < dominancia:
			exit('La matriz no converge') 
	while (np.linalg.norm(minus(Xk1,Xk),np.inf) / (np.linalg.norm(Xk1,np.inf)) > prec:
	
		Xk[:] = Xk1[:]
		for i in range(n):
			sumation1 = sum(A[i][j]*Xk1[j] for j in range(i))
			sumation2 = sum(A[i][j]*Xk1[j] for j in range(i+1, n))

			Xk1[i] = (1.0/A[i][i])*(b[i] - sumation1 - sumation2)

		print(Xk1)
	return Xk1

#-------------------------------------------------------------------------------------------------------------------
"""
print("---Matriz A")
a=np.array([[2,3],[1.999,3]])
print(a)
print("---Matriz A^-1")
print(np.linalg.inv(a))
b=np.array([2,1.999])
print(f"-> Solucion del sistema con b={b}: {np.linalg.solve(a,b)}")

print("--||A|| :" ,norma(a))
print("--||A^-1|| :" ,norma(np.linalg.inv(a)))
print("--k(A): ",numCondicion(norma(a),norma(np.linalg.inv(a))))
condicionamiento(numCondicion(norma(a),norma(np.linalg.inv(a))))
"""
#-------------------------------------------------------------------------------------------------------------------
a=np.array([[2,-1,0],[1,6,-2],[4,-3,8]])  # Matriz del sistema.
b=np.array([2,-4,5])  # Vector de terminos independientes.
n=len(b) # Dimension de la matriz.
itmax=100  # Num. de iteraciones.
x=np.array([1,2,3]) # Aproximacion inicial.

##print(gaussseidelm(a,b,x,10**(-5),itmax))
print(gaussSeidel(a,b,10**(-5)))