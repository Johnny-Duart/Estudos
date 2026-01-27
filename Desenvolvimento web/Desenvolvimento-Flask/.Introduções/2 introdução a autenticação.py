"""
Entendendo autenticação e autorização:

Autenticação e autorização sao dois conceitos cruciais na segurança
de APIs RESTful. Embora frequentemente usados de forma intercambiavel
eles se referem a processos distintos'1


Autenticação:

Refere-se ao processo de verificar a identidade de um usuario.
é como um sistema reconhece quem voce é. isso geralemtne é feito
atraves de um nome de usuario e senha, mas tabem pode incluir outros metodos
como tokens ou impressoes digitais.


Autorização:

Apos a autenticação. a autorização determina quais recursos
um usuario autenticado tem permissao para acessar. basicamente é
sobre o que voce esta autorizado a fazer. por exemplo um usuario
administrador pode ter acesso a mais funcionalidades em comparação com um
usuario comum


JWT (JSON Web Tokens):

JSON Web Tokens (JWT) é um padrao aberto (RFC 7519) que define uma maneira
compacta e independente de transmitir informações de forma seguira entre partes
como um objeto JSON


Caracteristicas do JWT:

Compacto: pode ser enviado atraves de uma URL, paramentro ou POST ou no
cabecalho HTTP

Autocontido: a carga util contem todas as informações necessarias sobre o
usuario, evitando
a ncessidade de consultar o banco de dados mais uma vez
"""
