import pandas as pd
import numpy as np

dados = {"Estado":["Santa Catarina", "Rio de Janeiro", "Tocantins", "Bahia", "Minas Gerais"],
         "Ano": [2004,2005,2006,2007,2008],
         "Taxa Desemprego":[1.5,1.7,1.6,2.4,2.7]}


df_dados = pd.DataFrame(dados, columns=["Estado", "Taxa Desemprego", "Taxa Crescimento","Ano"],
                         index=["estado 1","estado 2","estado 3","estado 4","estado 5"])


#resumo estatístico para colunas numéricas
print(df_dados.describe())

#verificar se o data frame tem NaN
print(df_dados.isna) #se usar parenteses o isna retorna true ou False df_dados.isna()

#varificar se uma coluna possui valores ausentes
print(df_dados["Taxa Crescimento"].isna())

df_dados["Taxa Crescimento"] = np.arange(5.)

print(df_dados)

print(df_dados.isna())

print(df_dados.describe())
