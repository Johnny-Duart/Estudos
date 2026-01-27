"""
Objetivo geral:

Entender como o framework Flask funciona, desenvolvendo
uma API REST completa. Iremos realizar itegração com
banco de dados, escrever testes unitarios e conversar sobre como
empregar as boas praticas na escrita de apps Flask

Flask = mais flexivel porem nao indicado para projetos grandes

----

Endpoint e roteamento
"""

"""
@app.route("/")
def hello_world():
    return "<p>Hello, World<p/>"


# criando rodas
@app.route("/meusite")
def meu_site():
    return "<h1>Meu site<h1/>"
"""

# criando variaveis no site
# @app.route("/formulario/<nome>")
# def formulario(nome):
#    return f"""<p>Fomulario:<p/>
#    <label for="name">Nome<label/>
#    <p>{nome}<p/>"""


# usamos o tipo da (variavel):(nome da variavel) para forçar
# a variavel ficar nesse tipo
"""@app.route("/formulario_forcado/<string:nome>/<int:idade>")
def formulario_forcado(nome, idade):
    print(type(nome))
    print(type(idade))"""
# return f"""nome: {nome} <br>
# idade: {idade}"""

"""
# se colocar outros valores como nesse caso idade, temos que colocar outra /
# na url para funcionar, e apos essa / tem que ter os valores desejados


# url redirecionada vs url unica
# url redirecionada:
@app.route("/redirecionamento/")
def redirecionamento():
    return "Se nao colocar / no final da url mesmo assim vai ser redirecionado"

# url unica:
@app.route("/unica", methods=["POST", "GET"])
def unica():
    if request.method == "POST":
        return "Voce esta no metodo POST"
    elif request.method == "GET":
        return "Voce esta no metodo GET"
    else:
        return "Se colocar / no final ele retorna erro"


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    return f"subpath {subpath}"


with app.test_request_context():
    print(url_for("hello_world"))
    print(url_for("meu_site"))
    print(url_for("formulario", nome="Jonathan"))
    print(url_for("formulario_forcado", nome="Jonathan", idade="22"))
    print(url_for("redirecionamento"))
    print(url_for("unica"))
    print(url_for("show_subpath", subpath="ScreenShot00006.png"))
"""
"""
Em FLASKAPI um dicionario se torna json
"""

"""
@app.route("/json/<string:nome>/<int:idade>")
def dicionario(nome, idade):
    return {"chave": "valor", "Nome": nome, "idade": idade}
"""
