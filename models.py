from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Sequence

# from sqlalchemy.orm import relationship


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


# class Movie(Base):
#     __tablename__ = "movies"

#     title = Column(String(50))
#     created_at = Column(DateTime, server_default=func.now())

#     def __str__(self):
#         return self.title


# class UserReview(Base):

#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     movie_id = Column(Integer, ForeignKey("movies.id"))
#     review_text = Column(Text)
#     review_score = Column(Integer)

#     user = relationship("User", back_populates="reviews")
#     movie = relationship("Movie", back_populates="reviews")

#     def __str__(self):
#         return f"Review by {self.user} for {self.movie}"
