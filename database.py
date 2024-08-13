# database.py
from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Crear una instancia de la base de datos
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/fastapi"
database = Database(DATABASE_URL)

# Crear un motor de SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Crear una base de datos
metadata = MetaData()
Base = declarative_base(metadata=metadata)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# crea una fábrica de sesiones configurada para trabajar con el
#  motor de base de datos que hemos creado.
