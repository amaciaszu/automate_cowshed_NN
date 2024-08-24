from fastapi import APIRouter, HTTPException
from typing import List
from modules.schemas import CowMeasurement
from modules.crud import get_cow_measurements_last_30_days

router = APIRouter()

@router.get("/cows/{id}", response_model=List[CowMeasurement])
def read_cow_measurements_last_30_days(id: str):
    cows_measures = get_cow_measurements_last_30_days(id)
    if not cows_measures:
        raise HTTPException(status_code=404, detail="No records found for this cow")

    cows_measures_output = [dict(cow) for cow in cows_measures]

    return cows_measures_output
