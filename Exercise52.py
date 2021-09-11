import datetime
import json


def get_date_time():
    date_time = datetime.datetime.now()
    formate_date = date_time.strftime("%m/%d/%Y, %H:%M:%S")

    date = formate_date.split()[0].replace(',', '')
    time = formate_date.split()[1]

    data = {
        'date': date,
        'time': time,
    }
    return json.dumps(data)

