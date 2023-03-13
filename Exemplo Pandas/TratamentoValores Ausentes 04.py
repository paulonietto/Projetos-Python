import pandas as pd
import numpy as np

df_dados = pd.read_csv("dataset.csv")
print(df_dados.head())

#verificar quantidade de NaN por coluna
print(df_dados.isna().sum())


#descobrir a moda dos valores
#Value conts retorna no numéro de ocorrencias de cada valor ordenado da maior para a menor ocorrencia

print(df_dados["Quantidade"].value_counts())
moda = df_dados["Quantidade"].value_counts()[0] #indice 0 pegar o mais recorrente, primeiro

#inserir nos valores ausentes a moda. Inplace True altera diretamente nos dados
df_dados["Quantidade"].fillna(moda, inplace=True)

#verificar quantidade de NaN por coluna
print(df_dados.isna().sum())

#se usar a media ele desconsidera as linhas NaN
