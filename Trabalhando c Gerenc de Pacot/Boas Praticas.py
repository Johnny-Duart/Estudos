"""
PYthon tem uma serie de convenções e melhores praticas codificadas em PEPs
(Propostas de Melhorias do Python). A mais conhecida destas é provavelmente a
PEP 8, que cobre o estilo de codificação

O que é PEP 8

Pep 8 é o guia de estilo para codificação em python, ele possui convenções
sobre nomes de variaveis, uso de espaços em branco, comprimento da linha e
muitas outras coisas que ajudam a manter o codigo python consistente e legivel

PRINCIPAIS RECOMENDAÇÔES DA PEP 8:

usar 4 espaços para identação, limitar as linhas a 79 caracteres
usar nomes de variaveis em snake_case para funções e variaveis, e
CamelCase para classes
"""


def somar(argumento_1, argumento_2):
    # essa função é um exemplo seguindo a PEP 8
    pass


class ContaBancaria:
    # essa classe é um exemplo seguindo a PEP 8
    pass


"""
Uso de ferramentas de checagem de estilo
Para nos ajudar a seguir as recomendações da PEP 8
podemos usar f erramentas de checagem de estilo como
flake8, essas ferramentas verificam nosso codigo e nos
informam onde estamos desviando do guia de estilo

Formatação automatica de codigo:

Black é uma ferramenta de formatação de codigo Python
segue a filosofia 'formato unico'. BLack reformata todo o seu
arquivo em um estilo consistente, simplificando a tarefa de
manter o codigo em conformidade com a PEP 8
"""

"""
Organização de imports com isort

Isort é uma ferramente Python para classificar
importações alfabeticamente e separalas automaticamente em seções.
Ele proporciona uma maneira rapida e facil de ordenar e categoziar suas
importações
"""
