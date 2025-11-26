lista = ["busco", "amor ", "reciproco"]
for x in range(len(lista)):
    print(x, lista[x])
"""texto = 'super, homem'
lista = list(texto)
print(lista) # a str esta sendo iterada, sendo escritas de forma separada
texto = texto.split() #voce pode colocar coisas para ele nao considerar aqui
print(texto)
texto = 'jonathan@gmail.com'
lista = list(texto)
texto = texto.split('@') # da para separar o conteudo antes e apos o @, deixando mais facil a leitura de endereços
print(texto)"""
print(lista)
lista.append("super heroi")
print(lista)
lista.remove("homem")
print(lista)
lista.insert(3, "Super macaco")
print(lista)
lista.append(["homem", "super heroi"])
print(lista)
lista.extend(["homem", "super heroi"])
print(lista)
lista.remove(["homem", "super heroi"])  # remove as palavras chaves
print(lista)
lista.pop(
    0
)  # remove o elemento do index 0 e o primeiro index (0) passa pro proximo 'vacalo' passa a ser o index 0
print(lista)
del lista[
    0
]  # deleta o elemento do index 0 e o primeiro index (0) passa pro proximo 'super heroi'
print(lista)
lista.sort()  # ordena em alfabetica priorizando letras maisculas
print(lista)
lista.sort(key=str.lower)  # CONSIDERA tudo sendo minusculo (nao torna)
print(lista)
lista.sort(
    reverse=True
)  # faz a lista começar de tras pra frente (nao deixa em alguma ordem, so faz ficar de tras pra frente)
print(lista)
lista.clear()
print(lista)
