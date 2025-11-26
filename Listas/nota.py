notas = []
while True:

    nota = input("digite uma nota (ou sair para 'sair'): ")
    if nota.lower() == "sair":
        break
    notas.append(float(nota))
print(sum(notas) / len(notas))
