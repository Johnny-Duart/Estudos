# importei a biblioteca sistema operacional
import limpardef

"""
Listas; Coleção ordenada, mutavel e permite valores duplicados
Tuplas; Coleção ordenada, imutavel e permite valores duplicados
Dicionarios; Coleção nao ordenada, mutavel e nao permite valores duplicados
"""
# sintaxes de listas e tuplas:
# index      0           1           2
lista = ["exemplo1", "exemplo2", "exemplo3"]
tupla = "exemplo1", "exemplo2", "exemplo3"
print(lista, tupla)

# sintaxe de dicionarios:
# Chave:valor
dicio = {"chave1": "teste", "chave2": "daniel", "chave3": 1999, "chave4": True}
print(dicio)

dicionario = {
    "nome": "Joao",
    "idade": 18,
    "Altura": 1.80,
}
# duplicamos a key 'idade'
print(dicionario["Altura"], type(dicionario["Altura"]))
# retorna o valor 'altura'

print(dicionario.get("nome"))
# get é muito usado quando tu nao sabe se a key existe, por exemplo se a chave
# 'nome' nao existir é possivel criar uma mensagem de retorno como:
print(dicionario.get("sobrenome", 'nao key "sobrenome" existe'))
# ele vai printar o segundo valor pois nao existe a key sobrenome
# isso torna bem melhor pois voce pode fazer programas que conferem se existe
# evitando erros no codigo

print(dicionario.get("idade"))
# mas ela retorna so o ultimo valor, no caso ela foi reescrita

print(dicionario.keys())
# diz quais sao as chaves

print(len(dicionario))
# quantidade de itens (igual qualquer len)

print(dicionario.values())
# os valores de cada chaves

print(len(dicionario.values()))

if "nome" in dicionario:
    print('funcionando, "nome" existe.')
# dicionario tambem sao conhecidos como mapas

print(dicionario.items())
# mostra todos os itens, desde keys ate os valores. isso tudo é mostrado
# em tuplas dentro de uma lista
limpardef.limpa()

# aula 2

dicio = {"nome": "legolas", "idade": 20, "altura": 1.74, "valor_logico": True}

# eu alterei o valor da key 'nome' porem da para adicionar elementos tambem
dicio["nome"] = "Pedro"
print(dicio)

# eu adicionei um valor com update, sendo 'comida fav' a key e 'fezes' o valor
dicio.update({"Comida Fav": "fezes"})
print(dicio)

# eu adicionei uma key chamada 'tamanho do dedo' com o valor de '4.5'
# entao agora mostra a key e o valor
dicio["tamanho do dedo"] = 4.5
print(dicio)

# essa mesma função tambem é possivel usar com o .update
dicio.update({"Estado": "Amado"})
print(dicio)

# para remover os valores e keys podemos usar o popitem
# para apagar o nosso ultimo item do dicionario
dicio.popitem()
print(dicio)
# entao o nosso "Estado" foi apagado
# e se fizermos isso novamente ele vai apagar o proximo.
dicio.popitem()
print(dicio)
# sempre apagando o ultimo item, isso so acontece partir da versão 3.7 acima
# em outras versões apaga um item aleatorio

# com o uso da pop() a gente pode apagar um item especifico
dicio.pop("nome")
print(dicio)
# com isso eu apaguei tanto a key quanto o valor
# tambem podemos usar del

# apagando a key 'comida fav' e o valor 'fezes'
del dicio["Comida Fav"]
print(dicio)
# se usarmos del dicio['ALTURA'] que nao se encontra essa variavel
# ele vai apresentar um erro pois o nome da variavel nao é esse

# para apagarmos tudo, ate o dicionario usamos:
# del dicio
# assim o dicio é apagado por completo.
# para limparmos o que tem dentro podemos usar:
# dicio.clear()

# retorna somente as keys, e nao os valores
for x in dicio:
    print(x)

# retorna somente as keys, e nao os valores
for x in dicio.keys():
    print(x)


# mas quando usar cada um desses dois exemplos??
# for x in dicio: é mais curto e mais usado no dia a dia
# for x in dicio.keys(): é mais explícito,
# mostrando claramente que estamos iterando pelas chaves.
# Pode ser útil para clareza do código em projetos grandes


# retorna somente os valores, e nao as chaves (keys)
for x in dicio:
    print(dicio[x])

# retorna os valores, so que sem usar o dicio[x]
for x in dicio.values():
    print(x)

# mas quando usar cada um desses dois exemplos??
# for x in dicio: seguido de dicio[x] é útil quando você quer trabalhar com
# chave e valor ao mesmo tempo
# for x in dicio.values(): é mais direto quando só te interessam os valores

# retorna tanto a key quanto o valor em tuplas
for x in dicio.items():
    print(x)

# retorna a key e o valor separados e sem estar em tuplas
for x, y in dicio.items():
    print(x, y)

# copia mas nao mantem uma sincronização entre os dicionarios
# entao se voce alterar um, nao altera o outro

# Lembrete sobre cópias:
# Tuplas: Imutáveis, não precisam de cópia, qualquer alteração cria nova tupla.
# Listas e Dicionários:
# copy() ou [:] faz cópia rasa (shallow copy): muda só fora, mas itens
# internos (listas/dicionários) são compartilhados.

# faz a key 'idade' se tornar uma lista dentro do dicionario
dicio.update({"idade": [10, 20]})

# copia exatamente o dicionario
dicio1 = dicio.copy()

print(dicio1)
print(dicio)

# outra forma de criar uma copia do dicionario é usando o dict
diciocopia = dict(dicio)

dicio["idade"].append(30)
print(diciocopia, "\n")
print(dicio)
print(dicio1)
print(diciocopia)

# aula 3

# deletando os valores antigos
del dicio, dicio1, diciocopia, dicionario, lista, tupla, x, y

# apagando o terminal para ficar mais limpo
limpardef.limpa()

# index     0         1         2
tupla1 = "chave1", "chave2", "chave3"
tupla2 = "subchave1", "subchave2", "subchave3"
# força a tupla a trocar index por chaves, entao os index se tornam chaves
dicio = dict.fromkeys(tupla1)
print(dicio)
# porem todas elas com nenhum valor, no caso none


# se fizermos isso:
x = 10
dicio = dict.fromkeys(tupla1, x)
print(dicio)
# todas os valores se tornam o valor de x

# tambem podemos fazer uma tupla dentro de uma tupla assim:
dicio = dict.fromkeys(tupla1, tupla2)
print(dicio)
# mostra que em cada chave tem 3 valores em tuplas

# faz com que as 'subchaves' que antes era os valores se tornem chaves
dicio = dict.fromkeys(tupla1 + tupla2)
print(dicio)

# para conseguir usar mais de uma key
# podemos usar dicionarios dentro de dicionarios

dicio = {
    "dicio1": {"nome": "Julia", "idade": 24, "cidade": "Pelotas"},
    "dicio2": {"nome": "Clayton", "idade": 16, "cidade": "Rio Grande"},
    "dicio3": {"nome": "Amanda", "idade": 19, "cidade": "Porto Alegre"},
}
# com isso temos um dicionario com outro dicionario dentro

# podemos printar so o dicionario para vermos todos os valores e keys:
print(dicio)

# podemos printar so os valores de um dicionario dentro do dicionario:
print(dicio["dicio1"])

# tambem podemos printar somente um valor do dicionario dentro do dicionario:
print(dicio["dicio1"]["nome"])
