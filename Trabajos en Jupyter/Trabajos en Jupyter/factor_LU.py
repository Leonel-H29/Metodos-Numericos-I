import numpy as np

def sust_adel(L, b):
    """Resuelve un sistema de ecuaciones
    con matriz de coeficientes triangular inferior 
    mediante el metodo de sustitución hacia adelante
    y retorna la matriz de incógnitas.
    
    Argumentos:
    L -- Matriz de coeficientes triangular inferior
    b -- Matriz de terminos independientes
    """
    
    x = [0, 0, 0]
    
    suma = 0
    
    x[0] = b[0] / L[0][0]
    
    for i in range(1,len(b)):
        suma = 0
        for j in range(0, i-1):
            suma += L[i][j] * x[j]
        
        x[i] = (b[i] - suma) / L[i][i]
    
    return x


def sust_atras(U, b):
    """Resuelve un sistema de ecuaciones
    con matriz de coeficientes triangular superior 
    mediante el metodo de sustitución hacia atrás
    y retorna la matriz de incógnitas.
    
    Argumentos:
    U -- Matriz de coeficientes triangular superior
    b -- Matriz de terminos independientes
    """
    
    x = [0, 0, 0]
    n = len(b)-1
    suma = 0
    
    x[n] = b[n] / U[n][n]
    
    for i in range(n-1, -1, -1):
        suma = 0
        for j in range(i+1, n):
            suma += U[i][j] * x[j]
        
        x[i] = (b[i] - suma) / U[i][i]
    
    return x


def sust_adel_LU(L, b):
    """Resuelve un sistema de ecuaciones
    con matriz de coeficientes triangular inferior 
    mediante el metodo de sustitución hacia adelante
    y retorna la matriz de incógnitas.
    
    Argumentos:
    L -- Matriz de coeficientes triangular inferior
    b -- Matriz de terminos independientes
    """
    
    x = [0, 0, 0]
    
    suma = 0
    
    x[0] = b[0]
    
    for i in range(1,len(b)):
        suma = 0
        for j in range(0, i):
            suma += L[i][j] * x[j]
        
        x[i] = (b[i] - suma)
    
    return x

def sust_atras_LU(U, b):
    """Resuelve un sistema de ecuaciones
    con matriz de coeficientes triangular superior 
    mediante el metodo de sustitución hacia atrás
    y retorna la matriz de incógnitas.
    
    Argumentos:
    U -- Matriz de coeficientes triangular superior
    b -- Matriz de terminos independientes
    """
    
    x = [0, 0, 0]
    n = len(b)-1
    suma = 0
    
    x[n] = b[n] / U[n][n]
    
    for i in range(n-1, -1, -1):
        suma = 0
        for j in range(i+1, n+1):
            suma += U[i][j] * x[j]

        x[i] = (b[i] - suma) / U[i][i]
    
    return x

def resolver_LU(L, U, b):
    """Resuelve un sistema de ecuaciones
    con las matrices L y U resultantes del
    metodo de factorizacion LU
    y retorna la matriz de incógnitas.
    
    Argumentos:
    L -- Matriz de coeficientes triangular inferior
    U -- Matriz de coeficientes triangular superior
    b -- Matriz de terminos independientes
    """
    
    return sust_atras_LU(U, sust_adel_LU(L, b))


def factorizar_LU_PE(A):
    """Factoriza la matriz A
    mediante metodo de pivoteo parcial escalado.
    
    Argumentos:
    A -- Matriz de coeficientes
    
    
    Retorna en forma de tupla: 
    LU -- Matriz compuesta por L y U
    mov -- Número de movimientos
    """
    n = len(A)
    mov = 0
    LU = np.array(A, dtype=float)
    P = np.arange(n)
    S = np.arange(n)

    #Inicializar S        
    for i in range(0, len(A)):
        S[i] = np.max(np.abs(A[i]))
    
    for k in range(0, n-1):
        #Determinar la fila maxima
        fila_max = k
        maximo = np.abs(LU[P[k]][k]) / S[P[k]]
        for i in range(k, n):
            if ( (np.abs(LU[P[i]][k]) / S[P[i]]) > maximo ):
                maximo = (np.abs(LU[P[i]][k]) / S[P[i]]) 
                fila_max = i
                
        #Permutar filas en P
        if (fila_max != k):
            mov += 1
            aux = P[k]
            P[k] = fila_max
            P[fila_max] = aux
        
        #Calcular LU 
        for i in range(k+1, n):
            
            LU[P[i]][k] = LU[P[i]][k] / LU[P[k]][k]
            
            for j in range(k+1, n):
                LU[P[i]][j] = LU[P[i]][j] - LU[P[i]][k] * LU[P[k]][j]
    
    return (LU, P, mov)

A = [[2, 1, -3],
     [2, -1, 5],
     [4, 1, -1]]

b = [5, 5, 1]

LU, P, mov = factorizar_LU_PE(A)

H = np.array(LU)

print("LU")
for i in range(len(LU)):
    print(np.around(LU[P[i]], 2))
    H[i] = LU[P[i]]
    
x = resolver_LU(H, H, b)

print("Solución del sistema:")
print(x)
    

























