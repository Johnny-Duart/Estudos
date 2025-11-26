#            0     1    2       3       4       5           6
lista = [int(12), 23, 2.00, "cavalo", True, "bebo", 3.14]
print(
    lista[::]
)  # faz imprimir td o primeiro : é o inicio e o segundo é ate onde vai (o final)
print(lista[:3])  # no caso vai do inicio ate o index 3-1
print(lista[3:])  # no caso vai do index 3 ate o ultimo da lista
print(
    lista[2:2]
)  # como o segundo é sempre o index -1 entao ele nao retorna nada
print(lista[2:4])  # começando no 2 e indo ate o 3 pq é o index final -1
print(lista[2:6:2])  # começando no index 2 indo ate o 5 indo de 2 em 2
# slicing tambem funciona com string

nome = "chifre de elefante"
print(nome[0:10])
lista1 = [10]
lista2 = [20]
lista = (
    lista1 + lista2
)  # adiciona primeiro index sendo lista1, e apos isso adiciona o segundo index sendo lista2
print(lista)
lista = (
    lista2 + lista1
)  # adiciona primeiro index sendo lista2 e apos isso adiciona o seguindo index sendo lista1
print(lista)
lista = lista1 + lista1  # adiciona 2 index iduais
print(lista)
print(sum(lista))  # faz a soma dos valores

lista = lista2 + lista1
print(len(lista))  # retorna o tamanho da lista
print(max(lista))  # retorna o maior elemento
print(min(lista))  # retorna o menor elemento
lista = lista2 + lista1 + [13, 15]  # da para adicionar na lista outra lista
print(lista)
