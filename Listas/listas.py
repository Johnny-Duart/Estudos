#             0           1  <- 2 elementos!!
lista = [int('2'), str('semen')]
print(type(lista))
print(lista)
print(lista[0])
print(lista[1])

lista = [True, 'como coco', 3.14, False, 69]
print(type(lista[0]))
print(type(lista[1]))
print(lista)
print(lista[-1]) # o index negativo faz "voltar", como se fosse uma roda, entao o 0 é o True e o -1 seria o 69 pq ele foi pro ultimo
print(lista[-2])
print(type(lista[-1]))