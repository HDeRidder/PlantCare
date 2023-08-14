from sqlalchemy.orm import Session

import app.models as models
import app.schemas as schemas


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


def get_plantreminders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PlantReminder).offset(skip).limit(limit).all()


def create_plantreminder(db: Session, item: schemas.PlantReminderCreate, user_id: int):
    db_item = models.PlantReminder(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_plantreminders_by_plantname(db: Session, plantname: str, skip: int = 0, limit: int = 100):
    return db.query(models.PlantReminder).filter(models.PlantReminder.plant_name == plantname).offset(skip).limit(limit).all()


def get_plantreminders_by_lighting(db: Session, lighting: str, skip: int = 0, limit: int = 100):
    return db.query(models.PlantReminder).filter(models.PlantReminder.lighting == lighting).offset(skip).limit(limit).all()


def get_plantreminders_by_watering(db: Session, watering: str, skip: int = 0, limit: int = 100):
    return db.query(models.PlantReminder).filter(models.PlantReminder.watering == watering).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        return None
    for key, value in user_update.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user



# Delete user
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()
    return db_user


# Delete plant reminder
def delete_plantreminder(db: Session, plantreminder_id: int):
    db_plantreminder = db.query(models.PlantReminder).filter(models.PlantReminder.id == plantreminder_id).first()
    if db_plantreminder is None:
        return None
    db.delete(db_plantreminder)
    db.commit()
    return db_plantreminder