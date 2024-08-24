from fastapi import HTTPException

from data_base.database import get_db_connection
from modules.models import Cow, Measurement, Sensor
from modules.validations import is_valid_date, is_valid_timestamp_float
from modules.queries import cow_last_datetime_measurements, cow_measurements_last_30_days_compare_last_datetime

def insert_cow(cow: Cow):
    conn = get_db_connection()
    cursor = conn.cursor()

    if cow.id == "":
        raise HTTPException(status_code=500, detail="Error inserting cow id in the database. COW ID must be a correct value")

    if not is_valid_date(cow.birthdate):
        raise HTTPException(status_code=500, detail="Error inserting cow birthdate in the database. Birthdate must be a valid date")

    try:
        cursor.execute('''INSERT OR IGNORE INTO cows (id, name, birthdate) VALUES (?, ?, ?)''',
                       (cow.id, cow.name, cow.birthdate))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Error inserting cow in the database")
    finally:
        conn.close()
    return {"id": cow.id, "name": cow.name, "birthdate": cow.birthdate}


def get_cow(id: str):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM cows where id = ?"
        cursor.execute(query,(id,))
        cow = cursor.fetchone()
    finally:
        conn.close()
    return cow

def insert_sensor(sensor: Sensor):
    conn = get_db_connection()
    cursor = conn.cursor()

    if sensor.id == "":
        raise HTTPException(status_code=500,
                            detail="Error inserting sensor id in the database. SENSOR ID must be a correct value")

    if sensor.unit == "" or (sensor.unit != "L" and  sensor.unit != "kg"):
        raise HTTPException(status_code=500,
                            detail="Error inserting sensor value in the database. SENSOR value must be L or kg")

    try:
        cursor.execute('''INSERT OR IGNORE INTO sensors (id, unit) VALUES (?, ?)''',
                       (sensor.id, sensor.unit))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Error inserting sensor in the database")
    finally:
        conn.close()
    return {"id": sensor.id, "unit": sensor.unit}

def get_sensor(id: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM sensors where id = ?"
    cursor.execute(query,(id,))
    sensor = cursor.fetchone()
    conn.close()
    return sensor

def insert_measurement(measurement: Measurement):
    conn = get_db_connection()
    cursor = conn.cursor()

    if measurement.sensor_id == "" or measurement.cow_id == "" or measurement.timestamp == "":
        raise HTTPException(status_code=500, detail="Error inserting register in the database. sensor_id, cow_id and timestamp must be a correct value")

    if not is_valid_timestamp_float(measurement.timestamp):
        raise HTTPException(status_code=500, detail="Error inserting timestamp in the database. Timestamp must be a valid date")

    if measurement.value < 0:
        raise HTTPException(status_code=500, detail="Error inserting value in the database. value must be a positive number")

    try:
        cursor.execute('''INSERT OR IGNORE INTO measurements (sensor_id, cow_id, timestamp, value) VALUES (?, ?, ?, ?)''',
                       (measurement.sensor_id, measurement.cow_id, measurement.timestamp, measurement.value))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail="Error inserting measurement in the database")
    finally:
        conn.close()
    return {"sensor_id": measurement.sensor_id, "cow_id": measurement.cow_id, "timestamp": measurement.timestamp, "value": measurement.value}

def get_cow_measurements_last_30_days(id: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Get MAX(TIMESTAMP) from measurements for the cow
    query = cow_last_datetime_measurements
    cursor.execute(query, (id,))
    max_timestamp = cursor.fetchone()
    max_timestamp_value = max_timestamp[0]

    # Get info on cow measurements for the last 30 days
    query = cow_measurements_last_30_days_compare_last_datetime
    cursor.execute(query,(id,max_timestamp_value,))
    cows_measurements = cursor.fetchall()
    conn.close()

    return cows_measurements