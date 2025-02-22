from sqlalchemy.orm import Session
import models,schemas

def get_user_by_id(db:Session, user_id:int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db:Session, email:str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_all_users(db:Session, skip:int=0, limit:int=100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db:Session, user:schemas.UserCreate):
    db_user = models.User(email=user.email, hashed_password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_item(db:Session, skip:int = 0, limit:int =100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_new_itme(db:Session, item:schemas.ItemCreate, user_id:int):
    db_item = models.Item(title=item.title, description=item.description, owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item