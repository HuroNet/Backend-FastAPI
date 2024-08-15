from sqlalchemy import Column, Integer, String, DateTime, Sequence

# from sqlalchemy.sql import func
from database import Base
from sqlalchemy.sql import func

# import datetime

# def del modelo de secuencia
user_id_seq = Sequence("user_id_seq", start=1000)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, user_id_seq, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, server_default=func.now())

    def __str__(self):
        return self.username
