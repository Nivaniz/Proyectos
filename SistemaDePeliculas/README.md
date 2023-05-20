## Sistema de Películas

Este proyecto es un sistema de manejo de películas simple que sirve modificando el código y desde la terminal. Utilizando Python y un modulo import pickle. Puedes:

- Crear un catálogo.

- Agregar el nombre de la película, duración y año de lanzamiento a este catálogo.

- Mostrar todas las películas del catálogo.

- Guardar los datos en el archivo antes de salir del programa.

- Y al regresar al programa las películas anteriormente registradas estaran ahí.

# Ejemplo:

```python
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

# Ya se guardaron las dos películas
CINEMEX = Catalogo()
CINEMEX.mostrar()
```

## Instalación

Para poder utilizar el proyecto o modificarlo puedes:

1.- **Clonar el repositorio:**
`git clone https://github.com/Nivaniz/Proyectos.git`
*(Hay que especificar la carpeta para este proyecto)*

2.- **Navegar en el directorio del proyecto:**
`cd Gestor`

### Autoría

Creado por **Nirvana Belen González López**
