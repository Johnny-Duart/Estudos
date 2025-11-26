"""
Bloco with!
use o gerenciamento de contexto (context manager) com a declaração 'with'. o
gerenciamento de contexto permite trabalhar com arquivos de forma segura,
garantindo que sejam fechados corretamente, mesmo em casos de exceções
"""

from pathlib import Path

ROOT_PATH = Path(__file__).parent

with open(ROOT_PATH / "Boas praticas!", "r") as arquivo:
    print(arquivo.read())

"""
Verifique o arquivo!
é recomendado verificar se o arquivo foi aberto corretamente antes de executar
quaisquer operação de leitura ou gravação nele!
"""
try:
    with open(ROOT_PATH / "Boas praticas!", "w") as arquivo:
        arquivo.write("Eu estou escrevendo aqui para ler depois!")

except Exception as exc:
    print(f"Nao abriu o arquivo! {exc}")

"""
Use a codificação correta!
Certifique de usar a codificação correta ao ler ou gravar arquivos de texto. o
argumento 'encoding' da função open permite especificar a codificação
"""
try:
    with open(
        ROOT_PATH / "codificado utf-8", "w", encoding="utf-8"
    ) as arquivo:
        arquivo.write(
            """Estou codificando com utf 8! então temos alguns caracteres adicionais! ç~"""
        )
except Exception as exc:
    print(f"Nao abriu o arquivo! {exc}")

try:
    with open(
        ROOT_PATH / "codificado ascii", "w", encoding="ascii"
    ) as arquivo:
        arquivo.write(
            "Estou codificando com ascii! entao temos algumas limitacoes!"
        )
except Exception as exc:
    print(f"Nao abriu o arquivo! {exc}")


# arquivo.write("Nao vai rodar pois esta fora do bloco")
# print(arquivo.read()) nao vai ler
