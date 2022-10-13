def mergeSort(alista):
    print("Divide", alista)
    if len(alista)> 1:
        mitad = len(alista)//2
        ladoIzquierdo = alista[:mitad]
        ladoDerecho = alista[mitad:]
        mergeSort(ladoIzquierdo)
        mergeSort(ladoDerecho)
        i = 0
        j = 0
        K = 0
        while i < len(ladoIzquierdo) and j < len(ladoDerecho):
            if ladoIzquierdo[i] < ladoDerecho[j]:
                alista[k] = ladoIzquierdo[i]
                i = i+1
            else:
                alista[k] = ladoDerecho[j]
                j = j+1
            k = k+1
        while i < len(ladoIzquierdo):
            alista[k] = ladoIzquierdo[i]
            i = i+1
            k = k+1
        while j < len(ladoDerecho):
            alista[k] = ladoDerecho[j]
            j = j + 1
            k = k+1
        print("Mezclando", alista)

alista = [38,47,23,3,9,82,10]
#alista = np.random.randint(100, size=50)
print("Lista original", alista)
mergeSort(alista)
