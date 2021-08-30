import numpy as np
import matplotlib.pyplot as plt
from math import pi, fabs
import random

def f(x): return x**(-1)-np.tan(x)
"""
-- Formula de la secante:
Xn+1= Xn - ((f(Xn)*(Xn-Xn-1))/(f(Xn)-f(Xn-1)))

La secante al ser un metodo abierto, la raiz no necesariamente
tiene que estar dentro del intervalo
"""
def secante(a,b,eps,max):
    #eps = 10**(-3)
    #a=Xn-1 ; b=Xn ;  XnC = Xn+1
    i=0
    error=eps*2    
    XnC=0
    print("Valor de a = ",a)
    print("Valor de b = ",b)
    print("Error= ", error)

    while (error>eps ):
        XnC= b - ((f(b)*(b-a))/(f(b)-f(a))) #Punto encontrado en la formula: Xn+1
        error = fabs(b-a) #Error de la secante
        a = b
        b = XnC
        i += 1 
        print("----------------Iteracciones: ", i)
        print("Valor de a = ",a)
        print("Valor de b = ",b)
        print("Error= ", error)
    if(i>max): print(f"No Converge en {max} iteracciones ")
    else: print(f"Raiz = {XnC} , Numero de iter= {i}")

"""
En regula falsi al ser un metodo cerrado, debo controlar primero que la raiz
este dentro del intervalo.
"""

def regulafalsi(a,b,eps,max):
    i=1
    x= b-((f(b)*(b-a))/(f(b)-f(a)))
    #print("Valor de a = ",a)
    #print("Valor de b = ",b)
    #print("Error= ", fabs(a-b))
    #print("Numero max de iter: ", max)
    #print("Error maximo: ", eps)
    
    #print("f(a)= ", f(a))
    #print("f(b)= ", f(b))
    #print("f(p)", f(x))
    ##Controlo si la raiz esta dentro del intervalo

    if((f(a)*f(b))>0): print("La raiz no se encuentra en el intervalo")
    else:
        while(i<max and (fabs(a-b))>eps):
            i+=1
            if((f(a)*f(x))>0): a=x
            else: b=x
            
            x=b-(f(b)*(b-a))/(f(b)-f(a))
        
            #print("-----------------Iteracciones: ", i)
            #print("Valor de a = ",a)
            #print("Valor de b = ",b)
            #print("Error= ", fabs(a-b))
            #print("f(a)= ", f(a))
            #print("f(b)= ", f(b))
            #print("f(p)", f(x))
        if(i>=max): print(f"No Converge en {max} iteracciones ")
        else:print(f"Raiz = {x} , Numero de iter= {i}") 



#print(f(3.14))
#secante(0.5, 1.5,10**(-3),50)
#regulafalsi(0.5, 1.5, 10**(-3),100)
#secante(0.5, pi/2,10**(-3),50)
regulafalsi(0.5, pi/2, 10**(-3),1000)

"""
Conclusiones:

Con los puntos de los intervalos que nos dan podemos concluir en este caso que
el metodo de la secante encuentra mucho mas rapido la raiz que el metodo de regula falsi.

Pero la ventaja que tiene regula falsi es que me asegura la convergencia (aunque sea lenta)
al contrario de la secante que puede diverger, dependiendo de los resultados.
"""