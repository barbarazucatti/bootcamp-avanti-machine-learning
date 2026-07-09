def pessoas(lista_pessoas):
    return sorted(lista_pessoas, key=lambda x: x['nome'], reverse=False)


print(pessoas([{'nome': 'Carlos', 'idade': 25}, {'nome': 'Alberto', 'idade': 30}, {'nome': 'Betina', 'idade': 20}]))