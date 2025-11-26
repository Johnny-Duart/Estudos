class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_com_ano_nascimento(cls, nome, ano_nasc):
        idade = 2025 - ano_nasc
        return cls(nome, idade)


p = Pessoa.criar_com_ano_nascimento("Joao", 2010)
