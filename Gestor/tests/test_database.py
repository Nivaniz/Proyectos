""" Importamos el módulo unittest y el módulo que contiene
 el código que queremos probar"""

import copy
import unittest
import database as db
import helpers
import csv
import config

# Creamos una clase para nuestras prueba


class TestDatabase(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba
        db.Clientes.lista = [
            db.Cliente('VLJP14041940MELORJF62', 'Marta', 'Pérez'),
            db.Cliente('NMXJ11111952HADJPFV11', 'Ana', 'Mariana'),
            db.Cliente('BYLG18051991MRAAEXR87', 'Ana', 'García')
        ]

    def test_buscar_cliente(self):
        """
            Prueba que el método buscar retorne un cliente existente y que retorne None si el cliente no existe.
        """
        cliente_existente = db.Clientes.buscar('BYLG18051991MRAAEXR87')
        cliente_no_existente = db.Clientes.buscar('BYLG18051991MRAAEXR88')
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_no_existente)

    def test_crear_cliente(self):
        """
            Prueba que el método crear agregue un nuevo cliente a la lista de clientes y que los datos sean los correctos.
        """
        nuevo_cliente = db.Clientes.crear('YCJK05041914MVLWYAF03', 'Yamileth', 'Jarana')
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.curp, 'YCJK05041914MVLWYAF03')
        self.assertEqual(nuevo_cliente.nombre, 'Yamileth')
        self.assertEqual(nuevo_cliente.apellido, 'Jarana')

    def test_modificar_cliente(self):
        """
           Prueba que el método modificar cambie los datos de un cliente existente y mantenga los demás datos intactos.
        """
        cliente_a_modificar = copy.copy(db.Clientes.buscar('NMXJ11111952HADJPFV11'))
        cliente_modificado = db.Clientes.modificar('NMXJ11111952HADJPFV11', 'Mariana', 'Pérez')
        self.assertEqual(cliente_a_modificar.nombre, 'Ana')
        self.assertEqual(cliente_modificado.nombre, 'Mariana')

    def test_borrar_cliente(self):
        """
            Prueba que el método borrar elimine un cliente existente de la lista de clientes.
        """
        cliente_borrado = db.Clientes.borrar('BYLG18051991MRAAEXR87')
        cliente_rebuscado = db.Clientes.buscar('BYLG18051991MRAAEXR87')
        self.assertNotEqual(cliente_borrado, cliente_rebuscado)

    def curp_valido(self):
        """
            Prueba unitaria que verifica si la función 'curp_valido()' del módulo 'helpers' funciona correctamente.

            La prueba realiza las siguientes acciones:
            1. Verifica que una CURP válida (en este caso, 'AEMM666666MAS78') se considera como válida por la función.
            2. Verifica que una CURP inválida (en este caso, 'AEMM666666MAS7') se considera como inválida por la función.
            3. Verifica que una CURP inválida (en este caso, 'AEMM666666MWS77') se considera como inválida por la función.
            4. Verifica que una CURP inválida (en este caso, 'AEMM666666hAS7&') se considera como inválida por la función.

            Si la prueba es exitosa, significa que la función 'curp_valido()' funciona correctamente.
        """
        self.assertTrue(helpers.curp_valido('AEMM666666MAS78', db.Clientes.lista))
        self.assertFalse(helpers.curp_valido('AEMM666666MAS7', db.Clientes.lista))
        self.assertFalse(helpers.curp_valido('AEMM666666MWS77', db.Clientes.lista))
        self.assertFalse(helpers.curp_valido('AEMM666666hAS7&', db.Clientes.lista))

    def test_escritura_csv(self):
        """
          Prueba unitaria que verifica si los cambios realizados en los datos de los clientes se guardan correctamente
          en el archivo CSV correspondiente.

          La prueba ejecuta las siguientes acciones:
          1. Borra dos clientes de la base de datos.
          2. Modifica los datos de un cliente existente en la base de datos.
          3. Lee la primera línea del archivo CSV donde se guardan los datos de los clientes.
          4. Comprueba que la primera línea leída del archivo contiene los datos del cliente modificado.

          Si la prueba es exitosa, significa que los cambios realizados se han guardado correctamente en el archivo CSV.
        """
        db.Clientes.borrar('VLJP14041940MELORJF62')
        db.Clientes.borrar('NMXJ11111952HADJPFV11')
        db.Clientes.modificar('BYLG18051991MRAAEXR87', 'Mariana', 'Pérez')

        curp, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH, newline="\n", encoding="utf-8") as fichero:
            reader = csv.reader(fichero, delimiter=";")
            curp, nombre, apellido = next(reader)  # Primera línea del iterador

        self.assertEqual(curp, 'BYLG18051991MRAAEXR87')
        self.assertEqual(nombre, 'Mariana')
        self.assertEqual(apellido, 'Pérez')


# Ejecutamos las pruebas
if __name__ == '__main__':
    unittest.main()
