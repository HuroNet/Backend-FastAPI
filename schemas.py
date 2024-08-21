from pydantic import BaseModel


class UserBaseModel(BaseModel):
    username: str
    password: str


class MovieBaseModel(BaseModel):
    title: str


class UserReviewBaseModel(BaseModel):
    review_text: str
    userid: str
    movieid: str
