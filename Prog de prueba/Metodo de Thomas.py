import numpy as np
import matplotlib.pyplot as plt
from math import pi, fabs , sqrt
import random
from sympy import *

def Thomas(a, b, c, d):
    n = len(d)  # número de filas

    # Modifica los coeficientes de la primera fila
    c[0] /= b[0]  # Posible división por cero
    d[0] /= b[0]

    for i in range(1, n):
        ptemp = b[i] - (a[i] * c[i-1])
        c[i] /= ptemp
        d[i] = (d[i] - a[i] * d[i-1])/ptemp

    # Sustitución hacia atrás
    x = [0 for i in range(n)]
    x[-1] = d[-1]

    for i in range(-2, -n-1, -1):
        x[i] = d[i] - c[i] * x[i+1]

    return x

def vecB(matriz): #Los elementos de la diagonal principal
    lista=[]
    for i in range(0,matriz.shape[0]):
        lista.append(matriz[i].item(i))
    array = np.array(lista)
    return array.astype(int)

def vecC(matriz): #Los elementos por encima de la diagonal principal
    lista=[]
    for i in range(0,matriz.shape[0]-1):
        lista.append(matriz[i].item(i+1))
    array = np.array(lista)
    return array.astype(int)

def vecA(matriz): #Los elementos por debajo de la diagonal principal
    lista=[]
    for i in range(0,matriz.shape[0]-1):
        lista.append(matriz[i+1].item(i))
    array = np.array(lista)
    return array.astype(int)

##--------------------------------------------------------------------------------------
a = np.array([[2,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,2]])
print(a)
d = np.zeros(len(vecA(a)))
d = d.astype(int)
print(d)
"""
print(vecB(a))
print(vecC(a))
print(vecA(a))
"""
print(f"### Solucion: {Thomas(vecA(a),vecB(a),vecC(a),d)}")

d=np.array([2,4,6])
print(d)
print(f"### Solucion: {Thomas(vecA(a),vecB(a),vecC(a),d)}")
