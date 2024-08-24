from data_base.database import get_db_connection
from modules.queries import milk_productio_cow_per_day, cow_weight_comparation, cow_could_be_sick


def generate_report_milk_production_cows_per_day(day: str):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(milk_productio_cow_per_day,(day,))
    liters_milk_by_cow_per_day = cursor.fetchall()

    conn.close()
    return [{"cow_id": row[0], "milk_liters": row[1]} for row in liters_milk_by_cow_per_day]

def generate_report_cow_weight():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(cow_weight_comparation)
    cow_weight = cursor.fetchall()

    conn.close()
    return [{"cow_id": row[0], "current_weight": row[1], "avg_weight_last_30_days": row[2], "current_date": row[3]} for row in cow_weight]

def generate_report_cow_could_be_sick():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(cow_could_be_sick)
    cow_weight = cursor.fetchall()

    conn.close()
    return [{"cow_id": row[0], "current_weight": row[1], "avg_weight_last_30_days": row[2], "diff_weight": row[3], "current_date": row[4]} for row in cow_weight]

