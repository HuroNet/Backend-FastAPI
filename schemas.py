from pydantic import BaseModel


class UserBaseModel(BaseModel):
    ideuser: int
    username: str
    password: str


