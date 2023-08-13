from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import app.crud as crud
import app.models as models
import app.schemas as schemas
from app.database import SessionLocal, engine
import os


if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')



#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# GET endpoints

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

@app.get("/plantreminders/", response_model=list[schemas.PlantReminder])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_plantreminders(db, skip=skip, limit=limit)
    return items

@app.get("/plantreminders/plantname/", response_model=list[schemas.PlantReminder])
def read_plantreminders_by_plantname(plantname: str, db: Session = Depends(get_db)):
    plantreminders = crud.get_plantreminders_by_plantname(db, plantname=plantname)
    return plantreminders


@app.get("/plantreminders/lighting/", response_model=list[schemas.PlantReminder])
def read_plantreminders_by_lighting(lighting: str, db: Session = Depends(get_db)):
    plantreminders = crud.get_plantreminders_by_lighting(db, lighting=lighting)
    return plantreminders


@app.get("/plantreminders/watering/", response_model=list[schemas.PlantReminder])
def read_plantreminders_by_watering(watering: str, db: Session = Depends(get_db)):
    plantreminders = crud.get_plantreminders_by_watering(db, watering=watering)
    return plantreminders

# POST endpoints

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/users/{user_id}/plantreminders/", response_model=schemas.PlantReminder)
def create_item_for_user(
    user_id: int, item: schemas.PlantReminderCreate, db: Session = Depends(get_db)
):
    return crud.create_plantreminder(db=db, item=item, user_id=user_id)


# PUT endpoints

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db=db, user_id=user_id, user_update=user_update)

@app.put("/plantreminders/{plantreminder_id}", response_model=schemas.PlantReminder)
def update_plantreminder(plantreminder_id: int, plantreminder_update: schemas.PlantReminderUpdate, db: Session = Depends(get_db)):
    db_plantreminder = crud.get_plantreminders(db, plantreminder_id=plantreminder_id)
    if db_plantreminder is None:
        raise HTTPException(status_code=404, detail="Plant reminder not found")
    return crud.update_plantreminder(db=db, plantreminder_id=plantreminder_id, plantreminder_update=plantreminder_update)

# DELETE endpoints

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, user_id=user_id)

@app.delete("/plantreminders/{plantreminder_id}", response_model=schemas.PlantReminder)
def delete_plantreminder(plantreminder_id: int, db: Session = Depends(get_db)):
    db_plantreminder = crud.get_plantreminders(db, plantreminder_id=plantreminder_id)
    if db_plantreminder is None:
        raise HTTPException(status_code=404, detail="Plant reminder not found")
    return crud.delete_plantreminder(db=db, plantreminder_id=plantreminder_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
