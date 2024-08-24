from pydantic import BaseModel

class Cow(BaseModel):
    id: str
    name: str
    birthdate: str # format YYYY-MM-DD

class Sensor(BaseModel):
    id: str
    unit: str

class Measurement(BaseModel):
    sensor_id: str
    cow_id: str
    timestamp: float
    value: float

class CowMeasurement(BaseModel):
    cow_id: str
    cow_name: str
    timestamp: str # format YYYY-MM-DD HH:MM:SS
    value: float
    unit: str