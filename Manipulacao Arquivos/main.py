import pandas as pd

def testes_leitura_texto(caminho:str):
    arquivo = open(caminho, "r")
    print(arquivo.read())
    # contar caracteres
    print(arquivo.tell())
    # alterar ponteiro para o caractere escolhido do arquivo
    print(arquivo.seek(0, 0))


def gravacao_text(caminho:str, texto:str):
    arquivo = open(caminho, "w")
    arquivo.write(texto)
    arquivo.close()


def acrescentar_texto(caminho:str, texto:str):
    arquivo = open(caminho, "a")
    arquivo.write(texto)
    arquivo.close()

def tratar_csv(caminho_arquivo_csv:str):
    arquivo = open(caminho_arquivo_csv, "r")
    dados = arquivo.read()
    linhas = dados.split("\n")
    matriz =[]
    for linha in linhas:
        array= linha.split(",")
        matriz.append(array)
    return matriz

def ler_csv_pandas(caminho:str):
    df = pd.read_csv(caminho)
    return df


if __name__ == '__main__':
    #testes_leitura_texto("arquivo1.txt")
    #texto = "Ele sabia a dura verdade. A única coisa que poderia destruir a Casa do Dragão era ela mesma."
    #gravacao_text("arquivo2.txt", texto)
    #texto = "\nVocê e eu temos úteros reais. O parto é o nosso campo de batalha. Temos que aprender a encarar esta batalha com firmeza."
    #acrescentar_texto("arquivo2.txt", texto)
    #matriz = tratar_csv("salarios.csv")
    #print(matriz)
    #data_frame = ler_csv_pandas("salarios.csv")
    #print(data_frame)
