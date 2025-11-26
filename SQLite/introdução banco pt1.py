"""
Vamos abordar conceitos basicos de banco de dados
e como podemos iteragir com eles usando a DB API em python

DB API é o que vai especificar como a linguagem vai conversar
com determinado banco de dados

----

O que é um banco de dados?

os bancos de dados sao coleções organizadas de dados,
geralmente armazenados e acessados eletronicamente a
partir de um sistema de computador

----

Tipos de bancos de dados:

Existem varios tipos de bancos de dados, incluindo relacionais
nao relacionais, orientados a objetos e muito mais. O tipo mais
comum é o banco de dados relacional, que organiza os dados em tabelas

----

E qual é o papel do SGBD?

Os Sistemas de Gerenciamento de Banco de Dados (SGBD) sao
softwares que interagem com o usuario, outras aplicações e o
proprio banco de dados para capturar e analisar os dados. Existem
muitos SGBDs dispponiveis no mercado, alguns dos mais populares incluem:
MySQL, PostgreSQL, SQLite, Oracle Database, Microsoft SQL server e MariaDB

----

Introdução aos bancos de dados relacionais:

Um banco de dados relacional é um tipo de banco de dados
ue organiza os dados em tabelas. Cada tabela é composta
de linhas, que representam registros individuais e colunas que
representam campos de dados

----

Tabelas

Em um banco de dados relacional, uma tabela é uma estrutura
que organiza os dados em linhas e colunas, semelhante a uma
planilha.

Cada linha representa um registro distinto e cada coluna representa
um tipo de informaçõa chamado de chamo, por exemplo
uma tabela 'Clientes' pode ter campos como 'ID', 'nome', 'email' e 'telefone'

campo nao é nada mais que uma informação que voce guarda sobre algo

----

Chaves primarias:

Cada tabela em um banco de dados relacional deve ter uma
chave primaria. A chave primaria é uma coluna (ou conjunto
de colunas) cujo valor é unico para cada registro. Isso garante
que cada registro da tabela possa ser indentificado de maneira unica;
Por exemplo na tabela 'Clientes', o campo 'ID' pode ser uma chave primaria

NO CASO:
PRIMARY KEY = VALOR UNICO + NAO NULO
UNICIDADE -> cada valor é unico
NAO PODE SER NULL
IDENTIFICA A LINHA DE FORMA EXCLUSIVA
"""
