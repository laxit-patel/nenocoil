import datetime
import itertools


def date_generator():
    fullday = datetime.datetime.now().strftime("%d")
    fullmonth = datetime.datetime.now().strftime("%m")
    fullyear = datetime.datetime.now().strftime('%Y')[2:4]
    day = ""
    month = ""
    day_dict = {'01': '1', '02': '2', '03': '3', '04': '4', '05': '5', '06': '6', '07': '7', '08': '8', '09': '9', '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F', '16': 'G', '17': 'H', '18': 'I', '19': 'J', '20': 'K', '21': 'L', '22': 'M', '23': 'N', '24': 'O', '25': 'P', '26': 'Q', '27': 'R', '28': 'S', '29': 'T', '30': 'U', '31': 'V'}

    month_dict = {'01': '1', '02': '2', '03': '3', '04': '4', '05': '5', '06': '6', '07': '7', '08': '8', '09': '9', '10': 'A', '11': 'B', '12': 'C'}

    for day_data in day_dict:
        if day_data == fullday:
            day = day_dict[day_data]

    for month_data in month_dict:
        if month_data == fullmonth:
            month = month_dict[month_data]

    if day == "":
        return "Invalid Day"
    elif month == "":
        return "Invalid Month"
    else:
        date = day + month + fullyear

    return date
