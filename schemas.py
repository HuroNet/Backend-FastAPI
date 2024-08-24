from pydantic import BaseModel


class UserBaseModel(BaseModel):
    ideuser: int
    username: str
    password: str


class MovieBaseModel(BaseModel):
    title: str
    createal: TimeoutError


class UserReviewBaseModel(BaseModel):
    review_text: str
    userid: str
    movieid: str
