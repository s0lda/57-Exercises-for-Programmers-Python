import json
from Exercise52 import get_date_time

# didn't set up web server

def data_info():
    data = get_date_time()
    data = json.loads(data)
    for key, value in data.items():
        if key == 'date':
            date = value
        elif key == 'time':
            time = value

    print(f'The current time is: {time}\nDate: {date}')

if __name__ == '__main__':
    data_info()
