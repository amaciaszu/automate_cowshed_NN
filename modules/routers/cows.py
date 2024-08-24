from fastapi import APIRouter, HTTPException
from modules.schemas import Cow
from modules.crud import insert_cow, get_cow

router = APIRouter()

@router.post("/cows", response_model=Cow)
def create_cow(cow: Cow):
    cow_id = insert_cow(cow)
    return {"id": cow.id, "name": cow.name, "birthdate": cow.birthdate}

@router.get("/cow/{id}", response_model=Cow)
def read_cow(id: str):
    cow = get_cow(id)
    if not cow:
        raise HTTPException(status_code=404, detail="No records found for this cow")
    return dict(cow)
