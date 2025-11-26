"""
vamos aprender sobre iteradores e geradores em python.
esses sao conceitos poderosos que nos permitem trabalhar com
sequencias de maneira eficiente

introdução:
Em python, um iterador é um objeto que contem um numero contavel
de valores que podem ser iterados, o que significa que voce pode
percorrer todos os valores. O protocolo do iterador é uma maneira do
python fazer a iteração de um objeto que consiste em dois metodos especiais
"__iter()" e "__next__()"

Ler arquivos grandes:
economizar memoria evitando carregar todas as linhas do arquivo
iterar linha a linha do arquivo
"""


class MeuIterador:
    def __init__(self, numeros: list[int]):
        # o contador nao esta atribuido no construtor pois nao deve ser
        # recebido pelo usuario
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        # transforma o objeto em iteravel, para conseguir usar o metodo next
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration


for i in MeuIterador(numeros=[1, 2, 34]):
    print(i)
