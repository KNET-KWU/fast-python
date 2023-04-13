from typing import Union

from pydantic import BaseModel
from datetime import datetime


class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True


###


class ReadingroomBase(BaseModel):
    room_number: int
    in_use: int
    not_use: int
    timestamp: datetime


class ReadingroomCreate(ReadingroomBase):
    pass


class Readingroom(ReadingroomBase):
    id: int

    class Config:
        orm_mode = True
