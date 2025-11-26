import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_primeiro_banco_de_dados.db")
# agora vamos atribuir a variavel ao cursor.
# ele é o mais importante, pois ele faz enviar os comandos SQL,
# receber resultados e iterar dados retornados

cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def Criar_Tebela():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS clientes "
        "(id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "nome VARCHAR(100), email VARCHAR(150) UNIQUE)"
    )


"""
Criando valores, com o INSERT INTO (nome db) (elementos) VALUES (chaves)
"""


def Criar_Valores(data):
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()


"""
Alterando valores, com o UPDATE (nome db) SET (elemento ou elementos) WHERE(PK)
"""


def Alterar_Valores(data):
    cursor.execute(
        "UPDATE clientes SET nome = ?, email = ? WHERE id = ?", data
    )
    conexao.commit()


"""
Deletando Valores, com o DELETE FROM (nome db) WHERE (PK)
"""


def Deletar_Valores(data):
    cursor.execute("DELETE FROM clientes WHERE id = ?", data)
    conexao.commit()


"""
Criando muitos valores com função executemany
"""


def Criar_Muitos(dados):
    cursor.executemany(
        "INSERT INTO clientes (nome, email) VALUES (?,?)", dados
    )
    conexao.commit()


"""
O metodo 'fetchone()' é usado para recuperar um unico
registro de resultado. Ele terona o proximo registro na
lista de resultados ou 'None' se nao houver mais nenhum resultado
"""

"""
SEMPRE USAR TUPLAS, POIS SE USAR STR NORMAL OU INT DA ERRO
"""


def Recuperar_cliente(chave, seleciona):
    colunas_validas = {"id", "nome", "email"}

    if chave not in colunas_validas:
        raise ValueError("Coluna nao existente")

    texto = f"SELECT * FROM clientes WHERE {chave} = ?"
    print(dict(cursor.execute(texto, (seleciona,)).fetchone()))


"""
O metodo 'fetchall()' pode ser usado para recuperar todos os
registros de resultados de uma vez. Ele retorna uma lista de
registros ou uma lista vazia se nao houver mais resultados
"""


def Recuperar_Clientes(chave, seleciona):
    colunas_validas = {"id", "nome", "email"}

    if chave not in colunas_validas:
        raise ValueError("Coluna nao existente")

    texto = f"SELECT * FROM clientes WHERE {chave} = ?"
    resultado = cursor.execute(texto, (seleciona,)).fetchall()
    for linha in resultado:
        print(dict(linha))


def Listar_Clientes():
    linha = cursor.execute("SELECT * FROM clientes ORDER BY id")
    for row in linha:
        print(dict(row))


# print(cursor.execute("SELECT * FROM clientes").fetchall())

# dados = [("Zezinho", "zezinho@gmail.com"),
# ("Roberto", "robertinho@gmail.com")]
# cursor.execute("DROP TABLE clientes")
Criar_Valores(("Robson", "robsonxx@gmail.com"))
# Alterar_Valores(("Maria", "mariagames@gmail.com", "2"))
# Deletar_Valores("3")
# Criar_Muitos(dados)
# Recuperar_cliente("nome", "Jonathan")
# Recuperar_Clientes("nome", "Jonathan")
# Listar_Clientes()
