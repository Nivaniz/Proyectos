#Algorotimo que busca el valor minimo de una lista
def BuscaMinimo(lista):
    menor = lista[0];
    longitud = len(lista)
    for i in range(1, longitud):
        if lista[i] < menor:
            menor = lista[i]
    return menor
lista = [10, 5, 22, 1, 42]
print("El valor minimo de la lista es ", BuscaMinimo(lista))