"""
A classe abstrata é uma "forma" de se fazer as classes
no caso ela nao pode receber um objeto
e sim ser "mae" de outras classes que terao esses objetos com essas funções

nesse caso:
o controle vai receber ABC e vai ser um molde para proximas classes
e quando usamos o decorador @abstratcmethod
estamos dizendo que para a classe filha funcionar ela tem que ter essa função no codigo
se nao ela gera erro, mesmo que nao seja usada.

"""

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
        print("ligando")

    def desligar(self):
        print("desligando")


class ControleAr(Controle_remoto):
    def ligar(self):
        print("ligando")

    def desligar(self):
        print("desligando")


controle = ControleTv()
controle.ligar()
controle.desligar()


"""class Animal:
    def __init__(self, som):
        self.som = som
    
    def fazer_som(self):
        print(self.som)


class Gato(Animal):
    def __init__(self):
        super().__init__('miau')


gato = Gato()
gato.fazer_som()
"""
