from sqlalchemy.orm import Session
from models.databasemodel import User
from interfaces.request import UserCreate
from fastapi import HTTPException
from datetime import datetime

def create_user(db: Session, user_data: UserCreate):
    new_user = User(first_name=user_data.first_name,
        last_name=user_data.last_name,
        username=user_data.username,
        email=user_data.email,
        date_of_birth=datetime.strptime(user_data.date_of_birth, r"%Y/%m/%d").date(),
        gender=user_data.gender,
        mobile=user_data.mobile,)  
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"User Created Successfully"}

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    
    return {"message": "User deleted successfully"}

def update_user(db:Session,user_id:int,change:str):
    user=db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User not Found")
    
    user.first_name=change
    db.commit()

    return {"message":"User updated successfully"}

def read_all(db:Session):
    user=db.query(User).all()

    if not user:
        raise HTTPException(status_code=404,detail="Table is Empty")
    
    return user

def read_one(db:Session, user_id:int):
    user=db.query(User).filter(User.id==user_id).one_or_none()

    if not user:
        raise HTTPException(status_code=404,detail="User is not Present")
    
    return user 