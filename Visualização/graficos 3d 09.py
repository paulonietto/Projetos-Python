from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm


#Tick off the switch in menu Settings/Preferences | Tools | Python Scientific

# Dados
x = np.arange(-5, 5.1, 0.2)
y = np.arange(-5, 5.1, 0.2)

X, Y = np.meshgrid(x, y)
Z = np.sin(X)*np.cos(Y)


# Cria a figura
figura = plt.figure(figsize = (14,6))

# Adiciona o subplot 1 com projeção 3d
eixo = figura.add_subplot(1, 2, 1, projection = '3d')
grafico = eixo.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

# Adiciona o subplot 2 com projeção 3d
eixo = figura.add_subplot(1, 2, 2, projection = '3d')
grafico = eixo.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Cria a barra de cores como legenda
cb = figura.colorbar(grafico, shrink=0.5)

plt.show()

#Criando wireframe
# Cria a figura
figura = plt.figure(figsize=(8,6))

# Subplot
eixo = figura.add_subplot(1, 1, 1, projection = '3d')

# Wire frame
grafico = eixo.plot_wireframe(X, Y, Z, rstride=4, cstride=4)

plt.show()