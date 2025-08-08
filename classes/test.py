'''def dizer_oi(nome):
    return f'oi {nome}'


def mensagem(nome):
    return nome('jonathan')


print(mensagem(dizer_oi))'''

def meu_decorador(funcao, nome='Jonathan'):
    def envelope():
        print('Inicio')
        funcao()
        print('fim')
    return envelope


@meu_decorador
def diga_ola(nome='jonathan'):
    print(f'Ola! {nome}')


diga_ola()