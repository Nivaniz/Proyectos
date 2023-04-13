# Menú UI
from tkinter import *
from tkinter import ttk
import database as db
from tkinter.messagebox import askokcancel, WARNING
import helpers


class CenterWidgetMixin:
    def center(self):
        # Actualiza la ventana antes de obtener el ancho y la altura
        self.update()

        # Obtiene el ancho y la altura de la ventana
        w = self.winfo_width()
        h = self.winfo_height()

        # Obtiene el ancho y la altura de la pantalla
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()

        # Calcula las coordenadas para centrar la ventana
        x = int((ws / 2) - (w / 2))
        y = int((hs / 2) - (h / 2))

        # Establece la geometría de la ventana para que aparezca centrada
        self.geometry(f"{w}x{h}+{x}+{y}")


class CreateClientWindow(Toplevel, CenterWidgetMixin):
    """
    Ventana de creación de clientes.

    Esta clase representa una ventana de Tkinter que permite crear un cliente.
    Se asegura de que los datos ingresados sean válidos antes de permitir la
    creación del cliente.

    Attributes
    ----------
    crear : tkinter.Button
        Botón "Crear" que permite crear un nuevo cliente.
    curp : tkinter.Entry
        Entrada de texto que permite ingresar la CURP del cliente.
    nombre : tkinter.Entry
        Entrada de texto que permite ingresar el nombre del cliente.
    apellido : tkinter.Entry
        Entrada de texto que permite ingresar el apellido del cliente.
    validation_message : tkinter.Label
        Etiqueta que muestra un mensaje de validación para los campos de entrada.
    validaciones : list
        Lista que almacena los valores de validación de los campos de entrada.

    Methods
    -------
    build()
        Construye los widgets de la ventana.
    validate(event, index)
        Valida la entrada de texto de los campos de entrada.
    create_client()
        Crea un nuevo cliente a partir de los datos ingresados.
    close()
        Cierra la ventana.

    """
    def __init__(self, parent):
        """
        Inicializa la ventana.

        Parameters
        ----------
        parent : tkinter.Tk
            La ventana principal de la aplicación.
        """
        super().__init__(parent)
        self.title('Crear cliente')
        self.build()
        self.center()
        # Obligar al usuario a interactuar con la subventana
        self.transient(parent)
        self.grab_set()

    def build(self):
        """
        Construye los widgets de la ventana.
        """
        # Top frame
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        # Labels
        Label(frame, text="Inserte la CURP (EJEMPLO: AEMM666666MAS78): ").grid(row=0, column=0)
        Label(frame, text="Nombre (de 2 a 30 caracteres):").grid(row=0, column=1)
        Label(frame, text="Apellido (de 2 a 30 caracteres):").grid(row=0, column=2)

        # Entries
        curp = Entry(frame)
        curp.grid(row=1, column=0)
        curp.bind("<KeyRelease>", lambda ev: self.validate(ev, 0))
        nombre = Entry(frame)
        nombre.grid(row=1, column=1)
        nombre.bind("<KeyRelease>", lambda ev: self.validate(ev, 1))
        apellido = Entry(frame)
        apellido.grid(row=1, column=2)
        apellido.bind("<KeyRelease>", lambda ev: self.validate(ev, 2))

        # Add label for the validation message
        self.validation_message = Label(frame, text="")
        self.validation_message.grid(row=2, columnspan=3, padx=0, pady=10)

        # Bottom frame
        frame = Frame(self)
        frame.pack(pady=10)

        # Buttons
        crear = Button(frame, text="Crear", command=self.create_client)
        crear.configure(state=DISABLED)
        crear.grid(row=0, column=0)
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)

        # Create button activation
        self.validaciones = [False, False, False]  # False, False, False

        # Class exports
        self.crear = crear
        self.curp = curp
        self.nombre = nombre
        self.apellido = apellido

    def create_client(self):
        """
            Agrega un nuevo cliente a la lista de clientes y la base de datos.
            Cierra la ventana después de crear el cliente.
        """
        self.master.treeview.insert(
            parent='', index='end', iid=self.curp.get(),
            values=(self.curp.get(), self.nombre.get(), self.apellido.get()))
        db.Clientes.crear(self.curp.get(), self.nombre.get(), self.apellido.get())
        self.close()

    def close(self):
        """
           Destruye la ventana actual y actualiza el estado de la ventana principal.
        """
        self.destroy()
        self.update()

    def validate(self, event, index):
        """
            Valida la entrada del usuario para el widget que desencadenó el evento.
            Actualiza el mensaje de validación y el color de fondo del widget.
            Actualiza el estado del botón Crear si todas las validaciones son verdaderas.
        """
        valor = event.widget.get()
        valido = False
        if index == 0:
            mensaje = helpers.curp_valido(valor, db.Clientes.lista)[1]
            valido = helpers.curp_valido(valor, db.Clientes.lista)[0]
            if valido:
                event.widget.configure({"bg": "Green"})
                self.validation_message.config(text=mensaje)
            else:
                event.widget.configure({"bg": "Red"})
                self.validation_message.config(text=mensaje)
        if index == 1:
            if len(valor) <= 2:
                self.validation_message.config(text="El nombre debe ser mayor que dos")
                event.widget.configure({"bg": "Red"})
            elif len(valor) > 30:
                self.validation_message.config(text="Debe ser menor que 30")
                event.widget.configure({"bg": "Red"})
            else:
                valido = valor.isalpha()
                if valido:
                    event.widget.configure({"bg": "Green"})
                    self.validation_message.config(text="")
                else:
                    event.widget.configure({"bg": "Red"})
                    self.validation_message.config(text="El nombre solo puede contener letras")
        if index == 2:
            if len(valor) <= 2:
                self.validation_message.config(text="El apellido debe ser mayor que dos")
                event.widget.configure({"bg": "Red"})
            elif len(valor) > 30:
                self.validation_message.config(text="El apellido debe ser menor que 30")
                event.widget.configure({"bg": "Red"})
            else:
                valido = valor.isalpha()
                if valido:
                    event.widget.configure({"bg": "Green"})
                    self.validation_message.config(text="")
                else:
                    event.widget.configure({"bg": "Red"})
                    self.validation_message.config(text="El apellido solo puede contener letras")

        # Cambiar estado del botón con base en las validaciones
        self.validaciones[index] = valido
        self.crear.config(state=NORMAL if self.validaciones == [1, 1, 1] else DISABLED)


