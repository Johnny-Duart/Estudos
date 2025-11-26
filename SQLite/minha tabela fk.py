import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_primeiro_banco_de_dados.db")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")


def Criar_Tabelas(cursor):
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS produtos (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, produto VARCHAR(100), id_cliente INTEGER, FOREIGN KEY (id_cliente) REFERENCES clientes(id));"
    )


def Criar_Valores(tabela, campos, quantidade, valores):
    tabelas_existentes = {"produtos", "clientes"}

    if tabela not in tabelas_existentes:
        raise ValueError("Tabela inexistente")

    texto = f"INSERT INTO {tabela} ({','.join(campos)}) VALUES ({quantidade})"
    cursor.execute(texto, valores)
    conexao.commit()


# cursor.execute("DROP TABLE produtos")


# Criar_Tabelas(cursor)
Criar_Valores("produtos", ("produto", "id_cliente"), "?, ?", ("Teclado", 3))
