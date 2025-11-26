# adicionando na lista
lista = ["super", "heroi"]
lista.append("como assim")
print(lista)
lista = ["ambulancia", "ambulante"]
lista += "alo"
# assim ele vai ser 'nao' concatenado
print(lista)
lista[1] = "teste"  # troca o item do intex
lista[2] = "coco"
print(lista)
lista[1:3] = ["suculenta", "como"]  # troca os itens de 1 ao 2
print(lista)
lista[1:2] = [
    "super heroi",
    "comidaembalada",
]  # como so colocamos para trocar o segundo index no caso o
#'suculenta' e adicionamos mais de um index, ele nao apagou o outro e sim adicionou um a mais
print(lista)
print(
    lista[-5]
)  # é possivel printar index negativos, é como se ele voltasse, como se fosse um circulo
# print(lista[-8]) nao é possivel acessar elementos que nao existem