class EditClientWindow(Toplevel, CenterWidgetMixin):
    """
    Clase que representa la ventana de edición de clientes.
    """

    def __init__(self, parent):
        """
        Constructor de la clase.
        :param parent: Ventana padre.
        """
        super().__init__(parent)
        self.title('Modificar cliente')
        self.build()
        self.center()
        # Obligar al usuario a interactuar con la subventana
        self.transient(parent)
        self.grab_set()

    def build(self):
        """
           Método que construye la interfaz de la ventana.
        """
        # Top frame
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        # Labels
        Label(frame, text="Inserte la CURP (No editable): ").grid(row=0, column=0)
        Label(frame, text="Nombre (de 2 a 30 caracteres):").grid(row=0, column=1)
        Label(frame, text="Apellido (de 2 a 30 caracteres):").grid(row=0, column=2)

        # Entries
        curp = Entry(frame)
        curp.grid(row=1, column=0)
        nombre = Entry(frame)
        nombre.grid(row=1, column=1)
        nombre.bind("<KeyRelease>", lambda ev: self.validate(ev, 0))
        apellido = Entry(frame)
        apellido.grid(row=1, column=2)
        apellido.bind("<KeyRelease>", lambda ev: self.validate(ev, 1))

        # Set entries initial values
        cliente = self.master.treeview.focus()
        campos = self.master.treeview.item(cliente, 'values')
        curp.insert(0, campos[0])
        curp.config(state=DISABLED)
        nombre.insert(0, campos[1])
        apellido.insert(0, campos[2])

        # Add label for the validation message
        self.validation_message = Label(frame, text="")
        self.validation_message.grid(row=2, columnspan=3, padx=0, pady=10)

        # Bottom frame
        frame = Frame(self)
        frame.pack(pady=10)

        # Buttons
        actualizar = Button(frame, text="Actualizar", command=self.update_client)
        actualizar.grid(row=0, column=0)
        Button(frame, text="Cancelar", command=self.close).grid(row=0, column=1)

        # Create button activation
        self.validaciones = [1, 1]  # False, False, False

        # Class exports
        self.actualizar = actualizar
        self.curp = curp
        self.nombre = nombre
        self.apellido = apellido

    def update_client(self):
        """
        Método que actualiza un cliente en la base de datos y en la tabla de clientes de la ventana principal.
        """
        cliente = self.master.treeview.focus()
        # Sobreescribimos los datos de la fila seleccionada
        self.master.treeview.item(
            cliente, values=(self.curp.get(), self.nombre.get(), self.apellido.get()))
        db.Clientes.modificar(self.curp.get(), self.nombre.get(), self.apellido.get())
        self.close()

    def close(self):
        """
        Método que cierra la ventana.
        """
        self.destroy()
        self.update()

    def validate(self, event, index):
        """
            Método que valida los datos ingresados en los campos de entrada.
        """
        valor = event.widget.get()
        valido = False
        if index == 0:
            if len(valor) <= 2:
                self.validation_message.config(text="El nombre debe ser mayor que dos")
                event.widget.configure({"bg": "Red"})
            elif len(valor) > 30:
                self.validation_message.config(text="Debe ser menor que 30")
                event.widget.configure({"bg": "Red"})
            else:
                valido = valor.isalpha()
                if valido:
                    event.widget.configure({"bg": "Green"})
                    self.validation_message.config(text="")
                else:
                    event.widget.configure({"bg": "Red"})
                    self.validation_message.config(text="El nombre solo puede contener letras")
        if index == 1:
            if len(valor) <= 2:
                self.validation_message.config(text="El apellido debe ser mayor que dos")
                event.widget.configure({"bg": "Red"})
            elif len(valor) > 30:
                self.validation_message.config(text="El apellido debe ser menor que 30")
                event.widget.configure({"bg": "Red"})
            else:
                valido = valor.isalpha()
                if valido:
                    event.widget.configure({"bg": "Green"})
                    self.validation_message.config(text="")
                else:
                    event.widget.configure({"bg": "Red"})
                    self.validation_message.config(text="El apellido solo puede contener letras")

        # Cambiar estado del botón con base en las validaciones
        self.validaciones[index] = valido
        self.actualizar.config(state=NORMAL if self.validaciones == [1, 1] else DISABLED)


