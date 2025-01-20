from fastapi import FastAPI, Depends, HTTPException
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import crud, models, schemas
from typing import List


models.Base.metadata.create_all(bind=engine)

app = FastAPI();

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create/user",response_model=schemas.User)
def create_user(user:schemas.UserCreate, db:Session=Depends(get_db)):
    db_user = crud.get_user_by_email(db,email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email Already exists")
    return crud.create_user(db=db,user=user)


@app.get("/user/{id}",response_model=schemas.User)
def getUserById(id:int,db:Session=Depends(get_db)):
    db_user = crud.get_user_by_id(db,user_id=id)
    if db_user is None:
        raise HTTPException(status_code=404,detail="User Not found")
    return db_user

@app.get("/all-user",response_model=List[schemas.User])
def getAllUSers(skip:int = 0, limit:int =100, db:Session=Depends(get_db)):
    users = crud.get_all_users(db,skip=skip,limit=limit)
     
    return users
