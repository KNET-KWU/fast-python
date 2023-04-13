from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# class Room(Base):
#     __tablename__ = "readingroom"
#     id = Column(Integer, primary_key=True, index=True)
#     room_number = Column(Integer)
#     in_use = Column(Integer)
#     not_use = Column(Integer)
#     timestamp = Column(TIMESTAMP)


def insert_readingroom_seats(db: Session, roomItem: schemas.ReadingroomCreate):
    db_item = models.Room(**roomItem.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_readingroom_seats(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Room).offset(skip).limit(limit).all()
