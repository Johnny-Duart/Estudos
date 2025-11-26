"""
Trabalhando com arquivos em python, podemos ter diversos
erros:
os mais comuns:
FileNotFoundError: quando o arquivo nao é encontrado
PermissionError: quando tenta abrir um arquivo sem permissao
IOError: um erro geral de E/S (entrada/saida), falta de espaço no disco
UnicodeDecodeError: erro ao tentar decodificar os dados de um texto com
codificação inadequada
UnicodeEncodeError: erro ao tentar codificar dados de uma determinada
codificação ao gravar em um arquivo
IsADirectoryError: Erro ao tentar abrir um diretorio em vez de um arquivo de
texto

UnicodeDecodeError = Erro de leitura
UnicodeEncodeError = Erro de gravação
"""

try:
    arquivo = open(
        "C:\\Users\\jonat\\Desktop\\programas\\python\\Coisas minhas\\manipulação de dados\\novo diretorio"
    )
except IsADirectoryError as exc:
    print(f"é um diretorio {exc}")
except FileNotFoundError as exc:
    print(f"arquivo nao encontrado {exc}")
except PermissionError as exc:
    print(f"Permissoes negadas {exc}")
except IOError as exc:
    print(f"Falta de memoria {exc}")
except UnicodeDecodeError as exc:
    print(f"erro de leitura {exc}")
except UnicodeEncodeError as exc:
    print(f"erro de gravação {exc}")
