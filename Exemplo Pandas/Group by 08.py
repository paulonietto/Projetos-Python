import pandas as pd
import numpy as np

df_dados = pd.read_csv("dataset.csv")
#agrupar por segmento e região retornando a taxa média de vendas por grupo
df_agrupado = df_dados[["Segmento","Regiao", "Valor_Venda"]].groupby(["Segmento","Regiao"]).mean()
print(df_agrupado)

#Agregacao do group by com mais de uma operação na coluna numerica
df_agregado = df_dados[["Segmento","Regiao", "Valor_Venda"]].groupby(["Segmento","Regiao"]).agg(['mean', 'std','count'])
print(df_agregado)