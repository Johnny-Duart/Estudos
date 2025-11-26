"""
API RESTFUL é o grande foco do curso

introdução ao desenvolvimento web:
desenvolvimento web refere-se ao processo de criação de
websites e aplicações para a internet ou uma intranet.
Abrange uma variedade de tarefas, incluindo web desing,
programação web, gestao de banco de dados e engenharia de servidores

internet: informações publica
intranet: informações privadas

----

compontentes principais:

frontend: a parte do website que os usuarios interagem diretamente
envolve a criação de interfaces de usuarios e experciencias
usando tecnologias como HTML, CSS e JavaScript

backend: o 'bastidor' de um website, onde ocorrem o processamento de
dados, gerenciamento de banco de dados e controle de servidor;
envolve linguagens como Python, Java, Go, etc

frontend:
usuarios veem
20% da aplicação

backend:
usuarios nao veem
80% da aplicação

----

Como a web funciona
Internet vs Web:

A internet é uma rede global de computadores
interconectados. A web (ou World Wide Web), é um sistema de
informações construido sobre a internet que utiliza o protocolo
HTTP para transmitir dados

FTP = é usado para transferencia de arquivos
Telnet = é outro protocolo, que conecta remotamente a qualquer maquina
e envia comandos remotos a essa maquina

Protocolo HTTP

HTTP (Hypertext Transfer Protocol) é o protocolo fundamental
usado na web para transferencia de dados. Quando um
usuario acessa um site, o navegador envia uma solicitação
HTTP para o servidor do site, que responde com os dados do site

----

Funcionamento de um Website:
Solicitação do usuario: Tudo começa com o usuario inserindo um URL no
navegador ou clicando em um link

Resolução de DNS: O url é traduzido em um endereço IP atraves de um sistema
chamado DNS (domain name system)

Conexão com o servidor: O navegador utiliza o endereço IP para estabelecer
uma conexão com o servidor que hospeda o site

Resposta do servidor: O servidor processa a solicitação HTT`e envia de volta
os arquivos geralmente em HTML, CSS e JavaScript

Renderização no navegador: O navegador interpreta esses arquivos e exibe os
sites ao usuario

----

Tecnologias envolvidas:

Alem do HTML, CSS E JavaScript, tecnologias como SSL/TLS
para segurança, APIs para interatividade e banco de dados
para armazenamento de dados tambem desempenham um papel vital no funcionamento
da web

SSL/TLS = criptografia das informações

----

Frond-end: A interface do usuario

Front refere-se a parte do desenvolvimento web
que lida com a interface do usuario. O objeto é apresentar
informação de forma interativa e acessivel para o usuario final

----

Tecnologias chaves front-end:

HTML (Hypertext Markup Language): estrutura o conteudo
da web

CSS (Cascadin Style Sheets): Estiliza e apresenta o
conteudo HTML

JavaScript: Torna as paginas web interativas e dinamicas

----

Back-end: A logica por tras dos bastidores:

Back-end é a parte do site que o usuario nao ve. Inclui
servidor, aplicação e banco de dados. É responsavel por gerenciar e
processar dados, garantindo que tudo no front-end funcione corretamente

----

Linguagens e Tecnologias:

Linguagens: Python, Ruby, PHP, Java, Javascript, etc

Banco de dados: PostgreSQL, MySQL, MongoDB, Oracle, etc

Frameworks: Django (Python), Express (JavaScript), Spring Boot (Java)

----

Desenvolvimento Full Stack:

Desenvolvedores Full Stacks sao profissionais que tem
habilidades tanto em front-end quanto em back-end, sendo capazes
de trabalhar em ambas as areas do desenvolvimento web

----

O que é uma API?

API ou Interface de Programação de aplicações, é um conjunto
de regras e definições que permite que diferentes aplicações
de software ou componentes se comuniquem entre si;
Funciona como um intermediraio, permitindo que pedidos sejam feitos
e respostas sejam recebidas entre diferentes sistemas de software

----

API no contexto da Web

Na web as api sao usadas para permitir a interação entre diferentes serviços e
aplicações. como enviar dados de um usuario de um aplicativo para um servidor
ou solicitar dados de um serviço externo (por exemplo, redes sociais, mapas)

----

Importancias da API

As API sao cruciais para construção de aplicações modernas e escalaveis.
elas permitem a flexibilidade para integrar e expandir funcionalidades
sem reinventar a roda

----

Exemplo pratico:

Apis de pagamento: facilita transação de comercio
eletronioc atraves de diferentes plataformas de pagamentos

----

API RESTful

RESTful refere-se a APIs que seguem os principios REST
(Representational State Transfer). Sao baseadas em padroes
HTTP e utilizadas para interações web

----

Caracteristicas de API RESTful

Uso dos metodos HTTP (GET, POST, PUT, DELETE) para operações
CRUD (CREATE READ UPDATE DELETE)

Curva de aprendizado menor.

Facil de entender e implementar

----

API SOAP

SOAP (simple object access protocol) é o protocolo que
define um padrao para a troca de mensagens baseadas em XML

----

Caracteristicas de API SOAP

Protocolo baseado em XML para troca de informações

Idependente de linguagem e plataforma de transporte

Suporte para operações complexas e segurança avançada

----

API GraphQL

Uma linguagem de consulta para sua API, e um servidor capaz de
executar essas consultas, retornando apenas dados especificos

----

Caracteristicas de API GraphQL

Permite que os clientes especifiquem exatamente quais dados
querem

Eficiente na redução de solucitações e no tamanho dos dados
transferidos

Flexivel e fortemente tipada, facilitando a evolução de APIS

----

Escolhendo o tipo certo de API

A escolha depende das necessidades especificas do projeto,
dos recursos disponiveis e da expertise da equipe.

RESTful é popular pela simplicidade, SOAP é preferido para
segurança e transações complexas, enquanto GraphQL é ideal para aplicações
que requerem daddos dinamicos e personalizados

----

Verbos HTTP

Em APIs RESTful os verbos HTTP tem papeis especificos que
se alinham com as operações CRUD (CREATE, READ, UPDATE, DELETE)

Esta abordagem padronizada permite que as API sejam intuitivas e previsiveis
facilitando a interação entre diferentes sistemas e aplicações.

----

Convenções RESTful

GET para LEITURA, POST para CRIAÇÂO, PUT/PATCH para ATUALIZAÇÃO
e DELETE para remoção

Essas conveções sao fundamentais para o design de uma API RESTful bem projetada

"""
