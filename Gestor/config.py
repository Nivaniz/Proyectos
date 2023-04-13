import sys

# Ruta por defecto del archivo CSV donde se guardan los datos de los clientes
DATABASE_PATH = 'clientes.csv'

# Si se está ejecutando con pytest, usar una ruta de prueba en lugar de la ruta por defecto
if 'pytest' in sys.argv[0]:
    DATABASE_PATH = 'tests/clientes_test.csv'

"""
Módulo que contiene la configuración de la base de datos para el manejo de los clientes.

Variables:
- DATABASE_PATH: ruta del archivo CSV donde se guardan los datos de los clientes. 
  Por defecto, su valor es 'clientes.csv', pero si se está ejecutando con pytest, se cambia a 'tests/clientes_test.csv'.

"""
