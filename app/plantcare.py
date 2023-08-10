import json

from fastapi import FastAPI, Depends, HTTPException, status, Query, Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from typing import List, Optional

app = FastAPI()

# Simulated database for plant care reminders
class PlantReminder(BaseModel):
    id: int
    plant_name: str
    watering: str
    lighting: str

plant_reminders_db = [
    {"id": 1, "plant_name": "Spider Plant", "watering": "Keep soil evenly moist", "lighting": "Bright indirect light"},
    {"id": 2, "plant_name": "Snake Plant", "watering": "Water sparingly", "lighting": "Low to moderate light"},
    {"id": 3, "plant_name": "Peace Lily", "watering": "Keep soil consistently moist", "lighting": "Bright indirect light"},
    {"id": 4, "plant_name": "Pothos", "watering": "Allow soil to dry between waterings", "lighting": "Bright indirect light"},
    {"id": 5, "plant_name": "Monstera", "watering": "Water moderately", "lighting": "Bright indirect light"},
    {"id": 6, "plant_name": "Fiddle Leaf Fig", "watering": "Water when top inch of soil is dry", "lighting": "Bright indirect light"},
    {"id": 7, "plant_name": "ZZ Plant", "watering": "Water sparingly", "lighting": "Low to moderate light"},
    {"id": 8, "plant_name": "Aloe Vera", "watering": "Allow soil to dry between waterings", "lighting": "Bright indirect light"},
    {"id": 9, "plant_name": "Rubber Plant", "watering": "Water when top inch of soil is dry", "lighting": "Bright indirect light"},
    {"id": 10, "plant_name": "Calathea", "watering": "Keep soil consistently moist", "lighting": "Bright indirect light"},
    {"id": 11, "plant_name": "Succulent", "watering": "Water sparingly", "lighting": "Bright direct light"},
    {"id": 12, "plant_name": "Cactus", "watering": "Water very sparingly", "lighting": "Bright direct light"},
    {"id": 13, "plant_name": "Bamboo Palm", "watering": "Keep soil evenly moist", "lighting": "Bright indirect light"},
    {"id": 14, "plant_name": "English Ivy", "watering": "Keep soil consistently moist", "lighting": "Bright indirect light"},
    {"id": 15, "plant_name": "Dracaena", "watering": "Water moderately", "lighting": "Bright indirect light"},
    {"id": 16, "plant_name": "Hoya", "watering": "Allow soil to dry between waterings", "lighting": "Bright indirect light"},
    {"id": 17, "plant_name": "African Violet", "watering": "Keep soil evenly moist", "lighting": "Bright indirect light"},
    {"id": 18, "plant_name": "Fern", "watering": "Keep soil consistently moist", "lighting": "Low to moderate light"},
    {"id": 19, "plant_name": "Orchid", "watering": "Water when roots are dry", "lighting": "Bright indirect light"},
    {"id": 20, "plant_name": "Jade Plant", "watering": "Water sparingly", "lighting": "Bright direct light"},
    {"id": 21, "plant_name": "String of Pearls", "watering": "Allow soil to dry between waterings", "lighting": "Bright indirect light"},
    {"id": 22, "plant_name": "Money Tree", "watering": "Water moderately", "lighting": "Bright indirect light"},
    {"id": 23, "plant_name": "Begonia", "watering": "Keep soil consistently moist", "lighting": "Bright indirect light"},
    {"id": 24, "plant_name": "Ficus", "watering": "Water when top inch of soil is dry", "lighting": "Bright indirect light"},
    {"id": 25, "plant_name": "Philodendron", "watering": "Allow soil to dry between waterings", "lighting": "Bright indirect light"},
    {"id": 26, "plant_name": "Spiderwort", "watering": "Keep soil consistently moist", "lighting": "Low to moderate light"},
    {"id": 27, "plant_name": "Tradescantia", "watering": "Water moderately", "lighting": "Bright indirect light"},
    {"id": 28, "plant_name": "Fatsia", "watering": "Keep soil evenly moist", "lighting": "Bright indirect light"},
    {"id": 29, "plant_name": "Alocasia", "watering": "Allow soil to dry between waterings", "lighting": "Bright indirect light"},
    {"id": 30, "plant_name": "Cyclamen", "watering": "Water when top inch of soil is dry", "lighting": "Bright indirect light"},
    {"id": 31, "plant_name": "Schefflera", "watering": "Water sparingly", "lighting": "Low to moderate light"},
    {"id": 32, "plant_name": "Dieffenbachia", "watering": "Keep soil consistently moist", "lighting": "Bright indirect light"},
    {"id": 33, "plant_name": "Tradescantia", "watering": "Allow soil to dry between waterings", "lighting": "Bright indirect light"},
    {"id": 34, "plant_name": "African Daisy", "watering": "Water moderately", "lighting": "Bright indirect light"},
    {"id": 35, "plant_name": "Lavender", "watering": "Keep soil evenly moist", "lighting": "Bright indirect light"},
    {"id": 36, "plant_name": "Rosemary", "watering": "Allow soil to dry between waterings", "lighting": "Bright indirect light"},
    {"id": 37, "plant_name": "Mint", "watering": "Water when top inch of soil is dry", "lighting": "Bright indirect light"},
    {"id": 38, "plant_name": "Lemon Balm", "watering": "Water sparingly", "lighting": "Low to moderate light"},
    {"id": 39, "plant_name": "Thyme", "watering": "Keep soil consistently moist", "lighting": "Bright indirect light"},
    {"id": 40, "plant_name": "Oregano", "watering": "Allow soil to dry between waterings", "lighting": "Bright indirect light"},
    {"id": 41, "plant_name": "Basil", "watering": "Water moderately", "lighting": "Bright indirect light"},
    {"id": 42, "plant_name": "Chives", "watering": "Keep soil evenly moist", "lighting": "Bright indirect light"},
    {"id": 43, "plant_name": "Parsley", "watering": "Allow soil to dry between waterings", "lighting": "Bright indirect light"},
    {"id": 44, "plant_name": "Coriander", "watering": "Water when top inch of soil is dry", "lighting": "Bright indirect light"},
    {"id": 45, "plant_name": "Sage", "watering": "Water sparingly", "lighting": "Low to moderate light"},
    {"id": 46, "plant_name": "Cilantro", "watering": "Keep soil consistently moist", "lighting": "Bright indirect light"},
    {"id": 47, "plant_name": "Rose", "watering": "Allow soil to dry between waterings", "lighting": "Bright indirect light"},
    {"id": 48, "plant_name": "Daisy", "watering": "Water moderately", "lighting": "Bright indirect light"},
]

