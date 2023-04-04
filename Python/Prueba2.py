""" Buscar y borrar un cliente con POO """


class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)


class Empresa:

    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")

    def borrar_cliente(self, dni=None):
        for i, c in enumerate(self.clientes):
            if c.dni == dni:
                del (self.clientes[i])
                print(str(c), "> BORRADO")
                return
        print("Cliente no encontrado")


# Para generar un cliente
hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="GOCM1608")
juan = Cliente("MLNM1101", "Juan", "Gonzalez Marquez")

# Para crear la empresa y asignar clientes
empresa = Empresa(clientes=[hector, juan])

print(empresa.mostrar_cliente(dni="GOCM1608"))  # Para mostrar el cliente