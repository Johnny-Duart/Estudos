import functools

"""
funções de decoradores c argumentos:
podemos usar *args e **kwargs na função interna, com isso ela aceitara um
numero arbitrario de argumentos posicionais e de palavras chave
"""


def meu_decorador(func):

    def envelope(*arg, **kwarg):
        print("antes de executar")
        func(*arg, **kwarg)
        print("args: ", arg)
        print("kwarg: ", kwarg)
        print("depois de executar")

    return envelope


@meu_decorador
def ola_mundo(numero, nome, idade):
    print(f"ola mundo, ola {nome}")


ola_mundo(10, nome="Rodolfo", idade=20)

"""
retornando valores de funções decoradas:
o decorador pode decidir se retorna o valor da função
decorada ou nao. Para que o valor seja retornado a função
de envelope deve retornar o valor da função decorada
"""


def duplicar(func):
    @functools.wraps(func)
    def envelope(*arg, **kwarg):
        func(*arg, **kwarg)
        return func(*arg, **kwarg)

    return envelope


@duplicar
def aprender(tecnologia):
    print(f"voce esta aprendendo a {tecnologia}")
    return tecnologia.upper()


print(aprender("python"))

"""
introspecção é a capacidade de um objeto saber sobre seus
proprios atributos em tempo de execução
"""

print(aprender.__name__)

"""
o uso do functools é importante para a documentação do codigo
e metadados, pois ela preserva os valores da função decorada
"""
