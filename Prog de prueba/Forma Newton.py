import numpy as np

def DifDiv(x, y, n):
    for i in range(0,n):
        for j in range(n-1,i, -1):
            y[j]=(y[j]-y[j-1])/(x[j]-x[j-(i+1)])
    return y

def Newton(x,y, n, x0):
    f=DifDiv(x, y, n)
    P=f[0]
    for i in range(1,n):
        aux=f[i]
        for j in range(0,i):
            aux=aux*(x0-x[j])
        P=P+aux
    return P

def Resultado(x, y, n, x0):
    print("-----------Datos de la función")
    print("--Valores de abscisas: ",x)
    print("--Valores de ordenadas: ",y)
    print("--Cantidad de puntos: ",n)
    print("")
    print(f"---> Resultado de interpolar en x = {x0}: {Newton(x, y, n, x0)}")
##--------------------------------------------------------------------------
x = [100,120,150,180,210]
y = [124.1,181.9,285.5,457.4,551.6]
n = 5
x0 = 160
Resultado(x, y, n, x0)


x = [0.1,0.0,0.2,0.3]
y = [5.30,2.00,3.19,1.00]
n = 4
x0 = 0.15
Resultado(x, y, n, x0)

x = [11.79, 43.64, 4.67, 29.1, 3.63, 77.54, 31.1, 53.28, 49.15, 94.51]
y = [3.56, 5.45, 2.22, 4.86, 1.86, 6.28, 4.96, 5.74, 5.62, 6.56]
n = 10
x0 = 30
Resultado(x, y, n, x0)
