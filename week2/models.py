from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(128), unique=True, index=True)
    hashed_password = Column(String(128))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(128), index=True)
    description = Column(String(128), index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class Room(Base):
    __tablename__ = "readingroom"
    id = Column(Integer, primary_key=True, index=True)
    room_number = Column(Integer)
    in_use = Column(Integer)
    not_use = Column(Integer)
    timestamp = Column(TIMESTAMP)
