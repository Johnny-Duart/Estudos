import os
# import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# os.mkdir(ROOT_PATH / 'novo diretorio')

arquivo = open(ROOT_PATH / "novo-texto.txt", "w")
arquivo.write("Arquivo criado pelo ROOT_PATH")
arquivo.close()
# os.rename(ROOT_PATH / 'novo diretorio', ROOT_PATH /
# 'novo diretorio atualizado')
# os.rmdir(ROOT_PATH / 'novo diretorio atualizado')

# shutil.move(ROOT_PATH / 'novo-texto.txt', ROOT_PATH.parent / 'Sets')
# ROOT_PATH = ROOT_PATH.parent / 'Sets'
# os.remove(ROOT_PATH / 'novo-texto.txt')

os.remove(ROOT_PATH / "novo-texto.txt")
