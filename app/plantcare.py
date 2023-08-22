from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app import auth
import secrets
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

security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"admin@mysite.com"
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"swordfish"
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "https://app-hderidder.cloud.okteto.net"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# GET endpoints

# @app.get("/users/me")
# def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
#    return {"username": credentials.username, "password": credentials.password}

@app.get("/users/me", response_model=schemas.User)
def read_users_me(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    current_user = auth.get_current_active_user(db, token)
    return current_user


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/plantreminders/")
def read_plantreminders(plantname: str = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if plantname:
        plantreminders = crud.get_plantreminders_by_plantname(db, plantname=plantname, skip=skip, limit=limit)
    else:
        plantreminders = crud.get_plantreminders(db, skip=skip, limit=limit)
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

@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    #Try to authenticate the user
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    #Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}

# PUT endpoints

@app.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db=db, user_id=user_id, user_update=user_update)


# DELETE endpoints

@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, user_id=user_id)

@app.delete("/plantreminders/{plantreminder_id}", response_model=schemas.PlantReminder)
def delete_plantreminder(plantreminder_id: int, db: Session = Depends(get_db)):
    db_plantreminder = crud.get_plantreminder_by_id(db, plantreminder_id)  # Use the new function
    if db_plantreminder is None:
        raise HTTPException(status_code=404, detail="Plant reminder not found")
    return crud.delete_plantreminder(db=db, plantreminder_id=plantreminder_id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
