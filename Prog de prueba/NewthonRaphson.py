import numpy as np
import matplotlib.pyplot as plt
from math import pi, fabs , sqrt
import random
from sympy import *

def NewtonRaphson(x0, eps, max,f,dxf):
    i=0
    x1= x0 + 2*eps
    error = 2*eps+1
    #print("x0 = ", x0)
    #print("x1 = ", x1)
    #print("Error = ", error)
    #print("Error maximo = ", eps)
    #print("f(x0)*f(x1) ="  , f(x0)*f(x1))
    #print("dxf(x0) = ", dxf(x0))
    #print("")
    
    while(i<=max and error>eps):
        x1=x0-(f(x0)/dxf(x0))
        i=i+1
        error = fabs(x1-x0)
        #print("----------------------------Iteracciones", i)
        #print("x0 = ", x0)
        #print("x1 = ", x1)
        #print("Error = ",error)
        #print("Error maximo = ", eps)
        x0=x1
        
    if(i>max): print("No converge en ", max, "iteracciones")
    else: print("Raiz: ", x1)
#__________________________________________________________________
def f(x): return np.e**(x)-x-1
def dxf(x): return np.e**(x)-1
#__________________________________________________________________
NewtonRaphson(1,10**(-5),100,f,dxf)