from datetime import date


class Pessoa:
    def __init__(self, nome, data_nascimento):
        self._nome = nome
        self.data_nascimento = data_nascimento
        # o setter vai atribuir esse valor na variavel value

    def dias_vividos(self):
        return (date.today() - self.data_nascimento).days

    @property
    def nome(self):
        return self._nome.title()

    @nome.setter
    def nome(self, value):
        self._nome = value

    # getter
    @property
    def data_nascimento(self):
        return self._data_nascimento

    # setter
    @data_nascimento.setter
    def data_nascimento(self, value):
        if not isinstance(value, date):
            raise ValueError("data_nascimento deve ser um objeto do tipo date")
        self._data_nascimento = value


p1 = Pessoa("jonathan da silva duarte", date(2003, 11, 16))
print(p1.dias_vividos())
print(p1.nome)
# getter = quando queremos retornar uma variavel
# setter = quando queremos definir algo dentro da variavel
