def mayor(lista):
    return max(lista)

def menor(lista):
    return min(lista)

def ordenar(lista):
    if lista == []:
        return []
    return [(mayor(lista[0]), menor(lista[0]), menor(lista[0]) + mayor(lista[0]))] + ordenar(lista[1:])


print(ordenar([[143,12,1290], [1,2,14]]))