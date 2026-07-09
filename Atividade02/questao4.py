

def maior_numero(lista_numeros):
    max_numero = 0
    for numero in lista_numeros:
        if numero > max_numero:
            max_numero = numero
    return max_numero

print(maior_numero([1,2,3,4,5,6,7,8,9]))