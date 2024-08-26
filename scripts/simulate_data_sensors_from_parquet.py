import sys
import os

pathAbs = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(pathAbs)
import pandas as pd
from modules.request import insert_df_to_table

def main():

    #####################################################
    #####################################################
    #SENSORS
    #####################################################
    #####################################################
    # Sensors file
    file_path_sensors = pathAbs + '\\data\\sensors.parquet'
    df_sensors = pd.read_parquet(file_path_sensors)
    
    # Clean dataframe
    # delete register with id null
    df_sensors = df_sensors[df_sensors['id'].notnull()]

    # Replace register with name or birthdate null
    df_sensors['unit'].fillna('no unit', inplace=True)

    insert_df_to_table("http://127.0.0.1:8000/sensors/", df_sensors)

    #####################################################
    #####################################################
    # COWS
    #####################################################
    #####################################################

    # Cows file
    file_path_cows = pathAbs + '\\data\\cows.parquet'
    df_cows = pd.read_parquet(file_path_cows)

    # Clean dataframe
    # delete register with id null
    df_cows = df_cows[df_cows['id'].notnull()]

    # Replace register with name or birthdate null
    df_cows['birthdate'].fillna('1900-01-01', inplace=True)
    df_cows['name'].fillna('no name', inplace=True)

    df_cows['birthdate'] = df_cows['birthdate'].astype(str)

    insert_df_to_table("http://127.0.0.1:8000/cows/", df_cows)

    #####################################################
    #####################################################
    # MEASUREMENTS
    #####################################################
    #####################################################

    # Measurements file
    file_path_measurements = pathAbs + '\\data\\measurements.parquet'
    df_measurements = pd.read_parquet(file_path_measurements)

    # Clean dataframe
    # delete register with id null
    df_measurements = df_measurements.dropna(subset=['sensor_id','cow_id','timestamp'])

    # Replace register with name or birthdate null
    df_measurements['value'].fillna('-1', inplace=True)

    insert_df_to_table("http://127.0.0.1:8000/measurements/", df_measurements)

if __name__ == "__main__":
    main()
