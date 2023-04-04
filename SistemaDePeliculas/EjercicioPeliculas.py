# Creamos un sistema de películas que no se borra

from io import open
import pickle


class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:
    peliculas = []

    # Constructor de clase
    def __init__(self):
        # Cargar las películas del fichero
        self.cargar()

    def agregar(self, p):
        self.peliculas.append(p)
        self.guardar()  # Para guardarlas en el fichero

    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catalogo esta vacío")
            return
        for p in self.peliculas:
            print(p)

    def cargar(self):
        fichero = open('Catalogo.pckl', 'ab+')  # Append binario con funciones de lectura
        fichero.seek(0)  # Ya que va cargar varias veces tenemos que regresar el puntero

        # Buscamos si hay películas
        try:
            self.peliculas = pickle.load(fichero)  # Se cargan y leen datos al fichero
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se han cargado {} películas".format(len(self.peliculas)))

    def guardar(self):
        fichero = open('Catalogo.pckl', 'wb')
        pickle.dump(self.peliculas, fichero)  # guarda un objeto serializado de Python self.peliculas
        fichero.close()

        # Destructor de clase

    def __del__(self):
        self.guardar()
        print("Se ha guardado el fichero")


# Crear una instancia de la clase Catálogo
CINEMEX = Catalogo()  # Para crearlo

# Agregar una película al catálogo
CINEMEX.agregar(Pelicula("El padrino", 175, 1972))
CINEMEX.agregar(Pelicula("El padrino 2", 202, 1974))

# Mostrar todas las películas del catálogo
CINEMEX.mostrar()

# Guardar los datos en el archivo antes de salir del programa
CINEMEX.guardar()

# Borramos
del CINEMEX

print("_______________________________________")
# Ya se guardaron las dos películas
CINEMEX = Catalogo()
CINEMEX.mostrar()