class MainWindow(Tk, CenterWidgetMixin):
    """
    La clase MainWindow define la ventana principal de la aplicación.

    Esta ventana contiene un Treeview que muestra la lista de clientes almacenados en la base de datos.
    También tiene botones para crear, modificar y borrar clientes.

    Atributos:
        treeview (ttk.Treeview): El widget Treeview que muestra la lista de clientes.
    """

    def __init__(self):
        """
        Constructor de la clase MainWindow.
        Configura la ventana, construye su interfaz de usuario y la centra en la pantalla.
        """
        super().__init__()
        self.title('Gestor de clientes')
        self.build()
        self.center()

    def build(self):
        """
        Construye la interfaz de usuario de la ventana principal.

        La interfaz contiene un Treeview que muestra la lista de clientes almacenados en la base de datos,
        así como botones para crear, modificar y borrar clientes.
        """
        # Top Frame
        frame = Frame(self)
        frame.pack()

        # Treeview
        style = ttk.Style()
        style.configure('Treeview', font=('SansSerif', 10))

        treeview = ttk.Treeview(frame, style='Treeview')
        treeview['columns'] = ('CURP', 'Nombre', 'Apellido')

        # Column format
        treeview.column("#0", width=0, stretch=NO)
        treeview.column("CURP", anchor=CENTER)
        treeview.column("Nombre", anchor=CENTER)
        treeview.column("Apellido", anchor=CENTER)

        # Heading format
        treeview.heading("#0", anchor=CENTER)
        treeview.heading("CURP", text="CURP", anchor=CENTER)
        treeview.heading("Nombre", text="Nombre", anchor=CENTER)
        treeview.heading("Apellido", text="Apellido", anchor=CENTER)

        # Scrollbar
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Assign scrollbar
        treeview.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=treeview.yview)

        # Fill treeview data
        for cliente in db.Clientes.lista:
            treeview.insert(
                parent='', index='end', iid=cliente.curp,
                values=(cliente.curp, cliente.nombre, cliente.apellido))

        # Pack
        treeview.pack()

        # Bottom Frame
        frame = Frame(self)
        frame.pack(pady=20)

        # Buttons
        Button(frame, text="Crear Cliente", command=self.create).grid(row=1, column=0, padx=10)
        Button(frame, text="Modificar Cliente", command=self.edit).grid(row=1, column=1, padx=10)
        Button(frame, text="Borrar Cliente", command=self.delete).grid(row=1, column=2, padx=10)

        # Export treeview to the class
        self.treeview = treeview

    def delete(self):
        """
        Borra el cliente seleccionado en el Treeview y en la base de datos.
        Pide confirmación antes de borrar al cliente.
        """
        cliente = self.treeview.focus()
        if cliente:
            campos = self.treeview.item(cliente, 'values')
            confirmar = askokcancel(
                title='Confirmación',
                message=f'¿Borrar a {campos[1]} {campos[2]}?',
                icon=WARNING)
            if confirmar:
                # remove the row
                self.treeview.delete(cliente)
                db.Clientes.borrar(campos[0])

    def create(self):
        """
        Crea una nueva ventana para agregar un nuevo cliente.
        """
        CreateClientWindow(self)

    def edit(self):
        """
        Abre una ventana de edición de clientes si se ha seleccionado
        previamente un cliente en el treeview.
        """
        if self.treeview.focus():
            EditClientWindow(self)


if __name__ == "__main__":
    """
    Código principal de la aplicación. Crea una instancia de la ventana
    principal y la muestra en pantalla.
    """
    app = MainWindow()
    app.mainloop()
