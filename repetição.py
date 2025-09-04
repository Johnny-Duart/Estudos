'''num_multi = int(input('digite o numero para ser multiplicado: '))
num_loop = int(input('digite ate onde o numero vai ser multiplicado: '))
num_ver = 1
while num_ver <= num_loop:
    print(f'o seu numero é: {num_multi} x {num_ver} = {num_multi * num_ver}')
    num_ver += 1'''
'''class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('plim plim')

    def parar(self):
        print('estamos parando!\n Bicicleta parada!')

    def correr(self):
        print('vrummmmmm')


b1 = Bicicleta('Vermelha', 'Caloi', 2019, 5000)
print(Bicicleta('verde', 'caloi', 2000, 1900))'''

'''class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        return('Auauau')

    def dormir(self):
        if self.acordado == 'dormindo':
            self.acordado = False
            return('ZZZZZZZ...')
        else:
            self.acordado
            return('Balançando o rabo')


cachorro1 = Cachorro('rogerio', 'azul')

print(cachorro1.latir())
print(cachorro1.dormir())
'''


class Bicicleta:

    def __init__(self, cor, modelo, ano: int, valor: float | int):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def correr(self):
        print('vrummmm')

    def buzinar(self):
        print('bibi')

    def parar(self):
        print('estamos parado senhor!')

    def __str__(self):
        # return f'{self.__class__.__name__}: {self.cor}, {self.ano}'
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}'
                                for chave, valor in self.__dict__.items()])}'


bicicleta1 = Bicicleta('Verde', 'Super', 2000, 1.500)
'''bicicleta1.buzinar()
bicicleta1.parar()
'''
print(bicicleta1)
