import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from modules.reports import generate_report_cow_weight

def main():
    informe = generate_report_cow_weight()
    print("*****************************************************************************")
    print("*****************************************************************************")
    print("REPORT FOR EACH COW CURRENT WEIGHT AND THE AVERAGE WEIGHT FOR THE LAST 30 DAYS")
    print("*****************************************************************************")
    print("*****************************************************************************")

    for item in informe:
        print(f"COW ID: {item['cow_id']}, CURRENT WEIGHT: {item['current_weight']}, AVERAGE WEIGHT LAST 30 DAYS: {item['avg_weight_last_30_days']}, CURRENT DATE: {item['current_date']}")

if __name__ == "__main__":
    main()
