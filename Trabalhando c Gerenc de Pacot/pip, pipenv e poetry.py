"""
o que sao pacotes em python?
sao modulos que podem ser instalados e utilizados em
seus programas python. eles permitem que voce utilize o codigo
que foi escrito por outras pessoas, economizando tempo e esforço

pip é o gerenciador de pacotes do pythom ele permite instalar, atualizar
e remover pacotes facilmente. Ele se comunica com o PyPI (python package index)
que é onde a maioria dos pacotes estao

os comandos sao:
pip install (biblioteca) (biblioteca)
pip uninstall (biblioteca) (biblioteca)
pip list

pip install instala as bibliotecas, podendo instalar
mais de uma simuntaneamente

pip uninstall é para desinstalar, tambem podendo desinstalar
mais de uma simuntaneamente

pip list é para listar as bibliotecas instaladas


para ver todos os comandos disponiveis do pip
é so digitar:
pip
no powershell

alguns pacotes precisam de outros pacotes para funcionar e chamamos isso
de dependencia aninhada, no caso:
começou um projeto A > dentro do projeto A tem dependencia de pacote B > e o
pacote B tem dependencia no C
entao no projeto o B é dependencia do A, e o C é dependente aninhada
(ou indireta) do A
"""

"""
pipenv:
é uma ferramenta de gerenciamento de pacotes
que combina a gestao de dependencias
com a criação de ambiente virutal para seus
projetos e adiciona/remove pacotes automaticamente do arquivo
Pipfile conforme voce instala e desinstala pacotes

ao usar o pipenv ele vai baixar o pacote e criar uma venv para aquele pacote,
e vai ser o nome da pasta com um hash

com o pipenv temos alguns comandos:
pipenv install (biblioteca)
pipenv uninstall (biblioteca)
pipenv lock
pipenv graph
pipenv clean (biblioteca)

esse lock serve para 'trancar' as informações da biblioteca em um arquivo .json
entao ele vai manter a versao e coisa do tipo

pipenv graph vai mostrar a lista das bibliotecas igual o pip list, porem ela
tambem mostra as dependencias aninhadas

o pipenv clean é para tirar as dependencias aninhadas
"""


"""
Poetry:
é outra ferramenta de gerenciamento de
dependencias para python que permite declarar
as bibliotecas que seu projeto depende
e gerencia (instala/atualiza/remove) essas
bibliotecas para voce. Ela tambem suporta empacotamento
e publicações de projetos no PyPI

os comandos basicos do poetry:
pip install poetry (instalando a biblioteca)

se ja existir projeto:
poetry init

se for criar um projeto:
poetry new (nome do projeto)

cd (nome do projeto)
poetry add (biblioteca)
poetry remove (biblioteca)
"""
