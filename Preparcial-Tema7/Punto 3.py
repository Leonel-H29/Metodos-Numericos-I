from Integracion import *

def f(x): return x**2

#h=0.5 -> n=4
#h=0.25 -> n=8

print(trapecio_compuesta(-1,1,4,f)) #Valor de la integral con h=0.5
print(trapecio_compuesta(-1,1,8,f)) #Valor de la integral con h=0.25
print("Ir ≈ ", Richadson(trapecio_compuesta(-1,1,4,f),trapecio_compuesta(-1,1,8,f)))