class Escola:
    escola = "DIO"

    def __init__(self, aluno, matricula):
        self.aluno = aluno
        self.matricula = matricula

    def __str__(self):
        return f"{self.aluno}, {self.matricula}, {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


adolfo = Escola("adolfo", 20)

mostrar_valores(adolfo)

adolfo.aluno = "Jose"

adolfo.matricula = 3

Escola.escola = "SuperHeroi"

jose = Escola("Adolfo", 3)

mostrar_valores(adolfo)
