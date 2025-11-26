"""
Em python podemos escrever em arquivos:
usando a função write() ou writelines().
no entando temos que sempre abrir o arquivo no modo correto
"""

arquivo = open(
    r"C:\Users\jonat\Desktop\programas\python\Coisas minhas\manipulação de dados\teste.txt",
    "w",
    encoding="utf-8",
)

# write = escreve
# writelines = itera o str
arquivo.write("Ola mundo!\n")
arquivo.writelines("Python")
# funciona
arquivo.writelines(["\n", "escrevendo", "um", "texto", "\n"])
texto = ["espaçamento", "automatico", "isso", "é", "um", "teste" "\n"]
arquivo.writelines(" ".join(texto))
arquivo.writelines(
    " ".join(["eu", "estou", "escrevendo", "dentro", "do", "writelines"])
)
arquivo.close()
