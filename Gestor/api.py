from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, constr, validator
import database as db
import helpers


# Definición del modelo de datos para un cliente
class ModeloCliente(BaseModel):
    curp: constr(min_length=15, max_length=15)
    nombre: constr(min_length=2, max_length=30)
    apellido: constr(min_length=2, max_length=30)


# Definición del modelo de datos para crear un nuevo cliente
class ModeloCrearCliente(ModeloCliente):
    @validator("curp")
    def validar_dni(cls, curp):
        # Validar la CURP del cliente utilizando una función auxiliar
        mensaje_error = helpers.curp_valido_api(curp, db.Clientes.lista)
        if mensaje_error:
            # Si la CURP no es válida, lanzar una excepción HTTP con un mensaje de error
            raise HTTPException(status_code=400, detail=mensaje_error)
        return curp


# Crear una instancia de la aplicación FastAPI
app = FastAPI(
    title="API del Gestor de clientes",
    description="Ofrece diferentes funciones para gestionar los clientes."
)


# Definir una ruta para obtener la lista de clientes
@app.get("/clientes/", tags=["Clientes"])
async def clientes():
    # Obtener la lista de clientes desde la base de datos y convertirlos a un formato adecuado para la respuesta
    content = [cliente.to_dict() for cliente in db.Clientes.lista]
    return JSONResponse(content=content)


# Definir una ruta para buscar un cliente por su CURP
@app.get("/clientes/buscar/{curp}/", tags=["Clientes"])
async def clientes_buscar(curp: str):
    # Buscar el cliente en la base de datos por su CURP
    cliente = db.Clientes.buscar(curp=curp)
    if not cliente:
        # Si el cliente no se encuentra, lanzar una excepción HTTP con un mensaje de error
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return JSONResponse(content=cliente.to_dict())


# Definir una ruta para crear un nuevo cliente
@app.post("/clientes/crear/", tags=["Clientes"])
async def clientes_crear(datos: ModeloCrearCliente):
    # Crear un nuevo cliente en la base de datos utilizando los datos proporcionados
    cliente = db.Clientes.crear(datos.curp, datos.nombre, datos.apellido)
    if cliente:
        # Si se crea correctamente, devolver el cliente creado en la respuesta
        return JSONResponse(content=cliente.to_dict())
    # Si no se puede crear el cliente, lanzar una excepción HTTP
    raise HTTPException(status_code=404)


# Definir una ruta para actualizar los datos de un cliente existente
@app.put("/clientes/actualizar/", tags=["Clientes"])
async def clientes_actualizar(datos: ModeloCliente):
    if db.Clientes.buscar(datos.curp):
        # Si el cliente existe en la base de datos, actualizar sus datos utilizando los proporcionados
        cliente = db.Clientes.modificar(datos.curp, datos.nombre, datos.apellido)
        if cliente:
            # Sí se actualiza correctamente, devolver el cliente actualizado en la respuesta
            return JSONResponse(content=cliente.to_dict())
    # Si el cliente no se encuentra, lanzar una excepción HTTP con un mensaje de error
    raise HTTPException(status_code=404, detail="Cliente no encontrado")


# Definir una ruta para borrar un cliente por su CURP
@app.delete("/clientes/borrar/{curp}/", tags=["Clientes"])
async def clientes_borrar(curp: str):
    if db.Clientes.buscar(curp=curp):
        # Si el cliente existe en la base de datos, eliminarlo
        cliente = db.Clientes.borrar(curp=curp)
        return JSONResponse(content=cliente.to_dict())
    # Si el cliente no se encuentra, lanzar una excepción HTTP con un mensaje de error
    raise HTTPException(status_code=404, detail="Cliente no encontrado")
