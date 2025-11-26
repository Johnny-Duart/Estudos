import datetime

"""
decorador de log
gerador de relatorios
iterador personalizado

decorador = implemente um decorador que seja aplicado a todas as funções
de transações (deposito, saque, criação de conta, etc).
esse decorador deve registrar (printar) a data e hora de cada transação, bem como o tipo de transação

gerador = criar um gerador que permita iterar sobre as transações de
uma conta e retorne uma a uma, as transações que foram realizadas
esse novo gerador deve tambem ter uma forma de filtrar as transações baseado em seu tipo (por exemplo apenas saques
ou apenas depositos)

iterador personalizado = implemente um iterador personalizado ContaIterador
que permita iterar sobre todas as contas do banco, retornando informações
baiscas de cada conta (numero, saldo atual, etc)

"""


class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""\n
                agencia:\t{conta.agencia}
                numero:\t{conta.numero}
                titular:\t{conta.cliente.nome}
                saldo:\t{conta.saldo:.2f}
"""
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1


def log_transacao(func):
    def wrapper(*arg, **kwarg):

        resultado = func(*arg, **kwarg)
        print(f"{datetime.datetime.now()}: {func.__name__.upper()}")
        return resultado

    return wrapper


class Historico:
    def __init__(self):
        self._transacoes = []

    # getter
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self.transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.datetime.now,
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self.transacoes:
            if (
                tipo_transacao is None
                or transacao["tipo"].lower() == tipo_transacao.lower()
            ):
                yield transacao


@log_transacao
def depositar(teste):
    return f"{teste}"


print(depositar("argumento"))
