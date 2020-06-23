def digitos(lista):
    if lista == []:
        return ""
    return str(lista[0])[-1] + digitos(lista[1:])

print(int(digitos([12,14,16,348])))