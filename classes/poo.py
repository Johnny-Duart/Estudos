class Escola:
    escola = 'DIO'

    def __init__(self, aluno, matricula):
        self.aluno = aluno
        self.matricula = matricula

    def __str__(self):
        return f'{self.aluno}, {self.matricula}, {self.escola}'


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


adolf = Escola('adolf', 20)

mostrar_valores(adolf)

adolf.aluno = 'Hitler'

adolf.matricula = 3

Escola.escola = 'SuperSemen'

hitler = Escola('Hitler', 3)

mostrar_valores(adolf)