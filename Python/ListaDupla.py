matriz = [
    [8,  7,  0],
    [34, 2, -1],
    [5, -5, 12]
]

# Completa el ejercicio aquí
# Primero recorremos todas las filas de la matriz con un for
# Necesitamos usar un enumerador para poder guardar su índice de fila
for i, fila in enumerate(matriz):
    # Dentro de cada fila recorremos cada columna con otro for
    # Necesitamos usar un enumerador para poder guardar su índice de columna
    for j, columna in enumerate(fila):
        # A partir de ambos índices podemos comprobar la celda actual
        # Si es par asignamos a la celda un 0
        if matriz[i][j] % 2 == 0:
            matriz[i][j] = 0
        # En caso contrario, si es impar, le asignamos un 1
        else:
            matriz[i][j] = 1
print(matriz)