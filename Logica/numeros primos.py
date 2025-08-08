"""um numero primo é quando é so divisivel pelo mesmo ou por 1 onde o resto é 0"""
numero = int(input("Insira o seu numero: "))
if numero > 1:
    for x in range(2,numero):
        if(numero % x) == 0:
            print("Seu numero nao primo")
            break
    else:
            print("seu numero é primo")
else:
    print("numero é impar")
 