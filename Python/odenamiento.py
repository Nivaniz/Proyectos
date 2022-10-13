def Ordena (vector):
    aux = 0
    longitud_vector=len(vector)
    for i in range(0, longitud_vector):
        for n in range(0, longitud_vector):
            if vector[i] < vector[n]:
                aux = vector[n]
                vector[n] = vector[i]
                vector[i] = aux
                print(vector)
    
cumpleaños = [8, 11, 3, 29]
print(Ordena(cumpleaños))