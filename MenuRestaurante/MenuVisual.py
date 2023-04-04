import sqlite3
from tkinter import *
from PIL import Image, ImageTk

# Configuración de la raíz
root = Tk()
root.title("PESCATUS")

# Cargar la imagen y mostrarla en la ventana
imagen = Image.open("restaurante.png")
imagen = imagen.resize((int(root.winfo_screenwidth()/3), int(root.winfo_screenheight()/5)))
imagen = ImageTk.PhotoImage(imagen)
Label(root, image=imagen).pack()

# Cambiar el color de fondo de la ventana
root.config(bg="#f6f6f6")
root.config(bd=25, relief="sunken")

Label(root, text="Menú del día", fg="green", font=("Times New Roman", 24, "bold italic")).pack()

# Separación de títulos y categorias
Label(root, text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

# Buscar las categorías y platos de la bd
categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
    Label(root, text=categoria[1], fg="black", font=("Times New Roman", 20, "bold italic")).pack()

    platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
    for plato in platos:
        Label(root, text=plato[1], fg="gray", font=("Verdana", 15, "italic")).pack()

    # Separación entre categorias
    Label(root, text="").pack()

conexion.close()

# Precio del menú
Label(root, text="120 MXN (IVA incl.)", fg="darkgreen", font=("Times New Roman", 20, "bold italic")).pack(pady=10)

root.mainloop()
