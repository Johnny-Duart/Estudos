import moeda

p = float(input("Digite o preço R$: "))
print(f"a metade: {moeda.metade(p)}")
print(f"o dobro: {moeda.dobro(p)}")
print(f"o acrescimo: {moeda.aumentar(p, 10)}")
print(f"o desconto: {moeda.diminuir(p, 10)}")
