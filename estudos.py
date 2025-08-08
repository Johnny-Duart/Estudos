'''conjunto_a = {1, 2, 3, 4}
conjunto_b = {2, 3, 4}
conjuntointersecao = conjunto_a.intersection(conjunto_b)

print(conjuntointersecao)
conjuntoissubset = conjunto_a.issubset(conjunto_b)
print(conjuntoissubset)'''

'''contatos = {
    'super': {'semen': 'gozo'},
    'gosto': {'penis': 'gozado'}
}
contatos['cheiro'] = 'porra'
print(contatos)

contatos['sememail'] = {'nome': 'seunome', 'telefone': '3333-3333'}
print(contatos)'''


# contatos = {
#     'Nome': {
#     'Telefone': '3333-3333',
#     'Email': 'seuemail@gmail.com'}}


# print(contatos.get('chave'))

# nome_contato = contatos['Nome']
# print(nome_contato)

# chave_contato = contatos.get('chave')
# print(chave_contato)

# chave_contato = contatos.get(
#     'chave',
#     'nao existe essa chave no dicionario por'
#     'favor reler o seu codigo seu imprestavel'
#     )
# print(chave_contato)
# contatos.pop('Nome')
# print(contatos)
# print(contatos.popitem())

# print('Telefone' in contatos['Nome'])

'''def exibir_nome(nome):
    print(f'ola mundo! ola {nome}')

exibir_nome(nome= input('diga o nome: '))'''
'''
def calcula(numeros):
    return sum(numeros)


print(calcula([10, 20]))

def retorna_ant_e_sucess(numero):
    ant = numero - 1
    suc = numero + 1
    print(ant, suc)


retorna_ant_e_sucess(40)'''


def carro_selecionado(marca, modelo, ano, placa):
    print(f'Carro selecionado com sucesso! {marca} {modelo} {ano} {placa}')


carro_selecionado(**{'marca': 'fiat', 'modelo': 'uno', 'ano': 2010, 'placa': 'abc-1234'})