# GET endpoints


# dit is een test

@app.get("/plant-reminders/", response_model=List[PlantReminder])
async def get_plant_reminders():
    return plant_reminders_db

@app.get("/plant-reminders/{plant_id}", response_model=PlantReminder)
async def get_plant_reminder(plant_id: int):
    plant = next((p for p in plant_reminders_db if p["id"] == plant_id), None)
    if plant is None:
        raise HTTPException(status_code=404, detail="Plant reminder not found")
    return plant

@app.get("/plant-reminders/by-name/")
async def get_plant_reminders_by_name(plant_name: str):
    matching_plants = [p for p in plant_reminders_db if plant_name.lower() in p["plant_name"].lower()]
    return matching_plants

@app.get("/plant-reminders/recent/", response_model=List[PlantReminder])
async def get_recent_plant_reminders(limit: int = 5):
    recent_plants = sorted(plant_reminders_db, key=lambda p: p["id"], reverse=True)[:limit]
    return recent_plants

@app.get("/plant-reminders/care-instructions/{instruction_term}", response_model=List[PlantReminder])
async def get_plant_reminders_by_care_instruction(instruction_term: str):
    matching_plants = [p for p in plant_reminders_db if instruction_term.lower() in p["watering"].lower() or instruction_term.lower() in p["lighting"].lower()]
    return matching_plants


# POST endpoints
class PlantReminderCreate(BaseModel):
    plant_name: str
    watering: str
    lighting: str


@app.post("/plant-reminders/", response_model=PlantReminder)
async def create_plant_reminder(plant_reminder: PlantReminderCreate):
    new_id = max(p["id"] for p in plant_reminders_db) + 1
    new_plant_reminder = PlantReminder(
        id=new_id,
        plant_name=plant_reminder.plant_name,
        watering=plant_reminder.watering,
        lighting=plant_reminder.lighting,
    )
    plant_reminders_db.append(new_plant_reminder)
    return new_plant_reminder


@app.post("/plant-reminders/{plant_id}", response_model=PlantReminder)
async def update_plant_reminder(plant_id: int, plant_reminder: PlantReminderCreate):
    existing_plant = next((p for p in plant_reminders_db if p["id"] == plant_id), None)
    if existing_plant is None:
        raise HTTPException(status_code=404, detail="Plant reminder not found")

    existing_plant["plant_name"] = plant_reminder.plant_name
    existing_plant["watering"] = plant_reminder.watering
    existing_plant["lighting"] = plant_reminder.lighting

    return existing_plant

# PUT endpoints
@app.put("/plant-reminders/{plant_id}", response_model=PlantReminder)
async def update_plant_reminder(plant_id: int, plant_reminder_update: PlantReminderCreate):
    existing_plant = next((p for p in plant_reminders_db if p["id"] == plant_id), None)
    if existing_plant is None:
        raise HTTPException(status_code=404, detail="Plant reminder not found")

    existing_plant["plant_name"] = plant_reminder_update.plant_name
    existing_plant["watering"] = plant_reminder_update.watering
    existing_plant["lighting"] = plant_reminder_update.lighting

    return existing_plant

@app.put("/plant-reminders/by-name/{plant_name}", response_model=List[PlantReminder])
async def update_plant_reminders_by_name(plant_name: str, plant_reminder_update: PlantReminderCreate):
    matching_plants = [p for p in plant_reminders_db if plant_name.lower() in p["plant_name"].lower()]
    if not matching_plants:
        raise HTTPException(status_code=404, detail="No matching plant reminders found")

    updated_plants = []
    for plant in matching_plants:
        plant["plant_name"] = plant_reminder_update.plant_name
        plant["watering"] = plant_reminder_update.watering
        plant["lighting"] = plant_reminder_update.lighting
        updated_plants.append(plant)

    return updated_plants


# DELETE endpoints
@app.delete("/plant-reminders/{plant_id}")
async def delete_plant_reminder(plant_id: int):
    plant_to_delete = next((p for p in plant_reminders_db if p["id"] == plant_id), None)
    if plant_to_delete is None:
        raise HTTPException(status_code=404, detail="Plant reminder not found")

    plant_reminders_db.remove(plant_to_delete)
    return {"message": "Plant reminder deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
