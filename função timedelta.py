import datetime

tipo_carro = input('''Escolha qual tipo de carro sera limpo
[P] = Pequeno
[M] = Medio
[G] = Grande: ''')

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.datetime.today()

if tipo_carro == 'P':
    data_estimada = data_atual + datetime.timedelta(minutes=tempo_pequeno)
    print(f'O tempo que o carro chegou foi: {data_atual.time()}, e o tempo '
          'estimado para a conclusao da limpeza é: {data_estimada.time()}')

elif tipo_carro == 'M':
    data_estimada = data_atual + datetime.timedelta(minutes=tempo_medio)
    print(f'O tempo que o carro chegou foi: {data_atual.time()}, e o tempo '
          'estimado para a conclusao da limpeza é: {data_estimada.time()}')

else:
    data_estimada = data_atual + datetime.timedelta(minutes=tempo_grande)
    print(f'O tempo que o carro chegou foi: {data_atual.time()}, e o tempo '
          'estimado para a conclusao da limpeza é: {data_estimada.time()}')
