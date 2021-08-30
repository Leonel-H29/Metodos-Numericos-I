import numpy as np
import matplotlib.pyplot as plt
from math import pi, fabs , sqrt, log
import random
from sympy import *

#Factorizacion LU
def triangulacion(A,b,n):
	for k in range(1,n):
		for i in range(k+1,n):
			A[i][k]/=A[k][k] #A[k][k]!=0
			for j in range(k+1,n):
				A[i][j]-=A[i][k]*A[k][j]
	return sustitucion(A,b,n)

def sustitucion(A,b,n):
	x=np.zeros(n)
	x=x.astype(int)
	#Resolucion Ly=b
	x[0]=b[0]
	for k in range(1,n):
		suma=0
		for j in range(0,k-1):
			suma+=A[k][j]*x[j]
		x[k]=b[k]-suma
	#Resolucion Ux=y
	x[n-1]/=A[n-1][n-1]
	for i in range(n-1,0,-1):
		suma=0
		for j in range(i+1,n):
			suma+=A[i][j]*x[j]
		x[i]=x[i]-suma/A[i][i]
	return x

a=np.array([[2,4,-2],[1,-1,5],[4,1,-2]])
b=np.array([6,0,2])
print(triangulacion(a,b,len(a)))