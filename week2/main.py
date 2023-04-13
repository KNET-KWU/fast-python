from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from .readingroom import get_reading_room
import asyncio
from datetime import datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_room_data():
    db = next(get_db())
    while True:
        # code to run periodically starts here
        rooom = await get_reading_room()
        # room[x] = {"in_use": using_list, "not_use": not_using_list}
        # code to run periodically ends here
        # sleep for 3 seconds after running above code
        for i, room in enumerate(rooom, start=1):
            사용중인_좌석수 = len(room["in_use"])
            비어있는_좌석수 = len(room["not_use"])
            crud.insert_readingroom_seats(
                db,
                schemas.ReadingroomCreate(
                    room_number=i,
                    in_use=사용중인_좌석수,
                    not_use=비어있는_좌석수,
                    timestamp=datetime.now(),
                ),
            )
        await asyncio.sleep(27)


@app.on_event("startup")
async def schedule_periodic():
    loop = asyncio.get_event_loop()
    loop.create_task(get_room_data())


@app.get("/room", response_model=list[schemas.Readingroom])
def get_room(db: Session = Depends(get_db)):
    return crud.get_readingroom_seats(db=db)


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
