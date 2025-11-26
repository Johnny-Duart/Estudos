"""
Introdução
Vamos aprender sobre arquivos CSV, um formato de arquivo amplamente utilizado
para armazenar dados tabulares. CSV é a sigla para 'Comma Separated Values'
(valores separados por virgula)

Ler arquivos CSV:
python fornece um modulo chamado 'csv' para lidar facilmente com esse tipo de
arquivo csv
"""

import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent
try:
    with open(
        ROOT_PATH / "exemplo.csv", "w", newline="", encoding="utf-8"
    ) as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome", "idade"])
        escritor.writerow(["1", "Maria", "10"])
        escritor.writerow(["2", "Joao", "19"])
except Exception as exc:
    print(f"Erro ao executar o arquivo {exc}")
try:
    with open(ROOT_PATH / "exemplo.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(", ".join(row))
except Exception as exc:
    print(f"Nao foi possivel abrir o arquivo {exc}")
