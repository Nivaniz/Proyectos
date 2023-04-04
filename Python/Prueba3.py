texto = "Un día que el viento soplaba con fuerza#mira como" \
        " se mueve aquella banderola - dijo un monje#lo que se mueve es el viento - respondió otro monje#ni las banderolas ni el viento, lo que se mueve son nuestras mentes -dijo el maestro"
texto2 = ''

texto2 = texto.split('#')


def formatear_texto(lista):
    lista[0] = lista[0] + "..."
    print(lista[0])  # Toma la primera línea de la lista y le agrega un ...
    for i in range(1, len(lista)):  # Toma el tamaño de la lista comenzando en 1
        texto = lista[i].capitalize()  # Hace la primera mayuscula
        texto = "- " + texto  # Agrega el - al principo
        if i == len(lista) - 1:  # Cuándo sea la ultima línea va agregar el . al final
            texto = texto + "."
        print(texto)

formatear_texto(texto2)       