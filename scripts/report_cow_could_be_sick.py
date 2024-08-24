from modules.reports import generate_report_cow_could_be_sick


def main():
    informe = generate_report_cow_could_be_sick()

    # Based on the data of the weights I have of the cows,
    # I assume that when a cow loses more than 10 kg with respect to the previous average values,
    # it can be determined that she may be sick.
    print("*****************************************************************************")
    print("*****************************************************************************")
    print("REPORT WITH THE LIST OF COWS THAT MIGHT BE SICK")
    print("*****************************************************************************")
    print("*****************************************************************************")
    if len(informe) == 0:
        print("No sick cows have been detected, none of the cows weighed more than 10 kg below their average weight.")
    for item in informe:
        print(f"COW ID: {item['cow_id']}, CURRENT WEIGHT: {item['current_weight']}, AVERAGE WEIGHT LAST 30 DAYS: {item['avg_weight_last_30_days']}, DIFF WEIGHT: {item['diff_weight']}, CURRENT DATE: {item['current_date']}")

if __name__ == "__main__":
    main()
