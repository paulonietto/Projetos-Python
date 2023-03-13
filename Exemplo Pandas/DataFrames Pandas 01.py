import pandas as pd

dados = {"Estado":["Santa Catarina", "Rio de Janeiro", "Tocantins", "Bahia", "Minas Gerais"],
         "Ano": [2004,2005,2006,2007,2008],
         "Taxa Desemprego":[1.5,1.7,1.6,2.4,2.7]}

#criando um data frame a partir do dicionário
df_dados = pd.DataFrame(dados)
print(df_dados)

print(type(df_dados))

#alterar order das colunas de um dataframe
df_dados = pd.DataFrame(dados, columns = ["Estado", "Taxa Desemprego", "Ano"])
print(df_dados)

#criando um dataframe com o dicionário anterior inserindo novas colunas
#index é o rótulo de linha, columns de coluna
df_dados2 = pd.DataFrame(dados, columns=["Estado", "Taxa Desemprego", "Taxa Crescimento","Ano"],
                         index=["estado 1","estado 2","estado 3","estado 4","estado 5"])
print(df_dados2)

#acessar a lista de indices por linnha ou coluna
print(df_dados2.columns)
print(df_dados2.index)

#acessar valores do data frame
print(df_dados2.values)

#tipos de dados no dataframe
print(df_dados2.dtypes)

#retornando valores de uma coluna do dataframe com as informações
print(df_dados2["Ano"])

#retornando somente os valores de uma coluna
print(df_dados2["Ano"].values)

#retornando mais de uma coluna de um data frame
print(df_dados2[["Ano", "Estado"]])

#filtrar por linhas
print(df_dados2.filter(items = ["estado 3"], axis = 0))