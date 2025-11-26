lista = ["Gustavo", "João", "Rebeca"]
lista.append(["Tiago", "Emilia"])
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
