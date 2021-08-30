import numpy as np
import matplotlib.pyplot as plt
from math import pi, fabs , sqrt, log
import random
from sympy import *

"""
def jacobi(a,b,x0,_max,eps):
    h=0
    error=2*eps+1
    x1=x0.copy()
    while h<_max and error>=eps:
        h=h+1
        x0=x1.copy() 
        for k in range(0,len(a)):
            for i in range(0, len(a)):
                suma=0
                for j in range(0, i):
                    suma=suma + a[i][j] * x1[j]
                for j in range(i+1, len(a)):
                    suma=suma + a[i][j] * x0[j] 
            x1[i]=(b[i]-suma)/a[i][i]
        #x1[k]=(b[k]-suma)/a[k][k]
        error=np.max(np.abs(x1 -x0))
            
    if(h>=_max): print(f"Jacobi ### No converge en {_max} iteraciones")
    else:
    	print(f"Jacobi ## Numero de iteraciones: {h}")
    	return x1
"""
        

def gauss_seidel(a,b,x0,_max,eps):
	error = 2*eps+1
	h=0
	x1=x0.copy()
	while h<_max and error>=eps:
		x0=x1.copy()
		h+=1
		for i in range(0,len(a)):
			suma=0
			for j in range(0,i):
				suma += a[i][j] * x1[j]
			for j in range(i+1,len(a)):
				suma += a[i][j] * x0[j]
			x1[i]=(b[i]-suma)/a[i][i]
		#error = max(fabs(x1-x0))
		error=np.max(np.abs(x1 -x0))
		
	if h>=_max: 
		print(f"Gauss Seidel ### No converge en {_max} iteraciones")
	else:
		print(f"Gauss Seidel ## Numero de iteraciones: {h}")
		return x1
				

a=np.array([[6,-2,1],[-2,7,2],[1,2,-5]])  # Matriz del sistema.
b=np.array([4,1,4])  # Vector de terminos independientes.
n=len(b) # Dimension de la matriz.
itmax=100  # Num. de iteraciones.
#x=zeros(n) # Aproximacion inicial.
x=np.ones(n) #Matriz con n elementos iguales a 1
#print(jacobi(a,b,x,itmax,10**(-6)))
print(gauss_seidel(a,b,x,itmax,10**(-6)))

