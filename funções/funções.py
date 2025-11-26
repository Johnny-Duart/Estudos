import limpardef

# paradigma imperativo, sao conhecido como tipos de programação. tempos a
# programação orientada a objetos a programação imperativa ou paradigma
# imperativo de forma adequada poque ela é basicamente natural sendo o mais
# antigo de todos, nos usamos esse paradigma. ele se baseia no modo de
# funcionamento do computador. quando criamos variaveis armazenamos dados na
# memoria ram do computador e isso é refletido na execução sequenmcial baseada
# em comando e armazenamento  de dados e pode ser alteravel. sao como
# computadores vao executar os programas a nivel de linguagem binaria e a
# parava imperare  em latim significa comandar. as linguagem que usam
# o paradigma imperativo sao praticamente todas. sendo o jeito mais antigo de
# escrever codigos e algoritmos na maquina, tambem conhecido como linguagem de
# maquina. as caracteristicas de um paradigma impertativo; as caracteristicas
# sao: variveis, atribuições e sequencias; e isso é tudo o que estamos vindo
# fazer desde entao e alem disso quando definimos algoritmo é um passo a
# passo. um algoritmo é uma base logica para que voce possa resolver qualquer
# problema logico, entao quando queremos resolver algum problema, a gente
# geralmente buscamos utilizar o raciocionio logico e sequencial. entao tanto
# natural pro ser humano tanto pra maquina e entao quando criamos um arquivo,
# damos uma variavel para ele, criamos outro arquivo e criamos a mesma
# variavel nao da erro pois elas nao tem ligação. e isso acaba limitando os
# nossos arquivos. entao nos temos limites na linguagem de programação, tambem
# chamada de escopo. significando um limite, um territorio onde nao podemos
# interagir essa variavel com qualquer outra variavel com o mesmo nome de
# outro arquivo. e isso é chamado de escopo, e esses arquivos podemso criar
# variaveis com quantas linhas que a gente quer, quando queremos criar uma
# variavel que nao sao acessiveis a todo o codigo, e é pra isso que criamos
# blocos interno e externo. e esse arquivo temos apenas o bloco externo e
# qualquer varivavel declada nele é considerada uma variavel global podendo
# ser usada em qualquer lugar do codigo. porem como so sabemos mexer somente
# com 1 arquivo podemos querer criar uma variavel com o mesmo nome e é pra
# isso que criamos blocos internos e externos. e esse arquivo como esta por
# enquanto temos so o bloco externo, e qualquer variavel que esta nele é
# considerada variavel global. e a vantagem é que ela é acessivel a qualquer
# parte do codigo inclusive em blocos internos, e tambem conseguimos criar
# blocos internos e qualquer variavel criada em um bloco interno é conhecida
# como variavel local, e variaveis locais nao sao acessiveis na nossas
# variaveis globais, uma função é um blooco de codigo que pode ser nomeada e
# pode ser chamada dentro de um programa, e pode ser chamada em qualquer parte
# de um programa quantas vezes for necessaria durante a sua execução. exemplo
# disso a palavra reservada para criar funções me python é 'def'

# bloco externo (tambem conhecido como local)
nome = "Gabriel"
# variavel global
# no python no pip 8 as funções devem ser decladaras com 2 linhas de espaço
# entre qualquer outra linha de codigo


def minha_funcao():
    nome = "Ana"
    print(nome)


# bloco interno
# bloco interno de uma função é conhecido como como corpo da função
# atribuimos a variavel nome com um valor
# e na função colocamos a para ter um print entao quando chamarmos a função
# 'minha_função' ele vai executar o nome, e apos isso vai executar o print
# e tudo o que vai codado dentro dessa função so vai ser acessivel apenas
# dentro desse bloco interno a nao ser que voce tenha
# passado esse valores para fora


print(nome)
# retorna o valor 'gabriel' ao inves do 'ana'. a gente nao usou a função,
# tem o mesmo nome porem o seu dado que foi atribuido é diferente e quando
# pedimos para imprimir a variavel 'nome' so imprime a variavel global

# para chamarmos a função é so botar o nome da função:
minha_funcao()
print(nome)

# AULA 2
limpardef.limpa()

lista = [1, 3, 5, 7, 9]
print(lista)
resto = lista.pop()
print(lista)
print(f"o retorno da função pop: {resto}")
var1 = print("ola mundo")
print(var1)
# diz que a variavel 1 n tem valor, nao tem retorno


def ola_mundo():
    print("ola mundo")


ola_mundo()
retorno = ola_mundo()
print(retorno)
# nao tem retorno
limpardef.limpa()


def ola_mundo():
    return "ola mundo"


ola_mundo()
# nao tem retorno porem se eu fizer:
retorno = ola_mundo()
print(retorno)
# essa é a diferença entre usar o return e o print em uma função,
# mas nao precisamos criar uma variavel retorno, podemos fazer assim:
print(ola_mundo())
# e em questao de linhas nao temos uma grande diferença, e ao usar uma função
# nos queremos que ela tenha um proposito bem definido, e queremos retulizar
# ela diversas vezes, usando dados diferentes e conseguir retornos diferentes.
# entao quando construir função, tem que ter alem da sua definição um retorno
# porque um dos proposito da função é a retulização


"""def par_impar():"""
