import pandas as pd
import numpy as np

df_dados = pd.read_csv("dataset.csv")

#chamar coluna específica
print(df_dados.Valor_Venda.describe())

#gerar um dataframe a partir de uma query

df2 = df_dados.query("229 < Valor_Venda <10000")
print(df2.describe())

df3 = df2.query(" Valor_Venda>766")
print(df3.head())