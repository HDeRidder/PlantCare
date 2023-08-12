from pydantic import BaseModel

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[PlantReminder] = []

    class Config:
        orm_mode = True


class PlantReminderBase(BaseModel):
    plant_name: str
    watering: str
    lighting: str

class PlantReminderCreate(PlantReminderBase):
    pass

class PlantReminder(PlantReminderBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


