def primos(lista_numeros):
    lista_primos = []
    for numero in lista_numeros:
        if numero % 2 != 0 and numero > 1:
            print("O número {} é primo".format(numero))
            lista_primos.append(numero)
        else:
            print("O número {} não é primo".format(numero))
    return lista_primos

print(primos([3, 5, 6, 8, 9]))
