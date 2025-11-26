# uma tupla é igual a lista porem nao é mutavel, e para se toranr mutavel tem que virar lista para depois se tornar tupla
tupla = "semen", "heroi"
print(type(tupla))
tupla = ("super", "heroi", "voador")  # podem ser feitos dessas duas maneiras
print(type(tupla))
print(tupla.count("voador"))  # mostra quantas vezes apareceu a palavra chave
# tuplas n é possivel adicionar elementos, nem excluir (imutavel)
# como nao é mutavel so da para reescrever as tuplas, se for necessario
tupla = ("super", True, 2, 5.3)
print(type(tupla[3]))
