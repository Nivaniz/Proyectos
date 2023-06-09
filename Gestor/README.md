# Gestor de Clientes

Este es un proyecto de Python que implementa un pequeño programa de gestión de clientes usando una base de datos
en formato CSV,  se puede ejecutar de varias maneras mediante la terminal, mediante una intefaz gráfica o mediante una API desarrollada en Uvicorn. El programa presenta un menú de opciones para que el usuario pueda listar, buscar, añadir, modificar o borrar clientes. **Se puede abordar más información en el archivo run.py.**

## Ejecución

Para poder ejecutar desde la terminal: `python3 run.py -t`

Para poder ejecutar desde la interfaz: `python3 run.py`

Para poder ejecutar desde la API: `pipenv run uvicorn api:app --reload`

## Instalación

Para poder utilizar el proyecto o modificarlo puedes:

1.- **Clonar el repositorio:**
`git clone https://github.com/Nivaniz/Proyectos.git`
*(Hay que especificar la carpeta de Gestor para este proyecto)*

2.- **Navegar en el directorio del proyecto:**
`cd Gestor`

3.- **Instalar las dependencias necesarias:**
`pip install -r requirements.txt`

## Uso

Para poder usar el proyecto puedes ejecutar la interfaz desde:
Para poder ejecutar desde la terminal: `python3 run.py -t`
Para poder ejecutar desde la interfaz: `python3 run.py`
Para poder ejecutar desde la API: `pipenv run uvicorn api:app --reload`

## Ejemplo de Uso

### API:
<div style="display: flex; flex-wrap: nowrap; justify-content: center;">
  <img src="https://github.com/Nivaniz/Proyectos/blob/main/Gestor/api.png" alt="API" style="width: 100%; max-width: 50%;">
</div>

### Interfaz:
<div style="display: flex; flex-wrap: nowrap; justify-content: center;">
  <img src="https://github.com/Nivaniz/Proyectos/blob/main/Gestor/interfaz.png" alt="Interfaz" style="width: 100%; max-width: 50%;">
</div>

Si tienes dudas del funcionamiento de una clase o función puedes agregar una línea de código como: 
`help(función/clase)` para saber más de ella o leer mi documentación.

El programa desde la interfaz se maneja mediante botones, aparecerán los clientes desde el archivo cvs, puedes
Crear Cliente, Modificar Cliente y Borrar Cliente. Todo esto se actualiza en el CVS permanentemente incluso después
de cerrarlo.

### Autoría

Creado por **Nirvana Belen González López** con el apoyo de **Héctor Costa Guzmán**
