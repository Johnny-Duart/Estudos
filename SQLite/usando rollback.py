import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_primeiro_banco_de_dados.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def Transação(conexao, cursor, dados):
    try:
        cursor.execute(
            "INSERT INTO clientes (nome, email) VALUES (?, ?)", dados
        )
        conexao.commit()
    except Exception as exc:
        print(f"DEU ERRO DOG! {exc}")
        conexao.rollback()


Transação(conexao, cursor, ("Fake Do Jonathan", "jonathancraft12@gmail.com"))

