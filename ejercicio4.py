class Nodo():
	def __init__(self, valor, izquierda=None, derecha=None):
		self.valor = valor
		self.izquierda = izquierda
		self.derecha = derecha

def en_orden(arbol):
	if(arbol==None):
		return []
	return en_orden(arbol.izquierda) + [arbol.valor] + en_orden(arbol.derecha)

def dividir_lista(lista):
    if lista == []:
        return []
    return [list(str(lista[0]))] + dividir_lista(lista[1:]) 

print(dividir_lista(en_orden(Nodo(22,Nodo(13,None,Nodo(18)),Nodo(35)))))
