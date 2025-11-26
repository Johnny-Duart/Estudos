class Pessoa:
    especie = "Humano"

    def __init__(self, nome):
        self.nome = nome

    @classmethod
    def mudar_especie(cls, nova_especie):
        cls.especie = nova_especie


p1 = Pessoa("Jonathan")
print(p1.especie)

Pessoa.mudar_especie("Android")
print(p1.especie)
