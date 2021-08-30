import numpy as np
import matplotlib.pyplot as plt
from math import pi, fabs , sqrt, log
import random
from sympy import *

def Horner(coef,x0):
	resultado=0
	for i in range(0,len(coef)): #Recorrer los coeficientes
		#Multiplicar al valor parcial el valor de x más el coeficiente
		resultado = resultado * x0 + coef[i]
	return resultado
##-----------------------------------------------------------------------
"""
#f(x): 4(x^4)+7(x^3)+3(x^2)+6x+2
valorX=8 #Valor de x
coeficientes=[4,7,3,6,2] #Coeficientes del polinomio

print(f"Resultado:{Horner(coeficientes,valorX)}")
"""
"""
#f(x): 1.01e^(4x)-4.62e^(3x)-3.11e^(2x)+12.2e^(x)-1.99
valorX=1.53 #Valor de x
coeficientes=[1.01*np.e,-4.62*np.e,-3.11*np.e,12.2*np.e,2] #Coeficientes del polinomio

print(f"Resultado:{Horner(coeficientes,valorX)}")
"""
#f(x): 4(x^3)+5(x^2)+10x-5
valorX=2 #Valor de x
coeficientes=[4,5,10,-5] #Coeficientes del polinomio

print(f"Resultado:{Horner(coeficientes,valorX)}")