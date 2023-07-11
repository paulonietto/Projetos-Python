from pylab import *
import matplotlib.pyplot as plt

# Dados
x = linspace(0, 5, 10)
y = x ** 2


# Divide a área de plotagem em dois subplots
figura, eixos = plt.subplots(nrows=1, ncols=2, figsize = (10,4))

# Cria o plot1
eixos[0].plot(x, x**2, x, exp(x))
eixos[0].set_title("Escala Padrão")


eixos[0].plot()
# Cria o plot2 plot(x1,y1, x2,y2)
eixos[1].plot(x, x**2, x, exp(x))
eixos[1].set_yscale("log")
eixos[1].set_title("Escala Logaritmica (y)");

plt.show()



# inserindo Grid

# Dados
x = linspace(0, 5, 10)
y = x ** 2

# Cria os subplots     plt.subplots(nrows=1, ncols=2, figsize = (10,3))
figura, eixos = plt.subplots(1, 2, figsize = (10,3))

# Grid padrão
eixos[0].plot(x, x**2, x, x**3, lw = 2)
eixos[0].grid(True)

# Grid customizado
eixos[1].plot(x, x**2, x, x**3, lw = 2)
eixos[1].grid(color = 'b', alpha = 0.7, linestyle = 'dashed', linewidth = 0.8)

plt.show()