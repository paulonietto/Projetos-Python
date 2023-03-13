import pandas as pd
import numpy as np

df_dados = pd.read_csv("dataset.csv")


#pesquisar substring no dataframe - começa com, termina com
print(df_dados[df_dados.Segmento.str.startswith('Con')])
print(df_dados[df_dados.Segmento.str.endswith('mer')])

#split de valores da colna por caractere escolhido retornando uma lista
print(df_dados['ID_Pedido'].str.split('-'))

#pegar o ano do ID Pedido
print(df_dados['ID_Pedido'].str.split('-').str[1])

df_dados['Ano'] = df_dados['ID_Pedido'].str.split('-').str[1]

print(df_dados)

#removendo caracteres de uma coluna do datagrame  - lstrip partindo da esquerda, rstrip a partir da direita
#remover o 2 e 0 do ano do pedido
print(df_dados["Data_Pedido"].str.lstrip('20'))

#alterando valores com replace(de, para)
print(df_dados["ID_Cliente"].str.replace('CG', 'AX'))

#Concatenar as strings com cat
df_dados["PedidoXSegmento"]= df_dados['ID_Pedido'].str.cat(df_dados["Segmento"], sep='-')
print(df_dados["PedidoXSegmento"])
