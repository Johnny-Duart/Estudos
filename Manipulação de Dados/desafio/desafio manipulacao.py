"""
Em nossa aplicação financeira, identificamos a necessidade de rastrear e
auditar as ações dos usuarios para garantir a segurança e a integridade das
operações. O console tem sido util ate agora, mas a quantidade crescente das
operações de atividades torna dificil aocmpnhar todas as operações em tempo
real. Portanto decidimos que é vital registrar essas informações em um arquivo
para analise posterior e backup continuoo

Objetivo:
Modificar o atual decorador de log, que imprime informações no console, para
que ele salve essas informações em um arquivo de log, possibilitanto a revisao
mais facil em uma analise detalhada das operações dos usuarios

O decoradro deve registrar o seguinte para cada chamada da função
1 data e horas atuais
2 nome da função
3 argumentos da função
4 valor retornado pela função
5 o aqruivo de log deve ser chamado log.txt
6 se o arquivo log.txt ja existir, os novos logs devem ser adicionados ao
final do arquivo (ou seja manter o historico e adicionar no final do arquivo a
nova operação)
7 cada entrada de log deve estar em uma nova linha
"""

import textwrap
from abc import ABC, abstractmethod
from datetime import datetime
from pathlib import Path

import pytz

ROOT_PATH = Path(__file__).parent


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
            Agência:\t{conta.agencia}
            Número:\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
"""
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 2:
            print("\n Excedeu o limite de transações permitidas hoje!")
            return

        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ('{self.nome}')('{self.cpf}')>"


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.\n")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===\n")
            return True

        else:
            print("\nOperação falhou! Valor informado é inválido!\n")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===\n")
            return True
        else:
            print("\nOperação falhou! Valor informado é inválido!\n")
        return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite=500, limite_saques=3):
        return cls(numero, cliente, limite, limite_saques)

    def sacar(self, valor):
        numero_saques = len(
            [
                t
                for t in self.historico.transacoes
                if t["tipo"] == Saque.__name__
            ]
        )
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite!\n")

        elif excedeu_saques:
            print("\nOperação falhou! Número máximo de saques excedido!\n")

        else:
            return super().sacar(valor)

        return False

    def __repr__(self):
        return f"<{self.__class__.__name__}: ('{self.agencia}, {self.numero}, {self.cliente.nome}')>"

    def __str__(self):
        return f"""\n
        Agência:\t{self.agencia}
        C/C:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now(
                    pytz.timezone("America/Sao_Paulo")
                ).strftime("%d-%m-%Y %H:%M:%S"),
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if (
                tipo_transacao is None
                or transacao["tipo"].lower() == tipo_transacao.lower()
            ):
                yield transacao

    def transacoes_do_dia(self):
        data_atual = datetime.now(pytz.timezone("America/Sao_Paulo")).date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(
                transacao["data"], "%d-%m-%Y %H:%M:%S"
            ).date()
            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.sacar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso = conta.depositar(self.valor)
        if sucesso:
            conta.historico.adicionar_transacao(self)


def log_transacao(func):
    def envelope(*args, **kwargs):
        data_hora = datetime.now(pytz.timezone("America/Sao_Paulo")).strftime(
            "%d-%m-%Y %H:%M:%S"
        )
        resultado = func(*args, **kwargs)
        try:
            with open(
                ROOT_PATH / "log.txt", "a", encoding="utf-8", newline=""
            ) as arquivo:
                arquivo.write(
                    f"[{data_hora}] Função '{func.__name__}' "
                    f"executada com argumentos {args}. {kwargs}"
                    f" retornou {resultado if resultado is not None else 'Sucesso'}\n"
                )
        except Exception as exc:
            print(f"Ocorreu um erro {exc}")
        return resultado

    return envelope


def menu():
    menu = """\n
    ===== MENU ====
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    Opção: """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [c for c in clientes if c.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta!\n")
        return
    return cliente.contas[0]


@log_transacao
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado\n")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado\n")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado\n")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n==== Extrato ====\n")
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio():
        tem_transacao = True
        extrato += f"\n{transacao['data']} - {transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    if not tem_transacao:
        extrato = "Não possui nenhuma transação"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("================")


@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\nJá existe cliente com esse CPF!\n")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): "
    )

    cliente = PessoaFisica(nome, data_nascimento, cpf, endereco)
    clientes.append(cliente)

    print("\n== Cliente criado com sucesso! ==\n")


@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\nCliente não encontrado, criação de conta encerrada!\n")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    for conta in ContasIterador(contas):
        print("-" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        op = menu().lower()

        if op == "d":
            depositar(clientes)

        elif op == "s":
            sacar(clientes)

        elif op == "e":
            exibir_extrato(clientes)

        elif op == "nu":
            criar_cliente(clientes)

        elif op == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif op == "lc":
            listar_contas(contas)

        elif op == "q":
            break

        else:
            print(
                "\n@@@ Operação inválida, por favor selecione novamente. @@@"
            )


if __name__ == "__main__":
    main()
    main()
    main()
