"""
  Este es un script de Python que implementa un pequeño programa de gestión de clientes usando una base de datos
  en formato CSV, se ejecuta mediante la terminal con python3 run.py. El programa presenta un menú de opciones para
  que el usuario pueda listar, buscar, añadir, modificar o borrar clientes. Sus funciones son:

  limpiar_pantalla(): función que borra la pantalla.
  curp_valido(curp): función que recibe una CURP y devuelve un mensaje indicando si es válida o no.
  leer_texto(min, max, mensaje): función que recibe un mínimo, un máximo y un mensaje y devuelve un texto
  introducido por el usuario que se ajusta a los límites.

  Clientes: clase que representa una base de datos de clientes en formato CSV y que contiene las siguientes funciones:
  __init__(): función que inicializa la base de datos vacía.
  cargar(): función que carga la base de datos desde el archivo CSV.
  guardar(): función que guarda la base de datos en el archivo CSV.
  buscar(curp): función que busca un cliente en la base de datos a partir de su CURP y devuelve una instancia de
  la clase Cliente si lo encuentra o None en caso contrario.

  crear(curp, nombre, apellido): función que crea un nuevo cliente en la base de datos a partir de su CURP, nombre y
  apellido.

  modificar(curp, nombre, apellido): función que modifica un cliente existente en la base de datos a partir de su CURP,
  nombre y apellido.
  borrar(curp): función que borra un cliente existente en la base de datos a partir de su CURP.
  Cliente: clase que representa un cliente y que contiene los atributos curp, nombre y apellido, así como las funciones
  __str__() y __repr__(), que devuelven una representación en cadena del objeto.

  iniciar(): función que ejecuta el programa y presenta el menú de opciones al usuario. Depende de todas las funciones
  anteriores y de la clase Clientes y Cliente.
"""


import os
import helpers
import database as db


def iniciar():
    """
        Función que ejecuta el programa del Manager de Clientes.
        Permite listar, buscar, añadir, modificar y borrar clientes.
    """
    while True:
        helpers.limpiar_pantalla()

        print("=" * 50)
        print("{:^50}".format("Bienvenido"))
        print("=" * 50)
        print("{:<5} {:<25}".format("[1]", "Listar clientes"))
        print("{:<5} {:<25}".format("[2]", "Buscar cliente"))
        print("{:<5} {:<25}".format("[3]", "Añadir cliente"))
        print("{:<5} {:<25}".format("[4]", "Modificar cliente"))
        print("{:<5} {:<25}".format("[5]", "Borrar cliente"))
        print("{:<5} {:<25}".format("[6]", "Cerrar el Manager"))
        print("=" * 50)

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Los clientes encontrados en la Base de Datos son:\n")
            for cliente in db.Clientes.lista:
                print(cliente)

        if opcion == '2':
            print("Buscando un cliente...\n")
            curp = helpers.leer_texto(15, 15, "Inserte la CURP (EJEMPLO: AEMM666666MAS78): ").upper()
            cliente = db.Clientes.buscar(curp)
            if cliente:
                print(f"El cliente encontrado es: {cliente}")
            else:
                print("Cliente no encontrado.")

        if opcion == '3':
            print("Añadiendo un cliente...\n")

            # end

            # Comprobación de CURP válido
            while True:
                curp = input("Inserte la CURP (EJEMPLO: AEMM666666MAS78): ")
                es_valido, mensaje_validacion = helpers.curp_valido(curp, db.Clientes.lista)
                if es_valido:
                    break
                else:
                    print(mensaje_validacion)

            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 caracteres): ").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 carateres): ").capitalize()
            db.Clientes.crear(curp, nombre, apellido)

        if opcion == '4':
            print("Modificando un cliente...\n")
            curp = helpers.leer_texto(15, 15, "Inserte la CURP (EJEMPLO: AEMM666666MAS78):").upper()
            cliente = db.Clientes.buscar(curp)
            if cliente:
                nombre = helpers.leer_texto(2, 30, f"Nombre (de 2 a 30 caracteres) [{cliente.nombre}]: ").capitalize()
                apellido = helpers.leer_texto(2, 30, f"Apellido (de 2 a 30 carateres) [{cliente.apellido}]: ").capitalize()
                db.Clientes.modificar(cliente.curp, nombre, apellido)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")

        if opcion == '5':
            print("Borrando un cliente...\n")
            curp = helpers.leer_texto(15, 15, "Inserte la CURP (EJEMPLO: AEMM666666MAS78):").upper()
            print("Cliente borrado correctamente.") if db.Clientes.borrar(curp) else print("Cliente no encontrado.")

        if opcion == '6':
            print("Saliendo, gracias!...\n")
            break

        input("\nPresiona ENTER para continuar...")
