"""
Chaves estrangeiras:

Por exemplo em uma tabela 'Pedidos' podemos ter
um campo 'ClienteID' que seja uma chave estrangeira
apontando para a chave primaria da tabela 'Clientes'.
isso cria um relacionamento entre 'Pedidos' e 'Clientes',
permitindo que cada pedido seja associado a um cliente especifico

pode exisitr mais de uma chave estrangeira e chamamos de: 'chave composta'

sao com as chaves estrangeiras que relacionamos um dado com outro dado, e
esses dados sao armazenados em tabelas

----

Relacionamento entre tabelas:

os banocs de dados relacionais permitem estabelecer relações entre tabelas. As
relações podem ser 'um para um', 'um para muitos' ou 'muitos para muitos'
Essas relações permitem efetuar consultas complexas que
unem dados de varias tabelas

quando criamos uma relação 'muitos para muitos' ou 'n:m'
nao criamos uma foreing key em nenhuma das tabelas relacionadas
e sim criamos uma terceira tabela entao vamos dizer:
uma planilha de pets onde tem 2 pets, esta relacionada
a uma tabela pessoas onde tem 2 pessoas, as 2 pessoas
podem ser donas dos 2 pets, e os 2 pets podem ser donos
das 2 pessoas, entao fariamos um:
pets_pessoas
usuario_id  pet_id
1              1
2              1
1              2
2              2
"""
