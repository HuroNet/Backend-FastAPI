from sqlalchemy import Column, ForeignKey, Text, Integer, String, DateTime
# from sqlalchemy.sql import func
from database import Base
from sqlalchemy.orm import relationship
import datetime
# import hashlib


class User(Base):
    __tablename__ = "users"

    username = Column(String(50), primary_key=True, index=True)
    password = Column(String(50))

    # @classmethod
    # def create_password(cls, password):
    #     h = hashlib.md5()
    #     h.update(password.encode('utf-8'))
    #     return h.hexdigest()

    # @classmethod
    # def authenticate(cls, session, username, password):
    #     user = session.query(cls).filter_by(username=username).first()
    #     if user and user.password == cls.create_password(password):
    #         return user

    def __str__(self):
        return self.username


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    created_at = Column(DateTime, default=datetime.datetime.now)

    def __str__(self):
        return self.title


class UserReview(Base):
    __tablename__ = "user_reviews"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    movie_id = Column(Integer, ForeignKey("movies.id"))
    review = Column(Text)
    score = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now)

    # Relaciones con User y Movie
    user = relationship("User", back_populates="reviews")
    movie = relationship("Movie", back_populates="reviews")

    def __str__(self):
        return f"{self.user.username} - #{self.movie.title}"
