import csv
import config


class Cliente:
    """
    Representa a un cliente registrado en el sistema.

    Atributos:
    ----------
    curp : str
        La clave única de registro de población del cliente.
    nombre : str
        El nombre del cliente.
    apellido : str
        El apellido del cliente.
    """

    def __init__(self, curp, nombre, apellido):
        """
        Crea un nuevo objeto Cliente.

        Parámetros:
        -----------
        curp : str
            La clave única de registro de población del cliente.
        nombre : str
            El nombre del cliente.
        apellido : str
            El apellido del cliente.
        """
        self.curp = curp
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        """
        Devuelve una representación en cadena de texto del objeto.

        Retorna:
        --------
        str
            Una representación en cadena de texto del objeto.
        """
        return f"({self.curp}) {self.nombre} {self.apellido}"


class Clientes:
    """
    Representa la colección de clientes registrados en el sistema.

    Atributos:
    ----------
    lista : list[Cliente]
        La lista de clientes registrados en el sistema.
    """

    lista = []

    with open(config.DATABASE_PATH, newline="\n", encoding="utf-8") as fichero:
        reader = csv.reader(fichero, delimiter=";")
        for curp, nombre, apellido in reader:
            cliente = Cliente(curp, nombre, apellido)
            lista.append(cliente)

    @staticmethod
    def buscar(curp):
        """
        Busca un cliente en la lista por su clave única de registro de población.

        Parámetros:
        -----------
        curp : str
            La clave única de registro de población del cliente a buscar.

        Retorna:
        --------
        Cliente or None
            El objeto Cliente correspondiente a la clave de registro proporcionada,
            o None si el cliente no se encuentra en la lista.
        """
        for cliente in Clientes.lista:
            if cliente.curp == curp:
                return cliente
        print("Cliente no encontrado")
        return None

    @staticmethod
    def crear(curp, nombre, apellido):
        """
        Crea un nuevo objeto Cliente y lo agrega a la lista de clientes.

        Parámetros:
        -----------
        curp : str
            La clave única de registro de población del nuevo cliente.
        nombre : str
            El nombre del nuevo cliente.
        apellido : str
            El apellido del nuevo cliente.

        Retorna:
        --------
        Cliente
            El objeto Cliente recién creado.
        """
        cliente = Cliente(curp, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente

    @staticmethod
    def modificar(curp, nombre, apellido):
        """
        Modifica el nombre y el apellido de un cliente existente en la lista.

        Parámetros:
        -----------
        curp : str
            La clave única de registro de población del cliente a modificar.
        nombre : str
            El nuevo nombre del cliente.
        apellido : str
            El nuevo apellido del cliente.

        Retorna:
        --------
        Cliente
            El objeto Cliente con los nuevos datos proporcionados.
        """
        for i, cliente in enumerate(Clientes.lista):
            if cliente.curp == curp:
                Clientes.lista[i].nombre = nombre
                Clientes.lista[i].apellido = apellido
                Clientes.guardar()
                return Clientes.lista[i]

    @staticmethod
    def borrar(curp):
        """
        Elimina un cliente de la lista de clientes.

        Parameters:
            curp (str): La CURP del cliente a eliminar.

        Returns:
            Cliente: El cliente eliminado, o None si no se encontró ningún cliente con esa CURP.
        """
        for i, cliente in enumerate(Clientes.lista):
            if cliente.curp == curp:
                cliente = Clientes.lista.pop(i)
                Clientes.guardar()
                return cliente

    @staticmethod
    def guardar():
        """
        Método estático que guarda los datos de los clientes en un archivo CSV llamado "clientes.csv".
        La lista de clientes a guardar se encuentra en el atributo estático "lista" de la clase Clientes.
        Los datos guardados por cada cliente son su CURP, nombre y apellido, separados por un punto y coma (;).
        """
        with open(config.DATABASE_PATH, "w", newline="\n", encoding="utf-8") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for c in Clientes.lista:
                writer.writerow((c.curp, c.nombre, c.apellido))
