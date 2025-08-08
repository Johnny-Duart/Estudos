list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print(list1, list2)
'''list1 = list1 + list2
print(list1)
list1.clear()
print(list1)
list1.extend(list2) # pode ser feito assim tambem, contatenando as listas
print(list1)'''
for x in list2:
    list1.append(x) 
print(list1)
lista2 = list1
print(lista2) #copia da list1 entao se fizermos isso
lista2.append('semen')
print(lista2, list1) # o semen é adicionado nas duas listas, porque qualquer alteração que acontecer em uma acontece em outra
#para conseguir receber elementos diferentes apos a copia das listas, podemos fazer
lista2 = list1.copy() # entao aqui ela vai copiar os elementos da list1 para a lista2, mas nao vao estar 'conectadas' entao
lista2.append('super')
list1.append('mijo')
print(lista2)
print(list1)# os valores sao diferentes