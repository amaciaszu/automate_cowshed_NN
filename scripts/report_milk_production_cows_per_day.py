import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.reports import generate_report_milk_production_cows_per_day
from modules.validations import is_valid_date


def main():
    date_input = input("Insert the date to generate report with milk production -- format (YYYY-MM-DD): ")
    if is_valid_date(date_input):
        informe = generate_report_milk_production_cows_per_day(date_input)
        print("*****************************************************************************")
        print("*****************************************************************************")
        print("REPORT MILK PRODUCTION FOR EACH COW PER DAY")
        print("*****************************************************************************")
        print("*****************************************************************************")
        for item in informe:
            print(f"COW_ID: {item['cow_id']}, MILK LITERS: {item['milk_liters']}")
    else:
        print("The input date is not a valid date. The correct format is YYYY-MM-DD")

if __name__ == "__main__":
    main()
