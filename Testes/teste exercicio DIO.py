entrada = input()


def extrair_dominios(emails):
    # Separa os emails por ponto e vírgula
    lista_emails = emails.split(";")
    # TODO: Implemente a lógica necessária para extrair os domínios
    dominios = [emails.split("@")[1] for email in lista_emails]

    return dominios


# Imprime a lista de strings com os domínios
print(extrair_dominios(entrada))
