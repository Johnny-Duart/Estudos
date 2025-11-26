"""
O que sao geradores?

Sao tipos especiais de iteradores, ao contrario de listas ou outros
iteraveis, não armazenam todos os seus valores na memoria.

Sao definidos usando funções regulares, mas, ao inves de retornar valores
sando "return" utilizam "yield".

iteradores armazenam toda a lista na memoria
geradores so mostram quando for pedido

uma vez que um item gerado é consumido, ele é esquecido
e nao pode ser acessado novamente

o estado interno de um gerador é mantido entre as chamadas

a execução de um gerador é pausada na declaração "yield"
e retomada dai na proxima vez que ele for chamado


recuperando dados de uma api

solicitar dados por paginas (paginação);

fornecer um produto por vez entre as chamadas.

quando todos os produtos de uma pagina forem retornados,
verificar se existem novas paginas

tratar o consumo da API como uma lista Python
"""

"""
import requests

def fetch_products(url, max_p=100):
    page = 1
    while page <= max_p:
        response = requests.get(f'{url}?page={page}')
        # get usado para buscar informações do servidor
        # nao altera nada, os dados vao pela url
        # post usado para enviar dados para o servidor
        data = response.json()
        for product in data["products"]:
            yield product
        if 'next_page' not in data:
            break

        page += 1


for product in fetch_products("https://api.example.com/products"):
    print(product['name'])
"""


def meu_gerador(numeros: list[int]):

    for numero in numeros:
        yield numero


for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)

"""
quando vamos usar um e quando vamos usar outro? depende
usar gerador:
quando se quer criar valores aos poucos
se quer econimizar na memoria
se quiser codigo curto

usar iteradores:
se precisar de logica mais estruturada
guardar o estado mais complexo
se quiser criar objetos personalizados que se comportam como listas
se quiser controlar o comportamento do iterador profundamente
"""
