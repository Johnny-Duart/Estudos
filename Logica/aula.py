pessoa = {}
while True:
    pessoa['nome'] = input("digite seu nome: ")
    if len(pessoa['nome']) < 3:
        print("dado invalido.")
        continue
    while True:
        pessoa['idade'] = int(input("digite sua idade: "))
        if pessoa['idade'] < 0 or pessoa['idade'] > 100:
            print("dado invalido.")
            continue
        while True: 
            pessoa['cpf'] = input("digite seu cpf: ")
            if len(pessoa['cpf']) != 11:
                print("dado invalido.")
                continue
            break
        break
    break
print(f'seu nome é: {pessoa['nome']}')
print(f'sua idade é: {pessoa['idade']}')
print(f'seu cpf é: {pessoa['cpf']}')
print(type(pessoa))