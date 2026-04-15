from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
from database import engine, SessionLocal
import crud, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)


@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_user(db, user_id)


@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, name)


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db, user_id)