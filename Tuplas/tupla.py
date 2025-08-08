'''Estou aprendendo sobre tuplas,
então vou mandar futuramente esses arquivos para mim.
Relembrando que uma tupla não pode ser mutável.
Se quiser colocar outros atributos, só se for reescrita,
pois ela não permite adicionar elementos.
Não dá para usar append, insert e extend como em listas.'''

# Em listas podemos usar várias maneiras de unir índices, por exemplo:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

'''lista = lista1 + lista2
print(lista)
Colocando os valores da lista1 e depois da lista2 na variável lista
lista1.extend(lista2) Adicionando os valores da lista2 na lista1
lista1.extend([4, 5, 6]) Também podemos fazer assim
lista1 += [4, 6, 6] Funciona como extend
print(lista1)'''

# Criando uma tupla com as listas
tupla1 = (lista1, lista2)
print(tupla1)

# Tuplas são imutáveis
# mas podemos modificar elementos mutáveis contidos nelas (como listas):
tupla1[0].append(int(20))
print(tupla1)  # O elemento 'teste' foi adicionado dentro da lista lista1

# Criando outra tupla
tupla2 = 'super', 'mijo'
# Concatenando tuplas (tupla1 e tupla2) para criar tupla3
tupla3 = tupla1 + tupla2
print(tupla3)

# Contando quantas vezes o valor 1 aparece na tupla3
# (não conta dentro de listas):
print(tupla3.count(1))

# Modificando a lista lista1 e refletindo na tupla:
print(lista1)
lista1[0] = "alterado"
print(lista1)
print(tupla3)

# Convertendo tupla para lista e vice-versa:
lista4 = list(tupla3)
print(lista4)
tupla3 = tuple(lista4)
print(tupla3)

# Criando uma tupla com um único item (precisa da vírgula):
tupla1 = 'isso é uma variável string'
print(tupla1, type(tupla1))  # Aqui é só uma string
tupla1 = 'isso é uma tupla',
print(tupla1, type(tupla1))  # Agora é uma tupla

# Multiplicando tupla (repetição dos itens):
tupla1 = tupla1 * 3
print(tupla1)

# Percorrendo a tupla:
for x in tupla1:
    print(x)
for x in range(len(tupla1)):
    print(x)  # Exibindo os índices
for x in range(len(tupla1)):
    print(x, tupla1[x])  # Exibindo índice e valor correspondente

# Desempacotando uma tupla:
tupla1 = 'banana', 'alface', 'beterraba'
x, y, z = tupla1
print(tupla1, type(tupla1))
print(x, y, z)

# Não podemos desempacotar mais variáveis do que elementos na tupla.

# Exemplo com lista:
lista1 = ['suco', 'de', 'uva']
print(lista1, type(lista1))
x, *y = lista1  # O * captura o restante dos elementos em uma lista
print(x, y)

# Desempacotando com * para capturar os elementos intermediários:
tupla1 = 'banana', 'alface', 'beterraba', 'cafe'
x, *y, z = tupla1
print(tupla1, type(tupla1))
print(x, y, z)

# Pegando elementos específicos por índice:
tupla1 = 'banana', 'alface', 'beterraba', 'cafe'
x = tupla1[0]
y = [tupla1[1], tupla1[3]]
z = tupla1[2]
print(x, y, z)
