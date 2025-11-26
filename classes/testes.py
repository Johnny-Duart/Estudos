class Animal:
    def __init__(self, nome):
        self.nome = nome
        print(nome)


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)


dog = Cachorro("Rodolfo")
