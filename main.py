from fastapi import FastAPI
from database import database as connection
from database import engine 
from database import Base




app = FastAPI(title="project to rese;ar peliculas",
               description="peliculas",
               version="1")




@app.on_event("startup")
async def startup():
    await connection.connect()
    print("esta conectada")
    # Crear las tablas en la base de datos
    Base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
async def shutdown():
    # Desconectar de la base de datos
    await connection.disconnect()
    print('cerrando')






@app.get("/")
async def index():
    return "Project of backend conectado a la base de datos"


@app.get("/about")
async def about():
    return "About"
