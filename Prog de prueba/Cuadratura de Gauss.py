import numpy as np
import matplotlib.pyplot as plt
from math import pi, fabs , sqrt, log
import random
from sympy import *

def func(x): return (np.e**(x) * np.sin(x)) / (1 + x**2)
#Forma Iterativa
def cuadratura_gauss(x,w,n,f):
    suma=0;
    print("-----------------------Numero de Intervalos: ",n)
    for i in range(0,n):
        #print("--Nodo: ",x[i])
        #print("--Coeficiente: ",w[i])
        #print("--f(x[i]+1): ", f(x[i]+1))
        suma+=w[i]*(f(x[i]+1))
        #print("--Suma: ", suma)
        #print("--------")
    return suma

#Forma Recursiva
def cuadratura_gauss2(x,w,n,f):
    if n==0: return 0
    
    else:
        return(w[n-1]*(f(x[n-1]+1)))+ cuadratura_gauss2(x,w,n-1,f)


x1=[-0.5773502692,0.5773502692]
w1=[1.0000000000,1.0000000000]

x2=[-0.7745966692,0,0.774566692]
w2=[0.5555555556,0.888888889,0.5555555556]

x3=[-0.8611361159,-0.3399810436,0.3399810436,0.8611361159]
w3=[0.3478548451,0.6521451549,0.6521451549,0.3478548451]

#####Probando con la forma recursiva
print("-----Valor de la integral a): ", cuadratura_gauss(x1,w1,2,func))
print("-----Valor de la integral b): ", cuadratura_gauss(x2,w2,3,func)) 
print("-----Valor de la integral c): ", cuadratura_gauss(x3,w3,4,func))

#####Probando con la forma iterativa
print("-----Valor de la integral a): ", cuadratura_gauss2(x1,w1,2,func))
print("-----Valor de la integral b): ", cuadratura_gauss2(x2,w2,3,func))
print("-----Valor de la integral b): ", cuadratura_gauss2(x3,w3,4,func))

