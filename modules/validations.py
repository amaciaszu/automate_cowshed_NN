from datetime import datetime

def is_valid_date(date_str, valid_format="%Y-%m-%d"):
    try:
        datetime.strptime(date_str, valid_format)
        print(datetime.strptime(date_str, valid_format))
        return True
    except ValueError:
        return False


def is_valid_timestamp_float(timestamp_value):
    try:
        datetime.fromtimestamp(timestamp_value)
        return True
    except (ValueError, OverflowError):
        return False