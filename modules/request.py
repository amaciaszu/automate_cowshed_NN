import pandas as pd
import requests

def insert_df_to_table(url: str, df: pd.DataFrame):
    for _, row in df.iterrows():
        # Convert row to dict
        item_data = row.to_dict()

        response = requests.post(url, json=item_data)

        if response.status_code == 200:
            print(f"Inserted {item_data} successfully")
        else:
            print(f"Failed to insert {item_data}: {response.text}")