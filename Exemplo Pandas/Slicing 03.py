import pandas as pd
import numpy as np
dados = {"Estado":["Santa Catarina", "Rio de Janeiro", "Tocantins", "Bahia", "Minas Gerais"],
         "Ano": [2004,2005,2006,2007,2008],
         "Taxa Desemprego":[1.5,1.7,1.6,2.4,2.7],
         "Taxa Crescimento": np.arange(5.)}


df_dados = pd.DataFrame(dados, columns=["Estado", "Taxa Desemprego", "Taxa Crescimento","Ano"],
                         index=["estado 1","estado 2","estado 3","estado 4","estado 5"])

#pegar linhas de um valor de indice até outro especificado

print(df_dados["estado 2":"estado 4"])
print(df_dados[1:5])

#selecionar elementos de acordo com uma regra Usa a condição interna para
# retornar um array booleano para selecionar as linhas do original
print(df_dados[df_dados["Taxa Desemprego"]>2])

#retornando valores de uma coluna do dataframe com as informações
print(df_dados["Ano"])

#retornando mais de uma coluna de um data frame. O segundo colchetes
# é para estabelecer a lista de elementos que o dataframe deve utilizar
print(df_dados[["Ano", "Estado"]])
