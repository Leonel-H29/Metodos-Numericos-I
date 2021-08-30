import numpy as np

def DifDiv(x, y, n):
    for i in range(0,n):
        for j in range(n-1,i, -1):
            y[j]=float((y[j]-y[j-1])/(x[j]-x[j-(i+1)]))
    return y

def MostrarResultados(x, y, n):
	posiciones=[]
	
	for i in range(0,len(y)):
	    print(f"f[x{i}]: {y[i]}")
	    posiciones.append('x'+str(i)) #posiciones = ['x0','x1','x2',...,'xn']

	aux = ""
	posAct = posiciones[0] + "," + posiciones[1]

	t=DifDiv(x, y, n)
	#print(t)
	print("")
	
	for i in range(1,len(t)):
		print(f"f[{posAct}]: {t[i]}")
		
		if i+1<len(t): aux = posiciones[i+1]
		else: break
		posAct = posAct + "," + aux
		

#----------------------------------------------------------------------------------
x = [100,120,150,180,210]
y = [124.1,181.9,285.5,457.4,551.6]
n = 5
#print(DifDiv(x, y, n))
MostrarResultados(x, y, n)
