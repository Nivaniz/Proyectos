lista = [29, -5, -12, 17, 5, 2, 5, 12, 23, 16, 12, 5, -12, 17]

def modificar(l):
    l = list(set(l))  # ELIMINAR DUPLICADS
    l.sort(reverse = True)  # ORDENAR LA LISTA DE MAYR  MENOR
    for i in range(len(l))[::-1]:  # Va en orden al reves 9:0:-1
        if l[i]%2 != 0:  # VA TOMANDO CADA NUM
            del( l[i] ) # ELIMINAR NUMEROS IMPARES [16,12,2,-12]
    suma = sum(l)  # Realizar una suma de todos los números que quedan = 18
    l.insert(0, suma)  # Añadir como primer elemento de la lista la suma realizada
    # [18,16...]
    return l  # Devolver la lista modificada            
    
print(modificar(lista))