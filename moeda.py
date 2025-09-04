def metade(num, Formato=False):
    if Formato == True:
        return f'R${num / 2:.2f}'
    else:
        return f'{num / 2:.2f}'


def dobro(num, Formato=False):
    if Formato == True:
        return f'R${num * 2:.2f}'
    else:
        return f'{num * 2:.2f}'


def aumentar(num, porcentagem):
    return f'R${num + (num * porcentagem) / 100:.2f}'


def diminuir(num, porcentagem):
    return f'R${num - (num * porcentagem) / 100:.2f}'
