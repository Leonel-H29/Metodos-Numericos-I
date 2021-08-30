import numpy as np
import matplotlib.pyplot as plt
from math import pi, fabs , sqrt
import random
from sympy import *

def f(x): return np.e**(x)-x-1
def dxf(x): return np.e**(x)-1
def dxf2(x): return np.e**(x)

def Metodo(x0, eps, max,f,dxf,dxf2):
    i=0
    x1= x0 + 2*eps
    error = 2*eps+1
    while(i<=max and error>eps):
        x1=x0-((f(x0)*dxf(x0))/(dxf(x0)**(2)-f(x0)*dxf2(x0)))
        i+=1
        error = fabs(x1-x0)
        x0=x1
    if(i>max): print(f"No converge en {max} iteracciones")
    else: print(f"Raiz: {x1} ; iteracciones: {i}")

Metodo(1,10**(-5),100,f,dxf,dxf2)
