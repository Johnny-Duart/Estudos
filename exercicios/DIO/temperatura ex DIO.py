temperaturas_celsius = input().split(",")


# função chamada converter_celsius_para_fahrenheit que recebe uma lista de strings
def converter_celsius_para_fahrenheit(temperaturas_celsius):

    lista_temperatura = []
    for temp in temperaturas_celsius:
        temp = float(temp)
        temperaturas_fahrenheit = (temp * 9 / 5) + 32
        lista_temperatura.append(temperaturas_fahrenheit)
    return lista_temperatura


# Imprime o resultado das temperaturas convertidas para Fahrenheit.
print(converter_celsius_para_fahrenheit(temperaturas_celsius))
