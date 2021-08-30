import numpy as np

def lim_f(x):    
    return ((np.e**x - np.e**(-x)) / 2*x)

for i in range(20):
    print (i+1)
    print (lim_f(10**(-(i+1))))
    
    
    
def serie_f (n):
    y = 0.0
    for i in range(n):
        y += 1/((i+1)**4)
    return (y)