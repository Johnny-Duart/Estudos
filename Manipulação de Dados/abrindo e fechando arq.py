"""
por que precisamos manipular arquivos?

os arquivos sao essensais para qualquer tipo de programação
pois fornecem um meio de armazenar e recuperar dados
atraves da manipulação de arquivos podemos persistir os dados alem da vida
util de um programa especifico

por que precisamos manipular aquivos?
os arquivos sao essenciais para qualquer tipo de programação,
pois fornecem um meio de armazenar e recuperar dados.
atraves da manipulação de arquivos podemos persistir os dados alem
da vida util de um programa especifico

se o programa quando fechado ou encerrado perder dados:
programa nao persistente

se o programa quando fechado ou encerrado permanecem dados:
programa persistente

conceito de arquivo em informatica
um arquivo é um container no computador onde as informações
sao armazenadas em formato digital. existem dois tipos de arquivos
que podemos manipular em python:
arquivos de texto e arquivos binarios

abrindo e fechado arquivos:
para manipular arquivos em python, primeiro precisamos abri-los.
usando a função open(), para isso. quando terminarmos de trabalhar
com o arquivo, usamos a função 'close()' para liberar recursos
"""

"""
modo de abertura:
r = read
w = write
a = anexar
"""
arquivo = open(
    "C:\\Users\\jonat\\Desktop\\programas\\python\\Coisas minhas\\manipulação de dados\\exemplo.txt",
    "r",
)

"""
funções do read:
read() = le tudo
readline() = le uma linha
readlines() = le todas as linhas e devolve uma lista
"""
# print(arquivo.read())
# print(arquivo.readline()) # pega a primeira linha
# print(arquivo.readline()) # pega a segunda linha
# print(arquivo.readlines())
arquivo.close()
