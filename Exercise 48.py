import requests, json, os


def user_input():
    valid = False
    while valid == False:
        try:
            usr_input = input('>> ')
            if len(usr_input) > 0:
                valid = True
                return usr_input
            else:
                print('Can\'t be empty.')
        finally:
            pass


def get_data(city, key):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}'
    response = requests.get(url)
    data = response.json()
    return data
    
# used round for temps for average user.
def get_temp_C(data):
    temperature = data['main']['temp']
    return round(temperature)


def convert_temp_F(temp):
    return round(temp * 1.8 + 32)


def get_sky(data):
    sky = data['weather']
    for item in sky:
        for key, value in item.items():
            if key == 'main':
                return value


def check_wind(data):
    wind = data['wind']['deg']
    if wind == 0:
        return 'North'
    elif wind > 0 and wind < 90:
        return 'North East'
    elif wind == 90:
        return 'East'
    elif wind > 90 and wind < 180:
        return 'South East'
    elif wind == 180:
        return 'South'
    elif wind > 180 and wind < 270:
        return 'South West'
    elif wind == 270:
        return 'West'
    else:
        return 'North West'


def check_weather(key):
    print('Where do you want to check weather?')
    city_valid = False
    while city_valid == False:
        try:
            city = user_input()
            data = get_data(city, key)
            # check if city was found in data base
            if data['cod'] == 200:
                city_valid = True
            else:
                print('Try again.')
        finally:
            pass

    c_temp = get_temp_C(data)
    f_temp = convert_temp_F(c_temp)
    sky = get_sky(data)
    wind = check_wind(data)
    print(f'\n{city.capitalize()} weather:\nTemp: {c_temp}C / {f_temp}F.\nPredicting {sky.lower()} for today.\nWind direction: {wind}.')


if __name__ == '__main__':
    # Free API key
    file_dir = os.path.dirname(__file__)

    with open(f'{file_dir}\ex48config.json', 'r') as f:
        f = json.load(f)
        for key, value in f.items():
            if key == 'key':
                api_key = value

    check_weather(api_key)
