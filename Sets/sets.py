# importei a biblioteca sistema operacional
import limpardef

"""
Listas; Coleção ordenada, mutavel e permite valores duplicados
Tuplas; Coleção ordenada, imutavel e permite valores duplicados
Dicionarios; Coleção nao ordenada, mutavel e nao permite valores duplicados
Sets; Coleção nao ordenada, imutavel e nao permite valores duplicados
"""
# sets tambem sao conhecidos como conjuntos

# a diferença entre dict e sets, é que a gente nao tem chaves aqui, so valores
# entao eu nao preciso colocar 'chave': 'valor'
conjunto = {"João", "Clebin", "Rafael"}
print(type(conjunto))
print(conjunto)
# Nao tem ordem

# se fizermos uma duplicata aqui ele simplesmente ignora
conjunto = {"João", "Clebin", "Rafael"}
print(len(conjunto))
conjunto = {"João", "Clebin", "Rafael", "João", "Clebin", "Rafael"}
print(len(conjunto))
# o retorno continua sendo 3 pois ele ignora dados repetidos

# mesmo tentando duplicar ele pela tupla ele nao aceita duplicatas
tupla = 3, 2, 2, 1.5
conjunto = set(tupla)
print(conjunto)
print(type(conjunto))

# tambem podemos ao inves de passar a tupla pra set
# podemos so colocar os valores e transformar em set assim:

# tupla = 3, 2, 2, 1.5
conjunto = set((3, 2, 2, 1.5))
# usando parenteses duplos
print(conjunto)
print(type(conjunto))

conjunto = {"odeio", "a", "ayra"}


"""conjunto.append('super')
print(conjunto)
nao da para adicionar elementos, nem procurar pelo index
"""
# a unica forma de acessar os itens de um set (conjunto)
# é printando ele por inteiro
# tambem podemos usar um laço de repetição para acessar
# item por item


for x in conjunto:
    print(x)
    if x == "a":
        break

conjunto = {4, 5, 2, 1}
print(4 in conjunto)
print(11 in conjunto)

# AULA 2


limpardef.limpa()
del conjunto
# temos como adicionar elemento com a função add
conj = {1, 2, 3, 11, 6}
print(conj)
conj.add(5)
print(conj)
conj1 = conj
conj2 = {"elementos", "do", "segundo", "conjunto"}
conj1.update(conj2)
print(conj1)

# adicionei conj2 no conj1

conj1.update((1, 2, 3, 10, 12, "conjunto"))
print(conj1)
# adicionei elementos separados no conj1, alem de mostrar que nao se repetem

conj1.pop()
print(conj1)
# remove itens aleatorios da lista, sempre removendo o "index 0"
conj1.pop()
print(conj1)

conj1.remove("elementos")
print(conj1)
# com remove da para falar qual elemento vai ser removido. diferente do pop


conj1.discard("do")
conj1.discard("elemento inexistente")
print(conj1)
# igual o remove, porem a diferença é que se tentar remover algum elemento
# que nao existe, ele nao retorna erro


# aula 3
limpardef.limpa()

# aula sobre a uniao, intersecção, diferença e diferença simetrica

conj1 = {1, 2, 4, 6, 7}
conj2 = {3, 4, 5, 8}
# elemento 4 repetido
conj3 = conj1.union(conj2)
print(conj3)

# mesma coisa que usar o update

conj3 = conj1.intersection(conj2)
print(conj3)
# mostra os elementos IGUAIS que estao presentes nesses conjuntos. e como o 4
# é o unico que se repete entao ele é o unico que aparece

# se quisermos usar somente 1 variavel, sem criar outra variavel no caso o
# conj3 podemos fazer assim:

conjunto1 = {1, 2, 4, 6, 7}
conjunto2 = {3, 4, 5, 8}
# elemento 4 repetido
conjunto1.intersection_update(conjunto2)
print(conjunto1)
# sem precisar criar outra variavel, so usando 1 variavel para mostra a
# intersecção entre o conjunto 1 e 2

conj1 = {1, 2, 3, 5, 5}
conj2 = {2, 3, 6}
conj3 = conj1.symmetric_difference(conj2)
print(conj3)
# na diferença simetrica mostra os elementos que nao se repetem, como nesse
# caso o 2, 3 se repetiam mostrou somente o 1, 5 e 6

# da para fazer a mesma coisa que fizemos com o intersecção com o diferença
# simetrica usando o update

conj1 = {1, 2, 3, 5, 5}
conj2 = {2, 3, 6}
conj3 = conj1.difference(conj2)
print(conj3)
conj3 = conj2.difference(conj1)
print(conj3)
# o unico que mostra elementos diferentes se alterarmos a ordem, mostra os
# elementos de X que nao aparecem em Y
