def Ordenar(vector):
    longitud = len(vector)
    for i in range(longitud):
        for j in range(i, 0, -1):
            if(vector[j - 1] > vector[j]):
                aux = vector[j]
                vector[j] = vector[j - 1]
                vector[j - 1] = aux
    print(vector)
    
vector =  [4,67,8,20,23,9,12,22,84,111,51,124,72,78,13,57,42,140,98,48,1,167,291,64,18,47,16,200,65,34]
Ordenar(vector)