from tkinter import *
from tkinter import filedialog as FileD
from io import open
from tkinter import messagebox as MessagesBox

ruta = ""  # La utilizamos para almacenar a ruta del fichero


def nuevo():
    global ruta  # Para indicar que estamos cambiando la global la general
    mensaje.set("Creando...")
    ruta = ""
    texto.delete(1.0, "end")  # Que borre del caracter número uno al final, que bore lo que hay en texto
    root.title("NirVaNor")


def abrir():
    global ruta
    mensaje.set("Abriendo...")

    # Abrimos un diálogo para que el usuario seleccione un archivo de texto
    ruta = FileD.askopenfilename(initialdir=".",  # Directorio inicial
                                 filetypes=(("Ficheros de texto", "*.txt"),),  # Tipos de archivo permitidos
                                 title="Abrir un archivo de texto")  # Título del cuadro de diálogo

    # Si se selecciona un archivo, procedemos con el siguiente código
    if ruta != "":
        # Abrimos el archivo en modo lectura
        fichero = open(ruta, 'r')

        # Leemos todo el contenido del archivo y lo almacenamos en una variable llamada "contenido"
        contenido = fichero.read()

        # Borramos todo el contenido actual del widget de texto llamado "texto"
        texto.delete(1.0, "end")

        # Insertamos el contenido del archivo en el widget de texto "texto" desde el cursor actual (que será el inicio)
        texto.insert('insert', contenido)

        # Cerramos el archivo
        fichero.close()

        # Cambiamos el título de la ventana principal para incluir la ruta del archivo seleccionado
        root.title(ruta + "- NirVaNor")
        mensaje.set("El archivo se ha abierto correctamente")
    else:
        MessagesBox.showerror("Error", "No existe ese archivo o ocurrio otro error")
        mensaje.set("NirVaNor")


def guardar():
    global ruta
    mensaje.set("Guardando...")
    if ruta != "":  # Ya hay una ruta guardada anteriormente
        # Obtenemos todo el contenido del widget de texto desde el comienzo hasta el final
        contenido = texto.get(1.0, "end-1c")
        # Abrimos el archivo en modo escritura y lo sobrescribimos (w+) o lo creamos si no existe
        fichero = open(ruta, "w+")
        # Escribimos el contenido del widget de texto en el archivo
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El archivo se ha guardado correctamente")
        root.title(ruta + "- NirVaNor")
    else:
        guardarcomo()


def guardarcomo():
    global ruta
    mensaje.set("Guardando como...")
    mensaje.set("El archivo se ha guardado correctamente")
    # Abrimos un cuadro de diálogo para guardar el archivo con el título "Guardar Archivo", modo de escritura "w" y la extensión por defecto ".txt"
    fichero = FileD.asksaveasfile(title="Guardar Archivo", mode="w", defaultextension=".txt")

    # Si se selecciona un archivo, procedemos con el siguiente código
    if fichero is not None:
        # Obtenemos la ruta del archivo seleccionado
        ruta = fichero.name

        # Obtenemos todo el contenido del widget de texto desde el comienzo hasta el final, excepto el último carácter que es un salto de línea
        contenido = texto.get(1.0, "end-1c")
        fichero = open(ruta, "w+")

        # Escribimos el contenido del widget de texto en el archivo
        fichero.write(contenido)
        fichero.close()
        root.title(ruta + "- NirVaNor")

    else:
        MessagesBox.showerror("Error", "Ocurrio otro error")
        mensaje.set("NirVaNor")
        ruta = ""


root = Tk()
root.title("NirVaNor")


# Menu Superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardarcomo)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

# Caja de texto central
texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Arial", 12))

# Monitor inferior para saber que esta sucediendo
mensaje = StringVar()
mensaje.set("Bienvenido a NirVaNor")
monitor = Label(root, textvariable=mensaje, justify="left")
monitor.pack(side="left")

root.config(menu=menubar)
root.mainloop()