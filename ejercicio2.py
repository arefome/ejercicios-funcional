def dividir_lista(lista):
    if lista == []:
        return []
    return [list(str(lista[0]))] + dividir_lista(lista[1:]) 


def multiplos(lista):
    if lista == []:
        return []
    return [[int(n)*3 for n in lista[0]]] + multiplos(lista[1:])


print(multiplos(dividir_lista([10,10,10])))

