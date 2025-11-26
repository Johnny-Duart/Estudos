"""fatorial é quando voce faz um numero X multiplicar ate encontrar o valor 1,
exemplo: 9! vai ser 9x8x7x6x5x4x3x2x1 = 362.880
exceto 0! que é = 1
1! = 1"""

fatorial = 1
numero = int(input("Insira um numero para ser fatorado: "))

if numero < 0:
    print("Nao existem numeros negativos")
elif numero == 0:
    print("Seu numero é: 1")
else:
    for x in range(1, numero + 1):
        fatorial *= x
print(f"seu numero é: {fatorial}")
