import pandas as pd
import numpy as np

df_dados = pd.read_csv("dataset.csv")
# para diverças condicionais usar bitwise (&,|)
print(df_dados[(df_dados.Segmento == "Home Office") & (df_dados.Regiao == "South")])

print(df_dados[(df_dados.Segmento == "Home Office") | (df_dados.Regiao == "South")])

#sample escolhe aleatoriamente n elementos
print(df_dados[(df_dados.Segmento != "Home Office") & (df_dados.Regiao != "South")].sample(5))