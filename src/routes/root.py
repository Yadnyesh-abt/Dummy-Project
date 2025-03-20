from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from configs.postgres import get_db
from interfaces.request import UserCreate
from queries.query import create_user, delete_user, read_all, update_user, read_one

router = APIRouter()


@router.post("/users/")
def add_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user_data)


@router.delete("/users/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    return delete_user(db, user_id)


@router.put("/users/{user_id}/{change}")
def change_user(user_id: int, change: str, db: Session = Depends(get_db)):
    return update_user(db, user_id, change)


@router.get("/users")
def output_user(db: Session = Depends(get_db)):
    return read_all(db)

@router.put("/users/{user_id}")
def one_user(user_id: int, db: Session = Depends(get_db)):
    return read_one(db,user_id)
