class Veiculo():
    def __init__(self, cor, placa, num_rodas):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas

    def ligar_veiculo(self):
        print(f'ligando o motor do veiculo: {self.__class__.__name__}')
        print(f'Motor do veiculo: {self.__class__.__name__} ligado!')


class Moto(Veiculo):
    pass


moto = Moto('abc-1234', 'preto', 2)
moto.ligar_veiculo()
# moto.esta_carregado()


class Carro(Veiculo):
    def esta_carregando(self):
        print('Nao estou carregado')


carro = Carro('abc-1324', 'vermelho', 4)
carro.esta_carregando()
