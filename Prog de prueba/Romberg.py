import numpy as np
import matplotlib.pyplot as plt
from math import pi, fabs , sqrt

def f(x): return x**2

def print_row(lst):
    print( ' '.join('%11.8f' % x for x in lst))

"""
- Aproximo la integral definida de f desde a hasta b
- eps es la presicion deseada
"""
def romberg(f, a, b, eps):
    R = [[0.5 * (b - a) * (f(a) + f(b))]]  # R[0][0]
    print_row(R[0])
    n = 1
    while True:
        h = float(b-a)/2**n #Calculo el valor de la banda
        R.append((n+1)*[None]) #Agrego una fila vacia
        R[n][0] = 0.5*R[n-1][0] + h*sum(f(a+(2*k-1)*h) for k in range(1, 2**(n-1)+1)) #Para los limites adecuados
        for m in range(1, n+1):
            R[n][m] = R[n][m-1] + (R[n][m-1] - R[n-1][m-1]) / (4**m - 1)
        print_row(R[n])
        if abs(R[n][n-1] - R[n][n]) < eps: #Me indica hasta cuando parar
            return R[n][n]
        n += 1

romberg(f,-1,1,10**(-6))