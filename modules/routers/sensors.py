from fastapi import APIRouter, HTTPException
from modules.schemas import Sensor
from modules.crud import insert_sensor, get_sensor

router = APIRouter()

@router.post("/sensors", response_model=Sensor)
def create_sensor(sensor: Sensor):
    sensor_id = insert_sensor(sensor)
    return {"id": sensor.id, "unit": sensor.unit}

@router.get("/sensor/{id}", response_model=Sensor)
def read_sensor(id: str):
    sensor = get_sensor(id)
    if not sensor:
        raise HTTPException(status_code=404, detail="No records found for this sensor")
    return dict(sensor)
