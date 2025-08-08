from abc import ABC, abstractmethod

class Controle_remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class ControleTv(Controle_remoto):
    def ligar(self):
        print('ligando')
    
    def desligar(self):
        print('desligando')


class ControleAr(Controle_remoto):
    def ligar(self):
        print('ligando')

    def desligar(self):
        print('desligando')


controle = ControleTv()
controle.ligar()


'''class Animal:
    def __init__(self, som):
        self.som = som
    
    def fazer_som(self):
        print(self.som)


class Gato(Animal):
    def __init__(self):
        super().__init__('miau')


gato = Gato()
gato.fazer_som()
'''