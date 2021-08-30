
#---------------------FUNCION ORIGINAL

def f(x):
    y = x**2 - 2*x - 3
    return y

#---------------------FUNCIONES PROPUESTAS -- PUNTO 1 -------------------

def g1(x):
    y= np.square(2*x + 3)
    return y

def g2(x):
    y = (x**2-3)/2
    return y

def g3(x):
    y = 3/(2-x)
    return y


#--------------------------------GRÁFICA------------------------

#----------Funcion f(x) ----------
x = np.linspace(-4, 4, 100)
y = f(x)
plt.figure(1, (10,6), 50, 'snow', 'g')
plt.plot(x, y)
plt.title("f(x)")
plt.legend(('y'), loc='upper left')
plt.show()

#----------Funcion g1(x) ----------
x = np.linspace(-2, 3.5, 100)
g1 = g1(x)
plt.figure(2, (10,6), 50, 'lightblue', 'g')
plt.plot(x, g1)
plt.plot(x,x)
plt.title("g1")
plt.show()

#La primera bisectriz solo intersecta a la grafica g2, y lo hace en ambas raices
#----------Funcion g2(x) ----------
x = np.linspace(-4.5, 8, 100)
g2 = g2(x)
plt.figure(2, (10,6), 50, 'lightblue', 'g')
plt.plot(x, g2)
plt.plot(x,x)
plt.title("g2")
plt.show()

#----------Funcion g3(x) ----------
x = np.linspace(-2, 2, 100)
g3 = g3(x)
plt.figure(2, (10,6), 50, 'lightblue', 'g')
plt.plot(x, g3)
plt.plot(x,x)
plt.title("g3")
plt.show()


#--------Funciones g propuestas, junto a la primera bisectriz 
#Considero que me mejor analizar las graficas por separado.
x = np.linspace(-1.5, 3.1, 100)
plt.figure(4, (10,6), 50, 'lightblue', 'g')
plt.plot(x, g1, 'black')
plt.plot(x, g2, 'black')
plt.plot(x, g3, 'black')
plt.plot(x,x)
plt.title("Todas las g y la primera bisectriz")
plt.show()

"""