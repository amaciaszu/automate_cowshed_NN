from fastapi import FastAPI
from data_base.database import init_db
from modules.routers import cows, sensors, measurements, cows_measurements

# Create FASTAPI app
app = FastAPI()

# Inicializar la base de datos
init_db()

app.include_router(cows.router)
app.include_router(sensors.router)
app.include_router(measurements.router)
app.include_router(cows_measurements.router)
