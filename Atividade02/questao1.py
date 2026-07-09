def impares(lista_numeros):
    lista_impares = []
    for numero in lista_numeros:
        if numero % 2 !=0:
            lista_impares.append(numero)
    return lista_impares