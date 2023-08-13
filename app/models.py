from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("PlantReminder", back_populates="owner")



class PlantReminder(Base):
    __tablename__ = "plantreminders"

    id = Column(Integer, primary_key=True, index=True)
    plant_name = Column(String, index=True)
    watering = Column(String, index=True)
    lighting = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


