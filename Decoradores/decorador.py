"""
dio:
é possivel definir funções dentro de outras funções. Tais funções sao chamadas
de funções internas ou inner functions
"""


def pai():
    print("escrevendo da pai() função")

    def filho1():
        print("escrevendo da filha filho1() função")

    def filho2():
        print("escrevendo da filho2() função")

    filho2()
    filho1()


pai()

"""
em python, podemos dentro de funções definir outras funções,
e se quisermos colocar varias funções dentro das funções poderiamos

nos podemos retornar funções de funções
python tambem permite que voce funções como valor de retorno
"""


"""
def calcular(operacao):

    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    def nao_existe(a, b):
        return "Operador invalido"

    if operacao == "+":
        return somar
    if operacao == "-":
        return subtrair
    else:
        return nao_existe
"""


def calcular(operacao):

    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    def multiplicao(a, b):
        return a * b

    def divisao(a, b):
        return a / b

    def nao_existe(a, b):
        return "Operador invalido"

    match operacao:
        case "+":
            return somar
        case "-":
            return subtrair
        case "*" | "x" | "X":
            return multiplicao
        case "/":
            return divisao
        case _:
            return nao_existe


print(calcular("x")(10, 20))

"""
agora vamos entender decoradores:
"""


def meu_decorador(funcao):
    def envelope():
        print("faz algo")
        funcao()
        print("faz algo")

    return envelope


@meu_decorador
def ola_mundo():
    print("Ola mundo!")


# sem o "açucar sintatico"
# ola_mundo = meu_decorador(ola_mundo)


ola_mundo()
"""
iremos usar o tal do açucar sintatico
o python permite que voce use decoradores de maneira
mais simples com o simbolo @
"""


"""
pythonando:
decorador nao é nada mais que a gente modificar o resultado final da função
ou seja vamos modificar alguma coisa para a saida seja diferente da final

um decorador nao é nada mais que outra função
e essa função vai receber uma função como parametro (sim isso é possivel)

em python tudo é objeto


def validar(x):
    return x


def soma(x, y):
    return x + y


print(validar(soma)(2, 3))

ou seja x vai ser uma função, e nao pode abrir os parenteses pois sempre que
abrirmos parenteses estamos executando a função


def validar():
    def valida():
        return "fui chamado"

    return valida()


print(validar())


entao da a entender que podemos fazer uma função dentro de uma função.

podemos unir os 2 conhecimentos e fazer algo:



def validar(f, x, y):
    if x < 0 or y < 0:
        raise ValueError("x ou y nao podem ser negativos!")

    else:
        return f(x, y)


def soma(x, y):
    return x + y


print(validar(soma, 10, 10))
# print(validar(soma, -1, 1))


def validar(f):
    def valida(x, y):
        if x < 0 or y < 0:
            raise ValueError("X ou Y nao podem ser negativos!")
        return f(x, y)

    return valida


@validar
def soma(x, y):
    return x + y


print(soma(10, 20))
"""
