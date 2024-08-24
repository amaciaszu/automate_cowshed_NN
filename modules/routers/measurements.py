from fastapi import APIRouter, HTTPException
from modules.schemas import Measurement
from modules.crud import insert_measurement

router = APIRouter()

@router.post("/measurements", response_model=Measurement)
def create_measurement(measurement: Measurement):
    measurement_id = insert_measurement(measurement)
    return {"sensor_id": measurement.sensor_id, "cow_id": measurement.cow_id, "timestamp": measurement.timestamp, "value": measurement.value}
