"""01 - Escreva um programa que leia 5 valores e encontre o maior e o menor deles. Mostre o
resultado"""

n1, n2, n3, n4, n5 = map(
    int, input("Digite 5 números separados por espaço: ").split()
)
if n1 > n2 and (n1 > n3) and (n1 > n4) and (n1 > n5):
    print("n1 numero maior")
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print("n2 é o maior número")
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    print("n3 é o maior número")
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    print("n4 é o maior número")
else:
    print("n5 numero maior")
numeros = n1, n2, n3, n4, n5
menor = min(numeros)
print(menor)
