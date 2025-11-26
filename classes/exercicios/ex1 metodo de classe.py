class Carro:
    def __init__(self, marca, ano, modelo):
        self.marca = marca
        self.ano = int(ano)
        self.modelo = modelo

    def mostrar_carro(self):
        return f"""
marca: {self.marca}
ano: {self.ano}
modelo: {self.modelo}

"""

    @classmethod
    def carro_criado_metodo(cls, texto):
        marca, ano, modelo = texto.split("-")
        return cls(marca, ano, modelo)


carro1 = Carro("bmw", 2000, "iX")
print(carro1.mostrar_carro())

carro2 = Carro.carro_criado_metodo("bmw-2000-iX")
print(carro2.mostrar_carro())
print(carro2.ano)
