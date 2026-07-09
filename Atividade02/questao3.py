def numeros_comum(lista1,lista2):
    lista_comum = []
    
    for numero in lista1:
        if numero in lista2:
            lista_comum.append(numero)
        
    return lista_comum

print(numeros_comum([0,2,8,9],[1,2,3,4,5]))
