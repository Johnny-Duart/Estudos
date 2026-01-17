entrada = input()


def extrair_dominios(emails):
    # Separa os emails por ponto e vírgula

    lista_emails = emails.split(";")
    lista_dominios = []

    for email in lista_emails:
        dominio = email.split("@")[1]
        lista_dominios.append(dominio)

    dominios = lista_dominios

    return dominios


# Imprime a lista de strings com os domínios
print(extrair_dominios(entrada))
