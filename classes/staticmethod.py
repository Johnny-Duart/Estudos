"""
Metodos estaticos sao nada mais que metodos onde tem
uma função nao ligada a classe, mas ela esta dentro
da classe para deixar o codigo limpo
"""


class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @staticmethod
    def altura(tamanho):
        return f"a altura é de: {tamanho}"


p1 = Pessoa("Joao", 20)
print(p1.altura(150))

"""
no caso a função altura nao precisa da classe pois ela nao usa o self
"""
