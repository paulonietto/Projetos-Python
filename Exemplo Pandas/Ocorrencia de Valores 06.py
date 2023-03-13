import pandas as pd
import numpy as np

df_dados = pd.read_csv("dataset.csv")

#shape verifica as dimensões
print(df_dados.shape)

#verificar existencia de valores em uma coluna
print(df_dados[df_dados["Quantidade"].isin([5,7,9,11])])
