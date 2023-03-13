from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt


iris = load_iris()

df_iris = pd.DataFrame(iris['data'], columns = iris['feature_names'])
df_iris['species'] = iris['target']

print(df_iris)
df_iris.plot()
plt.show() # não precisa de matplot lib no Jupyter

#scatter
df_iris.plot.scatter(x = 'sepal length (cm)', y = 'sepal width (cm)')
plt.show()

#area
colunas = ['sepal length (cm)','sepal width (cm)', 'petal length (cm)','petal width (cm)']
df_iris[colunas].plot.area()
plt.show()

#barra
df_iris.groupby('species').mean().plot.bar()
plt.show()


#pizza
df_iris.groupby('species').count().plot.pie(y = 'sepal length (cm)')
plt.show()

#KDE(Kernel Density Function)
df_iris.plot.kde(subplots = True, figsize = (8,8))
plt.show()

#boxplot
colunas = ['sepal length (cm)','sepal width (cm)', 'petal length (cm)','petal width (cm)']
df_iris[colunas].plot.box(figsize = (8,8))
plt.show()