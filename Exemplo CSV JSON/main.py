import csv
import json
from urllib.request import urlopen
def gravar_notas_csv():
    with open('notas.csv', 'w') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(("nota 1","nota 2","nota 3"))
        writer.writerow((63,87,92))
        writer.writerow((63, 79,76))
        writer.writerow((72,64,91))

def ler_notas_csv():
    with open('notas.csv', 'r', encoding="utf8", newline="\r\n") as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            print(linha)


def gravar_arquivo_json(arquivo_json):
    with open("dados.json", "w")as arquivo:
        arquivo.write(arquivo_json)

def ler_arquivo_json(caminho):
    with open(caminho)as arquivo:
        texto = arquivo.read()
        dados = json.loads(texto)

def ler_dado_url(caminho: str):
    response = urlopen(caminho).read().decode('utf8')
    dados = json.loads(response)[0] #[0] para pegar o primeiro elemento do json
    print(dados)
    print("Título:",dados["title"])
    print("URL:", dados["url"])
    print("Duração:", dados["duration"])
    print("Número de Visualizações:", dados["stats_number_of_plays"])



if __name__ == '__main__':
    #gravar_notas_csv()
    #ler_notas_csv()
    dict_guido = {"nome:":"Guido von Rossum",
                  "linguagem":"Python",
                  "similar": ['C','Modula-3', "Lisp"],
                  "users":1000000}

    #transformar dicionario em json
    #print(json.dumps(dict_guido))
    #gravar_arquivo_json(json.dumps(dict_guido))
    #ler_arquivo_json("dados.json")
    ler_dado_url("http://vimeo.com/api/v2/video/57733101.json")




