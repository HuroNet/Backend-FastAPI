from fastapi import FastAPI, Depends
from database import database as connection

from database import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from models import User

# from schemas import UserBaseModel


app = FastAPI(
    title="project to rese;ar peliculas", description="peliculas", version="1"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
    print("cerrando")


@app.post("/users/")
def create_user(username: str, password: str, db: Session = Depends(get_db)):
    db_user = User(username=username, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.post("/movie/")
def create_movie(db:Session=Depends(get_db)):
    db_movie=0
    return db_movie


@app.get("/")
async def index():
    return "Project of backend conectado a la base de datos"


@app.get("/about")
async def about():
    return "About"
