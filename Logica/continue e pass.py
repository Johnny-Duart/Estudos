for x in range(10):
    if x == 3 or x == 4:
        continue
    print(x)

if x == 5:
# se nao tiver "pass" aqui, ele vai dar erro de identação pois o print esta fora do if
# dito isso o "Pass" funciona para ignorar algo, o continue é para pular
    pass
print("Ola mundo")  