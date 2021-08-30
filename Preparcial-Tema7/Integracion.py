import numpy as np
import matplotlib.pyplot as plt
from math import pi, fabs , sqrt


def simpson_compuesta(a,b,n,f):
    sumatoria = 0.0
    h = (b-a)/n

    for i in range(1,n):
        if((i%2)==1): sumatoria += 4* f(a + h*i)
        else: sumatoria += 2 *f(a + h*i)
    return((h/3) * (f(a) + sumatoria + f(b)))

def trapecio_compuesta(a, b, n, f):
    h = (b-a)/n
    sumatoria = 0
    
    for i in range(1, n):
        sumatoria += f(a + h*i)
        
    return (h/2) * (f(a) + 2 * sumatoria + f(b))

def Richadson(i1,i2): return ((4/3)*i2 - (1/3)*i1)



